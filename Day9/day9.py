from intcode2 import IntCode

filename = "day9_test_data.txt"
a = IntCode(filename, "A", False)

# input = [1] # Part 1
input = [2] # Part 2

a.process(input)
