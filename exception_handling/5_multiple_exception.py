a=10
b=10
l1=[2,3,4,5]
try:
    print("list element is:",l1[3])
    div=a/b
    print("res of div:",div)
except ZeroDivisionError as e:
    print("you are trying to divide an int num by Zero")
    print("e value:",e)
except IndexError as e:
    print("your trying to access the wrong index ")
    print("e value:",e)
print("end")
