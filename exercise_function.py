def area_triangle(b,h):
    area=1/2*(b*h)
    return area

base = input("base of Triangle:")
height = input("Height of Triangle:")

base = float(base)
height = float(height)

area= area_triangle(base,height)
print(f"area of triangle is {area}")
#################################################################################3
def area_triangle(b,h):
    area=1/2*(b*h)
    return area

def area_rectangle(b,h):
    area=(b*h)
    return area

dimension1 = input("base of object:")
dimension2 = input("Height of object:")
shape = input("Shape of object:")

dimension1 = float(dimension1)
dimension2 = float(dimension2)

if shape== "triangle":
    area= area_triangle(dimension1,dimension2)
    print(f"area of triangle is {area}")

elif shape== "rectangle":
    area=area_rectangle(dimension1,dimension2)
    print(f"area of rectangle is {area}")

else:
    print("shape is neither triangle nor rectangle"'\n' "area is none")
###################################################################################
def print_pattern(n):
    for i in range(n+1):
        print("*"*i)

s= input("star pattern number:" )
s = int(s)
print_pattern(s)

