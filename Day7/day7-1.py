import sys
import time
from itertools import permutations

from intcode import IntCode

filename = "day7_data.txt"
print ("Please input phase sequence:")
phase_input = input().strip()
max = 0
max_perm = None

for phase in permutations(phase_input):
    print(f"Trying Phase: {phase}")
    a = IntCode(filename, True)
    b = IntCode(filename)
    c = IntCode(filename)
    d = IntCode(filename)
    e = IntCode(filename)

    a.process([phase[0], 0])
    print("B")
    time.sleep(2)
    b.process([phase[1], a.output])
    print("C")
    c.process([phase[2], b.output])
    print("D")
    d.process([phase[3], c.output])
    print("E")
    e.process([phase[4], d.output])

    if int(e.output) > max:
        print(f"NEW MAX! {e.output}")
        max = int(e.output)
        max_perm = phase

print(f"HI SIGNAL = {max}")
