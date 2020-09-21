from intcode2 import IntCode

filename = "day9_test_data.txt"
a = IntCode(filename, "A", False)

# input = [1] # TEST
input = [2]

a.process(input)
