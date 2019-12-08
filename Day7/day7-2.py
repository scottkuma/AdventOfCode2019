import sys
from itertools import permutations

from intcode2 import IntCode

filename = "day7_data.txt"
print ("Please input phase sequence:")
phase_input = input().strip()
max = 0
max_perm = None
for phase in permutations(phase_input,5):
    #phase = phase_input
    print(f"Trying Phase: {phase}")
    a = IntCode(filename, "A", False)
    b = IntCode(filename, "B", False)
    c = IntCode(filename, "C", False)
    d = IntCode(filename, "D", False)
    e = IntCode(filename, "E", False)

    a.process([phase[0]])
    b.process([phase[1]])
    c.process([phase[2]])
    d.process([phase[3]])
    e.process([phase[4]])

    while e.state != "STOPPED":
        a.process([e.output])
        b.process([a.output])
        c.process([b.output])
        d.process([c.output])
        e.process([d.output])

    if int(e.output) > max:
        print(f"NEW MAX! {e.output}")
        max = int(e.output)
        max_perm = phase

print(max, max_perm)
