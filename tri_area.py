import math


def t_area(a, b, c):
    s = (a + b + c) / 2

    Area = math.sqrt((s * (s - a) * (s - b) * (s - c)))


    print(" The Area of a Triangle is %0.2f" % Area)


t_area(6, 7, 8)