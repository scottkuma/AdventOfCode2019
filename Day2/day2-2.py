import sys

filename = "test_day2.txt"

orig_data = open(filename).readlines()[0].split(',')

for noun in range(0,100):
    for verb in range(0,100):

        data = orig_data.copy()

        data[1] = str(noun)
        data[2] = str(verb)

        for x in range(0,len(data),4):
            if data[x] == '1':
                a = int(data[int(data[x+1])])
                b = int(data[int(data[x+2])])
                c = int(data[x+3])
                data[c] = str(a + b)

            elif data[x] == '2':
                a = int(data[int(data[x+1])])
                b = int(data[int(data[x+2])])
                c = int(data[x+3])
                data[c] = str(a * b)

            elif data[x] == '99':
                break

        if data[0] == '19690720':
            print(f"NOUN: {noun}, VERB: {verb}, Ans: {100 * noun + verb}\n")
            print("Original Data:\n" + ','.join(orig_data) + "\n")
            print("Check Data:\n" + ','.join(data))
            sys.exit()
