from PIL import Image, ImageDraw
import numpy as np
import os


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


# width, height = 128, 128
# data = np.zeros((height, width, 3), dtype=np.uint8)
data = None

if os.path.exists(ROOT_DIR + '\\canvas.png'):

    imgFrame = Image.open(ROOT_DIR + '\\canvas.png')
    data = np.array(imgFrame)
    img = Image.fromarray(data, 'RGB')
    img.save(ROOT_DIR + '\\square.png')

else:

    input('Mi serve canvas.png')
    exit(0)


x = int(input('x: '))
y = int(input('y: '))

width = data.shape[0]
height = data.shape[1]

with open(ROOT_DIR + '\\comandi.txt', 'w') as file:

    for i in range(0, width):
        for j in range(0, height):

            red = hex(data[j][i][0]).replace('0x', '').upper()
            green = hex(data[j][i][1]).replace('0x', '').upper()
            blue = hex(data[j][i][2]).replace('0x', '').upper()

            if len(red) == 1:
                red = '0' + red
            if len(green) == 1:
                green = '0' + green
            if len(blue) == 1:
                blue = '0' + blue

            color = str(red) + str(green) + str(blue)

            if color != 'FFFFFF':

                line = 'plop ' + str(x + i) + ' ' + str(y + j) + ' ' + color + '\n'
                file.write(line)