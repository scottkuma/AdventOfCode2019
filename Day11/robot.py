from collections import defaultdict

class Robot:

    def __init__(self):
        self.numMoves = 0
        self.direction = '^'
        self.numPanelsPainted = 0
        self.panelsPainted = set()
        self.loc = (0,0)
        self.min_x = 0
        self.max_x = 0
        self.min_y = 0
        self.max_y = 0
        self.panels = defaultdict(int)
        # init default map color for spot
        # self.panels[self.loc] = 0  # Part 1 needed a black start spot
        self.panels[self.loc] = 1 # Part 2 needs a WHITE start spot

    def __str__(self):
        output = f"\n\n\nMove #{self.numMoves}\n{'-' * 20}\n"
        output += f"Location: {self.loc}\n"
        output += f"Direction: {self.direction}\n"
        output += f"Curr Panel Color: {self.panels[self.loc]}\n"
        output += f"Unique Panels Painted: {len(self.panelsPainted)}\n"
        output += f"Total Panels Painted: {self.numPanelsPainted}\n"
        output += f"Bounds: ({self.min_x}, {self.min_y}) --> ({self.max_x}, {self.max_y})"
        return output

    def turnRight(self):
        if self.direction == '^':
            self.direction = '>'
        elif self.direction == '>':
            self.direction = 'v'
        elif self.direction == 'v':
            self.direction = '<'
        else:
            self.direction = '^'

    def turnLeft(self):
        if self.direction == '^':
            self.direction = '<'
        elif self.direction == '<':
            self.direction = 'v'
        elif self.direction == 'v':
            self.direction = '>'
        else:
            self.direction = '^'

    def moveForward(self,numPanels=1):
        if self.direction == '^':
            self.loc = (self.loc[0], self.loc[1] + numPanels)
        elif self.direction == '>':
            self.loc = (self.loc[0] + numPanels, self.loc[1])
        elif self.direction == 'v':
            self.loc = (self.loc[0], self.loc[1] - numPanels)
        else:
            self.loc = (self.loc[0] - numPanels, self.loc[1])

    def paintPanel(self,color):
        self.panels[self.loc] = color
        self.numPanelsPainted += 1
        self.panelsPainted.add(self.loc)

    def getCurrPanelColor(self):
        return self.panels[self.loc]

    def getLoc(self):
        return self.loc

    def checkBounds(self):
        if self.loc[0] < self.min_x:
            self.min_x = self.loc[0]
        if self.loc[0] > self.max_x:
            self.max_x = self.loc[0]
        if self.loc[1] < self.min_y:
            self.min_y = self.loc[1]
        if self.loc[1] > self.max_y:
            self.max_y = self.loc[1]

    def showPanels(self):
        for y in range(self.max_y, self.min_y-1, -1):
            line = ''
            for x in range(self.min_x, self.max_x,1):
                if self.panels[(x,y)]:
                    line += '#'
                else: line += ' '
            print(line)

    def executeMove(self, color, turnDir):
        self.numMoves += 1
        self.paintPanel(color)
        if turnDir:
            self.turnRight()
        else:
            self.turnLeft()
        self.moveForward()
        self.checkBounds()
        print(self)
