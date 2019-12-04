import time

def check_adjacent_d2(value):
    #2print(value)
    l = list(str(value))
    has_two = False
    curr_char = ''
    run_length = 0
    for i in range(len(l)):
        if curr_char != l[i]:
            # We have found start of new run
            # Did ended run end in multiple of 2?
            if run_length == 2:
                has_two = True
            curr_char = l[i]
            run_length = 1
        else:
            run_length += 1
        #print(run_length, curr_char, found_adj)

    #check at end
    if run_length ==2:
        has_two = True


    #print("-"*10)

    return has_two

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

#pwRange = [112233,123444,111122]

for t in pwRange:
    if check_adjacent_d2(t) and all_rising(t):
        possibilities.append(t)

print(possibilities)
print(f"{len(possibilities)} possibilities")
