"""
File: blur.py
Name:
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img, x, y, blurfactor):
    """
    :param img:
    :return:
    """
    red_sum = 0
    green_sum = 0
    blue_sum = 0
    for x in range(x-1, x + 1 + 1):
        for y in range(y-1, y + 1 + 1):
            r = img.get_pixel(x, y)
            g = img.get_pixel(x,y)
            b = img.get_pixel(x,y)
            red_sum += r
            green_sum += g
            blue_sum += b
    red_sum = red_sum // ((1 * 2 + 1)**2)
    green_sum = green_sum // ((1 * 2 + 1) ** 2)
    blue_sum = blue_sum // ((1 * 2 + 1) ** 2)
    return (red_sum, green_sum, blue_sum)


def main():
    """
    TODO:
    """

    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    for x in range(1, old_img.width-1):
        for y in range(1, old_img.height-1):
            new_img = old_img.get_pixel((x,y))
            red2 =
    blurred_img = blur(old_img)
    for i in range(4):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
