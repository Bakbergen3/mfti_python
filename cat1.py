from graph import *

#Creating common window
width, height = windowSize()
mask_ratio = 3/7

def paint_cat():
    masks(mask_ratio)
    window(width*0.6, 10, width - 10, height*mask_ratio - 10, 10)
    cat(20, 300, 1)


def masks(ratio):
    """
    Creates 2 background rectangles.
    ratio - ratio of the first rectangle to the
    total height
    """
    brushColor(83, 68, 35)
    rectangle(0, 0, width, height*ratio)
    penColor(127, 102, 1)
    brushColor(127, 102, 1)
    rectangle(0, height*ratio, width, height)


def window(x1, y1, x2, y2, gap):
    """
    Draws window.
    x1, y1 - the coordinates of left-upper corner
    x2, y2 - the coordinates of right-lower corner
    """
    penColor(215, 251, 220)
    brushColor(215, 251, 220)
    rectangle(x1, y1, x2, y2)

    penColor(136, 205, 221)
    brushColor(136, 205, 221)
    rectangle(x1 + gap, y1 + gap, x1 + (x2 - x1) / 2 - gap/2, y2 * 1/3)
    rectangle(x2 - gap, y1 + gap, x1 + (x2 - x1) / 2 + gap, y2 * 1/3)
    rectangle(x1 + gap, y2 * 1/3 + gap, x1 + (x2 - x1) / 2 - gap/2, y2 - gap)
    rectangle(x2 - gap, y2 * 1/3 + gap, x1 + (x2 - x1) / 2 + gap, y2 - gap)


def cat(x1, y1, scale):
    """
    Draws a cat.
    x1, y1 - the coordinates of left-upper corner
    x2, y2 - the coordinates of right-lower corner
    scale - the scale of the cat
    """

    penColor('black')
    brushColor(220, 113, 54)

    #tail
    oval(x1 + scale * 150, y1 + scale * +20, x1 + scale * 260, y1 + scale * 50)
    #body and head
    oval(x1 + scale * 25, y1 + scale * -10, x1 + scale * 180, y1 + scale * 70)
    oval(x1 + scale * 15, y1 + scale * +10, x1 + scale * 35, y1 + scale * +65)
    oval(x1, y1, x1 + scale * 60, y1 + scale * 55)
    oval(x1 + scale * 35, y1 + scale * 55, x1 + scale * 75, y1 + scale * 75)
    oval(x1 + scale * 130, y1 + scale * 30, x1 + scale * 185,y1 + scale * 80) #back leg
    oval(x1 + scale * 175, y1 + scale * 60, x1 + scale * 190,y1 + scale * 95)

    #eyes
    brushColor(147, 168, 8)
    circle(x1 + scale * 17, y1 + scale * 25, scale * 8)
    circle(x1 + scale * 43, y1 + scale * 25, scale * 8)

    brushColor('black')
    oval(x1 + scale * 17, y1 + scale * 32, x1 + scale * 19, y1 + scale * 18)
    oval(x1 + scale * 43, y1 + scale * 32, x1 + scale * 45, y1 + scale * 18)

    #ears
    brushColor(214, 170, 138)
    a1, b1 = x1 + scale * 17, y1 + scale * 5
    polygon([(a1, b1), (a1 - scale * 10, b1 + scale * 10), 
            (a1 - scale * 12, b1 - scale * 5)])
    a2, b2 = x1 + scale * 43, y1 + scale * 5
    polygon([(a2, b2), (a2 + scale * 10, b2 + scale * 10), 
            (a2 + scale * 12, b2 - scale * 5)])

    #nose
    a3, b3 = x1 + scale * 30, y1 + scale * 40
    polygon([(a3, b3), (a3 + scale * 2.5, b3 + scale * -8), 
        (a3 - scale * 2.5, b3 + scale * -8)])

    #mouth
    a4, b4 = x1 + scale * 30, y1 + scale * 45
    line(a4 + scale * 5, b4, a4 + scale * -5, b4)

if __name__ == "__main__":
    paint_cat()
    run()