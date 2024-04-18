print("addition program using function")
def addition(n1,n2):
    result=n1,n2
    return result
print("function with return parameter demo")
a=int(input("enter the first int num:"))
b=int(input("enter the second int num:"))
sum=addition(a,b)
print("add of {0} and {1} is {2}".format(a,b,sum))
print("end of the program")