def fuel_rec(mass):
    print(f"m:{mass}")
    fuel_mass = int(mass) // 3 - 2
    if fuel_mass > 0:
        return fuel_mass + fuel_rec(fuel_mass)
    else:
        return 0

sum = 0
data = open("day1-1.txt").readlines()
    #print(fuel_rec(14))
    #print(fuel_rec(1969))
    #print(fuel_rec(100756))
for mass in data:
    sum += fuel_rec(int(mass))

print(sum)
