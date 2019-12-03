
def manhattan_distance(point1, point2):
    a1 = point1[0]
    a2 = point1[1]
    b1 = point2[0]
    b2 = point2[1]

    distance = abs(a1 - b1) + abs(a2 - b2)
    return distance


def get_wire_points(wire):
    UDLR = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}

    pointlist = {}
    point = (0, 0)
    length = 0
    for command in wire:
        #print(command)
        drx = command[0]
        dist = int(command[1:])
        for _ in range(dist):
            length += 1
            point = (point[0] + UDLR[drx][0], point[1] + UDLR[drx][1])
            if point not in pointlist:
                pointlist[point] = length

    return pointlist


infile = "prod_data.txt"

# Parse wires into a set of lists

A, B, _ = open(infile, 'r').read().split('\n')

A = A.split(',')
B = B.split(',')
a_points = get_wire_points(A)
b_points = get_wire_points(B)

intersections = set(set(a_points) & set(b_points))

min_dist = 999999999
for i in intersections:
    if manhattan_distance((0, 0), i) < min_dist:
        min_dist = manhattan_distance((0, 0), i)

print(f"Part 1 Answer (min Manhattan Distance): {min_dist}")

min_sig_delay = 999999999
for i in intersections:
    if a_points[i] + b_points[i] < min_sig_delay:
        min_sig_delay = a_points[i] + b_points[i]

print(f"Part 2 Answer (min sig delay): {min_sig_delay}")
