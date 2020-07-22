from PIL import ImageGrab
import os
import time

x_pad1 = 392
y_pad1 = 298
x_pad2 = 1028
y_pad2 = 778


def screenGrab():
    box = (x_pad1, y_pad1, x_pad2, y_pad2)
    im = ImageGrab.grab(box)
    im.show()


def main():
    screenGrab()


if __name__ == '__main__':
    main()
