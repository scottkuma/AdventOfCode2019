from intcode2 import *
from collections import defaultdict

def update(screen, outstring):
    status = {'numBlocks': 0, 'score': 0, 'paddlePos': (), 'ballPos': ()}
    for i in range(0, len(outstring), 3):
        x = outstring[i]
        y = outstring[i+1]
        z = outstring[i+2]

        if x == -1 and y == 0:
            status['score'] = z
        else:
            screen[(x,y)] = z

    for k,v in screen.items():
        #print(k,v)
        if v == 2:
            status['numBlocks'] += 1
        elif v == 3:
            status['paddlePos'] = k
        elif v == 4:
            status['ballPos'] = k
        elif k == (-1,0):
            status['score'] = k
        else:
            pass
    return status

screen = defaultdict(int)

c = IntCode("input.txt", 'A', False)

c.process() #draw initial screen
status = update(screen, c.output)
print(status, 'N/A')
initialNumBlocks = status['numBlocks']
score = 0

while c.state != "STOPPED":
    c.output= []
    joystick = 0
    if status['paddlePos'][0] > status['ballPos'][0]:
        joystick = -1  #Move Left
    elif status['paddlePos'][0] < status['ballPos'][0]:
        joystick = 1   #Move Right
    c.process([joystick])
    status = update(screen,c.output)
    if status['score'] > 0:
        score = status['score']
    else:
        status['score'] = score
    print(status,joystick)

print("\n\n\n")
print(f"Initial # of blocks: {initialNumBlocks} (Part 1)")
print(f"Final Score: {status['score']}  (Part 2)")
