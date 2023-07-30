with open('data.txt', 'r') as f:
    g = f.read()
listof90images = g.split('\n')
print(len(listof90images))
d = listof90images[0]
splitimageintolabelandpixel = d.split('::')
pixelstring = splitimageintolabelandpixel[1]
splitpixelintolist = pixelstring.split('],')
print(len(splitpixelintolist))
'''x = k[1].split('::')
y = x[1].split('], ')
train = usstring.split(', 255], ')
print(len(train))
print(len(y))
score = 0
for r in range(64):
    if train[r] == y[r]:
        score = score + 1
print(score)'''
