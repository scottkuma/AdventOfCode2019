import time

def check_adjacent(value):
    l = list(str(value))
    found_adj = False
    for i in range(len(l)-1):
        if l[i] == l[i+1]:
            found_adj = True
            break
    return found_adj

def all_rising(value):
    l = list(str(value))
    found_falling = False
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            found_falling = True
            break
    return not found_falling

rangeString = "245182-790572"
lo, hi = [int(x) for x in rangeString.split('-')]

pwRange = range(lo, hi+1)
possibilities = []

for t in pwRange:
    if check_adjacent(t) and all_rising(t):
        possibilities.append(t)

print(f"{len(possibilities)} possibilities")
