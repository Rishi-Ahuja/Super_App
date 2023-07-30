from PIL import Image
import numpy as np


def createexamples():
    numberArrayExamples = open('data.txt', 'a')
    numbersWeHave = range(0, 9)
    versionWeHave = range(1, 10)
    for eachNum in numbersWeHave:
        # print eachNum
        for furtherNum in versionWeHave:
            # you could also literally add it *.1 and have it create
            # an actual float, but, since in the end we are going
            # to use it as a string, this way will work.
            print(str(eachNum) + '.' + str(furtherNum))
            imgFilePath = 'images/numbers/' + str(eachNum) + '.' + str(furtherNum) + '.png'
            ei = Image.open(imgFilePath)
            eiar = np.array(ei)
            hh = str(eiar.tolist())
            print(hh)
            lineToWrite = str(eachNum) + '::' + hh + '\n'
            numberArrayExamples.write(lineToWrite)


createexamples()
'''n = 0 - 1
for x in range(0, 10):
    n = n + 1
    for y in range(1, 10):
        imn = str(x) + '.' + str(y) + '.png'
        # filename = 'Images/numbers/' + str(x) + '.' + str(y) + '.png'
        filename = 'Images/numbers/' + imn
        i = Image.open(filename)
        # i = Image.open('Images/numbers/%s.%s.png' % (x, y))
        j = str(n)
        iar = np.array(i)
        f = iar.tolist()
        s = str(f)
        final = '\n' + j + '::' + s
        with open('data.txt', 'a') as d:
            d.write(final)'''
