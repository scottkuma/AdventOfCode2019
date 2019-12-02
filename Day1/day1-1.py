def fuel(mass):
    return(int(mass) // 3 - 2)

data = open('day1-1.txt').readlines()

sum = 0
for mass in data:
    sum += fuel(int(mass))

print(sum)
