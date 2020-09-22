class Planet:
    def __init__(self, locstring):
        self.pos = {'x':0, 'y':0, 'z':0}
        self.vel = {'x':0, 'y':0, 'z':0}
        locarr = locstring.strip('< >\n').split(',')
        for axis in locarr:
            a,p = axis.strip().split('=')
            self.pos[a] = int(p)

    def applyVelocity(self):
        for axis in 'xyz':
            self.pos[axis] += self.vel[axis]

    def getPotE(self):
        potE = 0
        for axis in 'xyz':
            potE += abs(self.pos[axis])
        return potE

    def getKinE(self):
        kinE = 0
        for axis in 'xyz':
            kinE += abs(self.vel[axis])
        return kinE

    def __str__(self):
        out = f"pos=<x={self.pos['x']:4}, y={self.pos['y']:4}, z={self.pos['z']:4}> "
        out+= f"vel=<x={self.vel['x']:4}, y={self.vel['y']:4}, z={self.vel['z']:4}> "
        out+= f"e(p): {self.getPotE():4}  e(k): {self.getKinE():4}"
        return out

    def __repr__(self):
        out = f"Planet(pos=<x={self.pos['x']}, y={self.pos['y']}, z={self.pos['z']}> "
        out+= f"vel=<x={self.vel['x']}, y={self.vel['y']}, z={self.vel['z']}>)"
        return out
