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

    def getIndirects(self):
        if self.parent is None:
            return []
        else:
            parent_indirects = self.parent.getIndirects()
            parent_indirects.append(self.parent)
            return parent_indirects

    def getDepth(self):
        return (len(self.getIndirects()))

objects = {}
first_object = ""
data = open("day6_data.txt", "r").readlines()
for d in data:
    l,r = d.strip().split(')')
    if first_object == "":
        first_object = l
    if l not in objects:
        objects[l] = OrbitingObject(l)
    if r not in objects:
        objects[r] = OrbitingObject(r,objects[l])
    else:
        objects[r].parent = objects[l]
        objects[l].link_to(objects[r])

#print(objects)
print(objects['YOU'])
you = set(objects['YOU'].getIndirects())
san = set(objects['SAN'].getIndirects())
common_nodes = you & san

min = 999999
for c in common_nodes:
    out = f"YOU --> {c.name} --> SAN"
    you_depth = objects['YOU'].getDepth() - 1 # don't count YOUR depth, count from the object you're orbiting!
    san_depth = objects['SAN'].getDepth() - 1 # don't count YOUR depth, count from the object you're orbiting!
    via_depth = objects[c.name].getDepth()
    if (you_depth - via_depth) + (san_depth - via_depth) < min:
        min = (you_depth - via_depth) + (san_depth - via_depth)
        out += f"  NEW MIN! {min}"
    print(out)
print(f"Min xfers = {min}")
