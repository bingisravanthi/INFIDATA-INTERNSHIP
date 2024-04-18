print("area of rectangle")
def areavolume(l,b,h):
    area1=l*b
    vol1=l*b*h
    return area1,vol1

print("function with return value example")
a=int(input("enter the length"))
b=int(input("enter the breadth"))
c=int(input("enter the height"))

area,vol=areavolume(a,b,c)
print("area of the rectangle is:",area)
print("volume of the rectangle is:",vol)