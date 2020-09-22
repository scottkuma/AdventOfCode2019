from itertools import combinations
from planet import *

def printStep(steps,objs):
    print(f"After Step {steps}:")
    for o in objs:
        print(o)
    print("-" * 30)

def totalEnergy(objs):
    totE = 0
    for o in objs:
        totE += o.getKinE() * o.getPotE()
    return totE

def getState(objs):
    out = ""
    for o in objs:
        out += str(o)
    return out


planets = []

with open('data.txt', 'r') as infile:
    for line in infile.readlines():
        planets.append(Planet(line))
steps = 0


#printStep(steps, planets)

state = set()
state.add(getState(planets))


while steps < 1000:
    steps += 1
    for a, b in combinations(planets,2):
        for axis in 'xyz':
            if a.pos[axis] < b.pos[axis]:
                a.vel[axis] += 1
                b.vel[axis] -= 1
            elif a.pos[axis] > b.pos[axis]:
                a.vel[axis] -= 1
                b.vel[axis] += 1
    for p in planets:
        p.applyVelocity()

printStep(steps, planets)
print(f"e(total) = {totalEnergy(planets)}")
