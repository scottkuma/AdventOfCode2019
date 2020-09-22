class InvalidWriteValueError(Exception):
    pass

class InputError(Exception):
    pass

class IntCode:

    def __init__(self, filename, name, debug = False):
        self.orig_data = open(filename).readlines()[0].strip().split(',')
        self.data = self.orig_data.copy()
        for i in range(100):
            self.data.append(0)
        self.inst_pointer = 0
        self.output = []
        self.inputs = []
        self.debug = debug
        self.state = "START"
        self.name = name
        self.relative_base = 0
        self.log("IntCode computer initialized!")
        self.log(self)

    def log(self,s):
        if self.debug:
            print(f"{self.name} --> {s}")

    def __str__(self):
        out = "<< "
        for x in range(len(self.data)):
            if x == self.inst_pointer:
                out += f"[[{self.data[x]}]] "
            else:
                out += f"{self.data[x]} "
        out += f" >> \n"
        out += f"   RELBASE = {self.relative_base}\n"
        out += f"   INPUTS = {self.inputs}\n"
        out += f"   OUTPUT = {self.output}\n"
        out += f"   STATE = {self.state}"
        return out

    def get_val(self, offset, mode, rw = 'r'):
        position = int(self.data[self.inst_pointer + offset])
        if rw == 'r':
            if int(mode) == 0:
                self.log("POSITIONAL MODE")
                self.log(f"Fetching value from position {position}")
                base_val = int(self.data[position])
                self.log(f"BASEVAL = {base_val}")
                return base_val
            elif int(mode) == 1:
                self.log("IMMEDIATE MODE")
                return int(position)
            elif int(mode) == 2:
                base_val = position
                self.log("RELATIVE MODE")
                self.log(f"RBO = {self.relative_base} // BASEVAL = {base_val} ")
                return int(self.data[base_val + self.relative_base])
        else:
            if int(mode) == 0 or int(mode) == 1:
                self.log("POSITIONAL MODE (Write)")
                base_val = position
                self.log(f"BASEVAL = {base_val}")
                return int(base_val)
            elif int(mode) == 2:
                self.log("RELATIVE MODE (Write)")
                return int(position + self.relative_base)


    def add(self, p1mode, p2mode, p3mode):   # No return - changes memory
        a = self.get_val(1, p1mode)

        b = self.get_val(2, p2mode)

        c = self.get_val(3, p3mode, 'w')

        self.log(f"ADD {a} {b} STO {c}")
        self.data[c] = str(a + b)
        self.inst_pointer += 4

    def mul(self, p1mode, p2mode, p3mode):    # No return - changes memory
        a = self.get_val(1, p1mode)

        b = self.get_val(2, p2mode)

        c = self.get_val(3, p3mode, 'w')

        self.log(f"MUL {a} {b} STO {c}")
        self.data[c] = str(a * b)
        self.inst_pointer += 4


    def inp(self, p1mode):
        if len(self.inputs) == 0:
            self.log("No auto-inputs found; wait for required input")
            self.state = "INP_WAIT"
            return False
        else:
            self.log("Popping input...")
            in_val = str(self.inputs.pop(0))
            self.log(f"Accepting input: {in_val}")


        a = self.get_val(1, p1mode, 'w')
        #print(a)
        self.log(f"INP {in_val} STO {a} ")
        self.data[a] = in_val
        self.inst_pointer += 2


    def out(self, p1mode):
        a = self.get_val(1, p1mode)
        #print(f"OUT {a}")
        #print(f"\n\n{'*'*20}\n* OUTPUT: {a}\n{'*'*20}\n\n")
        self.output.append(a)
        self.inst_pointer += 2

    def jit(self, p1mode, p2mode):
        a = self.get_val(1, p1mode)

        b = self.get_val(2, p2mode)

        self.log(f"JIT {a} ADR {b}")

        if a != 0:
            self.log(f"  JUMPING to {b}")
            self.inst_pointer = int(b)
        else:
            self.inst_pointer += 3


    def jif(self, p1mode, p2mode):
        a = self.get_val(1, p1mode)

        b = self.get_val(2, p2mode)

        self.log(f"JIF {a} ADR {b}")

        if a == 0:
            self.log(f"  JUMPING to {b}")
            self.inst_pointer = int(b)
        else:
            self.inst_pointer += 3


    def lt(self, p1mode, p2mode, p3mode):
        a = self.get_val(1, p1mode)

        b = self.get_val(2, p2mode)

        c = self.get_val(3, p3mode, 'w')  #can't be in immediate mode

        self.log(f"LST {a} {b} STO {c}")
        if a < b:
            val = 1
        else:
            val = 0
        self.log(f"  VAL = {val}")
        self.data[c] = str(val)
        self.inst_pointer += 4


    def eql(self, p1mode, p2mode, p3mode):
        a = self.get_val(1, p1mode)

        b = self.get_val(2, p2mode)

        c = self.get_val(3, p3mode, 'w')  #can't be in immediate mode

        self.log(f"EQL {a} {b} STO {c}")
        if a == b:
            val = 1
        else:
            val = 0
        self.log(f"  VAL = {val}")
        self.data[c] = str(val)
        self.inst_pointer += 4

    def rbo(self, p1mode):
        a = int(self.get_val(1, p1mode))
        self.log(f"RBO {a}")
        self.relative_base = self.relative_base + a
        self.inst_pointer += 2

    def process(self,inputs = []):
        self.inputs = inputs
        if not self.state == "STOPPED":
            self.state = "RUN"
        else:
            print(f"{self.name} is STOPPED")

        while self.state == "RUN":
            self.log(self)
            instruction = self.data[self.inst_pointer].strip().rjust(5,'0')
            self.log(f"Instruction @ postion {self.inst_pointer} => {instruction}")

            command = instruction[-2:]

            p1mode = instruction[2]
            p2mode = instruction[1]
            p3mode = instruction[0]
            self.log(f"inst_pointer: {self.inst_pointer} // Command: {command} // P-modes: {p1mode}, {p2mode}, {p3mode}")

            if command == '01':  # ADD
                self.add(p1mode,p2mode, p3mode)

            elif command == '02':  # MUL
                self.mul(p1mode, p2mode, p3mode)

            elif command == '03':
                self.inp(p1mode)

            elif command == '04':
                self.out(p1mode)

            elif command == '05': #JUMP-IF-True
                self.jit(p1mode, p2mode)

            elif command == '06': #JUMP-IF-False
                self.jif(p1mode, p2mode)

            elif command == '07':  #LT
                self.lt(p1mode, p2mode, p3mode)

            elif command == '08':   #EQL
                self.eql(p1mode, p2mode, p3mode)

            elif command == '09':   #RBO
                self.rbo(p1mode)

            elif command == '99':
                self.state = "STOPPED"
                self.log(f" STOPPING")

            else:
                #print(f"{self.data[self.inst_pointer]}" )
                break
