filename = "day8_data.txt"
data = open(filename,'r').readlines()[0].strip()
#print(data)

layers = []

image_width = 25
image_height = 6

layer_length = image_width * image_height

for x in range(0,len(data),layer_length):
    layer = data[x:x + (layer_length)]
    layers.append(layer)

out = ""
for x in range(0,len(layers[0])):
    opaque = False
    for p in range(0,len(layers)):
        if not opaque:
            if layers[p][x] in "01":
                opaque = True
                out += layers[p][x]

print(out)
print(len(out))

out_image = []
for x in range(0,len(out),image_width):
    #print(x-1)
    row = out[x:x + (image_width)]
    out_image.append(row)

for row in out_image:
    row = row.replace('0',' ')
    print(row)
