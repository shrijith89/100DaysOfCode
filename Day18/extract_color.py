import colorgram

colors = colorgram.extract('spot_painting.jpg', 25)
color_list = []

for i in range(len(colors)):
    color_list.append((colors[i].rgb.r, colors[i].rgb.g, colors[i].rgb.b))

print(color_list)
