filename = "day8_data.txt"
data = open(filename,'r').readlines()[0].strip()
#print(data)

layers = []

image_width = 25
image_height = 6

layer_length = image_width * image_height

print(len(data))
print(layer_length)

for x in range(0,len(data),layer_length):
    #print(x-1)
    layer = data[x:x + (layer_length)]
    layers.append(layer)

fewest_zero_count = 99999
fewest_zero_index = 0

for l in range(len(layers)):
    if layers[l].count('0') < fewest_zero_count:
        fewest_zero_count = layers[l].count('0')
        fewest_zero_index = l

print(f"Layer {fewest_zero_index} has {fewest_zero_count} zeroes")

print(layers[fewest_zero_index])

num_ones = layers[fewest_zero_index].count('1')
num_twos = layers[fewest_zero_index].count('2')
print(f"{num_ones} * {num_twos} = {num_ones * num_twos}")
