from math import atan2, degrees, sqrt
import operator

class Asteroid:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.visible = []

    def __str__(self):
        return f"{self.x},{self.y}"

    def getAngleToAsteroid(self, asteroid):
        x_diff = self.x - asteroid.x
        y_diff = self.y - asteroid.y
        return degrees(atan2(y_diff, x_diff))

    def getDistToAsteroid(self, asteroid):
        x_diff = asteroid.x - self.x
        y_diff = asteroid.y - self.y
        return sqrt(x_diff**2 + y_diff**2)

    def getVisibleAsteroids(self,asteroids):
        self.visible = {}
        #print(f"From asteroid @ ({self.x}, {self.y})")
        for loc, a in asteroids.items():
            #print(loc)
            if not loc == (self.x, self.y):
                a2a = self.getAngleToAsteroid(a)
                d2a = self.getDistToAsteroid(a)
                if a2a in self.visible:
                    if d2a < self.visible[a2a]['d']:
                        #print(f"   ({a.x}, {a.y}) is visible and blocks ({self.visible[a2a]['a'].x}, {self.visible[a2a]['a'].y})")
                        self.visible[a2a] = {'a': a, 'd': d2a}

                else:
                    print(f"   ({a.x}, {a.y}) is visible.")
                    self.visible[a2a] = {'a': a, 'd': d2a}

        return(self.visible)

data = open('day10_data.txt').readlines()

asteroids = {}

for y in range(len(data)):
    row = data[y].strip()
    for x in range(len(row)):
        if row[x] == '#':
            #print(f"a found @ {x},{y}")
            asteroids[(x,y)] = Asteroid(x,y)

#print(asteroids)
#print(len(asteroids))

max = 0
max_loc = None
for l,a in asteroids.items():
    num_vis = len(a.getVisibleAsteroids(asteroids))
    if num_vis > max:
        max = num_vis
        #print(l)
        max_loc = l

print(f"Part 1 solution: {max} visible from  {max_loc}")
#print(asteroids[max_loc])

print("\n\n\n\n")

vis_ast = asteroids[max_loc].getVisibleAsteroids(asteroids)

for v in vis_ast:
    print(str(v))

keys = sorted(asteroids[max_loc].getVisibleAsteroids(asteroids).keys())
#print(keys)
pos_angles = []
neg_angles = []
for k in keys:
    #print(k)
    if k < 0:
        neg_angles.append(k)
    else:
        pos_angles.append(k)

angles = pos_angles
angles.extend(neg_angles)

print(len(angles))

last_asteroid = asteroids[max_loc].getVisibleAsteroids(asteroids)[angles[199]]['a']
print(last_asteroid)

#print(last_asteroid.x * 100 +  last_asteroid.y)
