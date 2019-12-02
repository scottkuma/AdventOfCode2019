filename = 'day1-1.txt'

def fuel_rec(mass):
    print(f"m:{mass}")
    fuel_mass = int(mass / 3) - 2
    if fuel_mass > 0:
        return fuel_mass + fuel_rec(fuel_mass)
    else:
        return 0
sum = 0
with open(filename,'r') as infile:
    #print(fuel_rec(14))
    #print(fuel_rec(1969))
    #print(fuel_rec(100756))
    for l in infile:
        sum += fuel_rec(int(l))

print(sum)
