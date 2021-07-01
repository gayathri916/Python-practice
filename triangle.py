def valid(a,b,c):
    if a+b>=c and b+c>=a and c+a>=b:
        return True
    else:
        return False


def type_of_triangle(a,b,c):
    if a==b and b==c:
        print('Triangle is Equilateral.')
    elif a==b or b==c or a==c:
        print('Triangle is Isosceles.')
    else:
        print('Triangle is Scalane')


a = float(input('Enter length of side a: '))
b = float(input('Enter length of side b: '))
c = float(input('Enter length of side c: '))


if valid(a, b, c):
    type_of_triangle(a, b, c)
else:
    print('Traingle is Invalid Tringle')