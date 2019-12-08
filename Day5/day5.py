import sys

def show_data(data,pos):
    out = "<< "
    for x in range(len(data)):
        if x == pos:
            out += f"[[{data[x]}]] "
        else:
            out += f"{data[x]} "
    out += " >>"
    return out

filename = "day5_test_data.txt"

orig_data = open(filename).readlines()[0].strip().split(',')
data = orig_data.copy()
pos = 0



continue_flag = True



while continue_flag:
    print(show_data(data,pos))
    instruction = data[pos].strip().rjust(5,'0')
    #print(f"Instruction @ postion {pos} => {instruction}")

    command = instruction[-2:]

    p1mode = instruction[2]
    p2mode = instruction[1]
    p3mode = instruction[0]
    print(f"Pos: {pos} // Command: {command} // P-modes: {p1mode}, {p2mode}, {p3mode}")

    if command == '01':  # ADD
        if p1mode == '0':
            a = int(data[int(data[pos+1])])
        else:
            a = int(data[pos+1])

        if p2mode == '0':
            b = int(data[int(data[pos+2])])
        else:
            b=int(data[pos+2])

        c = int(data[pos+3])  #can't be in immediate mode

        print(f"ADD {a} {b} STO {c}")
        data[c] = str(a + b)
        pos += 4

    elif command == '02':  # MUL
        if p1mode == '0':
            a = int(data[int(data[pos+1])])
        else:
            a = int(data[pos+1])

        if p2mode == '0':
            b = int(data[int(data[pos+2])])
        else:
            b=int(data[pos+2])

        c = int(data[pos+3])  #can't be in immediate mode

        print(f"MUL {a} {b} STO {c}")
        data[c] = str(a * b)
        pos += 4

    elif command == '03':
        print("Enter required input...")
        in_val = input().strip()
        a = int(data[pos+1])
        print(f"IN {in_val} STO {a} ")
        data[a] = in_val
        pos += 2

    elif command == '04':
        if p1mode == '0':
            a = int(data[int(data[pos+1])])
        else:
            a = int(data[pos+1])
        print(f"OUT {a}")
        print(f"\n\n{'*'*20}\n* OUTPUT: {a}\n{'*'*20}\n\n")
        pos += 2

    elif command == '05': #JUMP-IF-True
        if p1mode == '0':
            a = int(data[int(data[pos+1])])
        else:
            a = int(data[pos+1])

        if p2mode == '0':
            b = int(data[int(data[pos+2])])
        else:
            b=int(data[pos+2])

        print(f"JIT {a} ADR {b}")

        if a != 0:
            print(f"  JUMPING to {b}")
            pos = b
        else:
            pos += 3
        #sys.exit()

    elif command == '06': #JUMP-IF-False
        if p1mode == '0':
            a = int(data[int(data[pos+1])])
        else:
            a = int(data[pos+1])

        if p2mode == '0':
            b = int(data[int(data[pos+2])])
        else:
            b=int(data[pos+2])

        print(f"JIF {a} ADR {b}")

        if a == 0:
            print(f"  JUMPING to {b}")
            pos = b
        else:
            pos += 3
        #sys.exit()

    elif command == '07':  #LT
        if p1mode == '0':
            a = int(data[int(data[pos+1])])
        else:
            a = int(data[pos+1])

        if p2mode == '0':
            b = int(data[int(data[pos+2])])
        else:
            b=int(data[pos+2])

        c = int(data[pos+3])  #can't be in immediate mode
        print(f"LST {a} {b} STO {c}")
        if a < b:
            val = 1
        else:
            val = 0
        print(f"  VAL = {val}")
        data[c] = str(val)
        pos += 4
        #sys.exit()

    elif command == '08':   #EQL
        if p1mode == '0':
            a = int(data[int(data[pos+1])])
        else:
            a = int(data[pos+1])

        if p2mode == '0':
            b = int(data[int(data[pos+2])])
        else:
            b=int(data[pos+2])

        c = int(data[pos+3])  #can't be in immediate mode
        print(f"EQL {a} {b} STO {c}")
        if a == b:
            val = 1
        else:
            val = 0
        print(f"  VAL = {val}")
        data[c] = str(val)
        pos += 4
        #sys.exit()

    elif command == '99':
        continue_flag = False

    else:
        print(f"{data[pos]}" )
        break
