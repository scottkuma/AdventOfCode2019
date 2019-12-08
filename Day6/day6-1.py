import sys

class OrbitingObject:
    def __init__(self, name, parent=None):
        self.parent = parent
        if parent != None:
            parent.link_to(self)
        self.name = name
        self.linked_to = []

    def link_to(self, orbobj):
        #print("Linking!")
        #print(orbobj)
        self.linked_to.append( orbobj)

    def checksum(self,depth=1):
        sum = 0
        for o in self.linked_to:
            sum += o.checksum(depth+1)
            print(f"name: {o.name} depth:{depth+1}")
        return sum + depth - 1

objects = {}
first_object = ""
data = open("day6_data.txt", "r").readlines()
for d in data:
    l,r = d.strip().split(')')
    if first_object == "":
        first_object = l
    #print(f"{l}  {r}")
    if l not in objects:
        objects[l] = OrbitingObject(l)
    if r not in objects:
        objects[r] = OrbitingObject(r,objects[l])
    else:
        objects[r].parent = objects[l]
        objects[l].link_to(objects[r])


for o in objects:
    if objects[o].parent is None:
        print(objects[o].name)
        print(f"{objects[o].name} CS: {objects[o].checksum()}")
