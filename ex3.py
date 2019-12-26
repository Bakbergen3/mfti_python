from graph import *

penColor('black')
brushColor('yellow')
circle(200, 200, 100)

penColor('black')
brushColor('red')
circle(160, 180, 20)
circle(240, 180, 20)

penColor('black')
brushColor('black')
circle(160, 180, 10)
circle(240, 180, 10)

x1, y1 = 100, 140
x2, y2 = 180, 165
x3, y3 = x2 + 6, y2 - 6
x4, y4 = x1 + 6, y1 - 6
polygon([(x1, y1), (x2, y2), (x3, y3), (x4, y4)])

x1, y1 = 300, 135
x2, y2 = 220, 160
x3, y3 = x2 + 6, y2 + 6
x4, y4 = x1 + 6, y1 + 6
polygon([(x1, y1), (x2, y2), (x3, y3), (x4, y4)])

rectangle(150, 250, 250, 265)

run()