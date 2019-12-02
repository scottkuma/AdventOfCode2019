filename = 'day1-1.txt'

def fuel(mass):
    return(int(mass / 3) - 2)

with open(filename,'r') as infile:
    sum = 0
    for l in infile:
        sum += fuel(int(l))

print(sum) 
