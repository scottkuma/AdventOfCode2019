class IntCode:

    def __init__(self, filename, debug = False):
        self.orig_data = open(filename).readlines()[0].strip().split(',')
        self.data = self.orig_data.copy()
        self.inst_pointer = 0
        self.output = None
        self.inputs = []
        self.debug = debug

    def log(self,s):
        if self.debug:
            print(s)

    def __str__(self):
        out = "<< "
        for x in range(len(self.data)):
            if x == self.inst_pointer:
                out += f"[[{self.data[x]}]] "
            else:
                out += f"{self.data[x]} "
        out += " >> \n"
        out += f"OUTPUT = {self.output}"
        return out

    def get_val(self, offset, mode = 0):
        if int(mode) == 0:
            self.log("POSITIONAL MODE")
            return int(self.data[int(self.data[self.inst_pointer + offset])])
        else:
            self.log("IMMEDIATE MODE")
            return int(self.data[self.inst_pointer+offset])

    def add(self, p1mode, p2mode):   # No return - changes memory
        a = self.get_val(1,p1mode)

        b = self.get_val(2,p2mode)

        c = self.get_val(3,1)

        self.log(f"ADD {a} {b} STO {c}")
        self.data[c] = str(a + b)
        self.inst_pointer += 4

    def mul(self, p1mode, p2mode):    # No return - changes memory
        a = self.get_val(1, p1mode)

        b = self.get_val(2, p2mode)

        c = self.get_val(3, 1)

        self.log(f"MUL {a} {b} STO {c}")
        self.data[c] = str(a * b)
        self.inst_pointer += 4


    def inp(self):
        if self.inputs == []:
            self.log("No auto-inputs found; enter required input...")
            in_val = input().strip()
        else:
            in_val = str(self.inputs.pop(0))
            #print(f"Auto input: {in_val}")
        a = self.get_val(1, 1)
        self.log(f"INP {in_val} STO {a} ")
        self.data[a] = in_val
        self.inst_pointer += 2


    def out(self, p1mode):
        a = self.get_val(1, p1mode)
        self.log(f"OUT {a}")
        self.log(f"\n\n{'*'*20}\n* OUTPUT: {a}\n{'*'*20}\n\n")
        self.output = a
        self.inst_pointer += 2

    def jit(self, p1mode, p2mode):
        a = self.get_val(1, p1mode)

        b = self.get_val(2, p2mode)

        self.log(f"JIT {a} ADR {b}")

        if a != 0:
            self.log(f"  JUMPING to {b}")
            self.inst_pointer = b
        else:
            self.inst_pointer += 3


    def jif(self, p1mode, p2mode):
        a = self.get_val(1, p1mode)

        b = self.get_val(2, p2mode)

        self.log(f"JIF {a} ADR {b}")

        if a == 0:
            self.log(f"  JUMPING to {b}")
            self.inst_pointer = b
        else:
            self.inst_pointer += 3


    def lt(self, p1mode, p2mode):
        a = self.get_val(1, p1mode)

        b = self.get_val(2, p2mode)

        c = self.get_val(3, 1)  #can't be in immediate mode

        self.log(f"LST {a} {b} STO {c}")
        if a < b:
            val = 1
        else:
            val = 0
        self.log(f"  VAL = {val}")
        self.data[c] = str(val)
        self.inst_pointer += 4


    def eql(self, p1mode, p2mode):
        a = self.get_val(1, p1mode)

        b = self.get_val(2, p2mode)

        c = self.get_val(3, 1)  #can't be in immediate mode

        self.log(f"EQL {a} {b} STO {c}")
        if a == b:
            val = 1
        else:
            val = 0
        self.log(f"  VAL = {val}")
        self.data[c] = str(val)
        self.inst_pointer += 4

    def process(self,inputs = []):
        self.inputs = inputs
        continue_flag = True
        while continue_flag:
            self.log(self)
            instruction = self.data[self.inst_pointer].strip().rjust(5,'0')
            self.log(f"Instruction @ postion {self.inst_pointer} => {instruction}")

            command = instruction[-2:]

            p1mode = instruction[2]
            p2mode = instruction[1]
            p3mode = instruction[0]
            self.log(f"inst_pointer: {self.inst_pointer} // Command: {command} // P-modes: {p1mode}, {p2mode}, {p3mode}")

            if command == '01':  # ADD
                self.add(p1mode,p2mode)

            elif command == '02':  # MUL
                self.mul(p1mode, p2mode)

            elif command == '03':
                self.inp()

            elif command == '04':
                self.out(p1mode)

            elif command == '05': #JUMP-IF-True
                self.jit(p1mode, p2mode)

            elif command == '06': #JUMP-IF-False
                self.jif(p1mode, p2mode)

            elif command == '07':  #LT
                self.lt(p1mode, p2mode)

            elif command == '08':   #EQL
                self.eql(p1mode, p2mode)

            elif command == '99':
                continue_flag = False

            else:
                print(f"{data[inst_pointer]}" )
                break
