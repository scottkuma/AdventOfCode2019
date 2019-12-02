filename = "test_day2.txt"

data = open(filename).readlines()[0].split(',')
#data = [int(d) for d in data]

print(data)

for x in range(0,len(data),4):
    if data[x] == '1':
        a = int(data[int(data[x+1])])
        b = int(data[int(data[x+2])])
        c = int(data[x+3])
        print(f"pos {c} => {a} + {b} = {a+b}")
        data[c] = str(a + b)

    elif data[x] == '2':
        a = int(data[int(data[x+1])])
        b = int(data[int(data[x+2])])
        c = int(data[x+3])
        print(f"pos {c} => {a} * {b} = {a*b}")
        data[c] = str(a * b)

    elif data[x] == '99':
        break

print(','.join(data))
