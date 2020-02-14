import matplotlib.pyplot as plt

fig, axes = plt.subplots(figsize=(13,8))

with open('comics/1.png', 'rb') as map_file:
    map_img = plt.imread(map_file)

axes.imshow(map_img)
plt.plot([140], [220], 'r*')
plt.show()
