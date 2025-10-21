import numpy as np
from PIL import Image, ImageOps
import math

img_mat = np.zeros((2000, 2000, 3), dtype=np.uint8)

# def draw_line(img_mat, x0, y0, x1, y1, color, count):
#     step = 1.0 / count
#     for t in np.arange(0, 1, step):
#         x = round((1.0 - t) * x0 + t * x1)
#         y = round((1.0 - t) * y0 + t * y1)
#         img_mat[y, x] = color

# def dotted_line(image, x0, y0, x1, y1, color):
#      count = math.sqrt((x0 - x1)**2 + (y0 - y1)**2)
#      step = 1.0/count
#      for t in np.arange (0, 1, step):
#         x = round ((1.0 - t)*x0 + t*x1)
#         y = round ((1.0 - t)*y0 + t*y1)
#         image[y, x] = color

# def x_loop_line(image, x0, y0, x1, y1, color):
#
#     for x in range(int(x0), int(x1)):
#         t = (x-x0)/(x1 - x0)
#         y = round ((1.0 - t)*y0 + t*y1)
#         image[y, x] = color

# def x_loop_line(image, x0, y0, x1, y1, color):
#     if (x0 > x1):
#         x0, x1 = x1, x0
#         y0, y1 = y1, y0
#
#     for x in range(int(x0), int(x1)):
#         t = (x-x0)/(x1 - x0)
#         y = round ((1.0 - t)*y0 + t*y1)
#         image[y, x] = color

# def x_loop_line(image, x0, y0, x1, y1, color):
#
#     xchange = False
#     if (abs(x0 - x1) < abs(y0 - y1)):
#         x0, y0 = y0, x0
#         x1, y1 = y1, x1
#         xchange = True
#
#     for x in range(int(x0), int(x1)):
#         t = (x-x0)/(x1 - x0)
#         y = round ((1.0 - t)*y0 + t*y1)
#         if (xchange):
#             image[x, y] = color
#         else:
#             image[y, x] = color

# def x_loop_line(image, x0, y0, x1, y1, color):
#
#     xchange = False
#     if (abs(x0 - x1) < abs(y0 - y1)):
#         x0, y0 = y0, x0
#         x1, y1 = y1, x1
#         xchange = True
#
#     if (x0 > x1):
#         x0, x1 = x1, x0
#         y0, y1 = y1, y0
#
#     for x in range(int(x0), int(x1)):
#         t = (x-x0)/(x1 - x0)
#         y = round ((1.0 - t)*y0 + t*y1)
#         if (xchange):
#             image[x, y] = color
#         else:
#             image[y, x] = color

def x_loop_line(image, x0, y0, x1, y1, color):

    xchange = False
    if (abs(x0 - x1) < abs(y0 - y1)):
        x0, y0 = y0, x0
        x1, y1 = y1, x1
        xchange = True

    if (x0 > x1):
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    y = y0
    dy = 2 * abs(y1 - y0)
    derror = 0.0
    y_update = 1 if y1 > y0 else -1

    for x in range(x0, x1):

        if (xchange):
            image[x, y] = color
        else:
            image[y, x] = color

        derror += dy
        if (derror > (x1 - x0)):
            derror -= 2 * (x1 - x0)
            y += y_update


# for k in range(13):
#     x0, y0, = 100, 100
#     x1 = int(100 + 95 * math.cos(2 * math.pi / 13 * k))
#     y1 = int(100 + 95 * math.sin(2 * math.pi / 13 * k))
#     x_loop_line(img_mat, x0, y0, x1, y1, 255)
#
# # img = Image.fromarray(img_mat, mode='RGB')
# # img.save('img.png')

file = open('model_1.obj')
v = []
f = []
for s in file:
    sp = s.split()
    if (sp[0] == 'v'):
        v.append([float(sp[1]), float(sp[2]), float(sp[3])])
    if (sp[0] == 'f'):
        f.append([int(sp[1].split('/')[0]), int(sp[2].split('/')[0]), int(sp[3].split('/')[0])])

# for vx, vy, vz in f:
#     x = int(1000 * vx + 1000)
#     y = int(1000 * vy + 1000)
#     z = int(1000 * vz + 1000)
#     img_mat[x, z] = 255

for k in range(len(f)):
    x0 = int(v[f[k][0] - 1][0] * 10000) + 1000
    y0 = int(v[f[k][0] - 1][1] * 10000) + 1000
    x1 = int(v[f[k][1] - 1][0] * 10000) + 1000
    y1 = int(v[f[k][1] - 1][1] * 10000) + 1000
    x2 = int(v[f[k][2] - 1][0] * 10000) + 1000
    y2 = int(v[f[k][2] - 1][1] * 10000) + 1000

    x_loop_line(img_mat, x0, y0, x1, y1, 255)
    x_loop_line(img_mat, x1, y1, x2, y2, 255)
    x_loop_line(img_mat, x2, y2, x0, y0, 255)




img = ImageOps.flip(Image.fromarray(img_mat, mode='RGB'))
img.save('img.png')
