from intcode2 import *
from robot import *

r = Robot()
c = IntCode("input.txt", 'A', False)

while True:
    c.process([r.getCurrPanelColor()])
    if c.state != "STOPPED":
        direction = c.output.pop()  #backwards, but pop pulls from end
        color = c.output.pop()
        r.executeMove(color,direction)
    else:
        break

r.showPanels()
