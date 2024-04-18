print("function demo")
def addition(n1=2,n2=4):
    res=n1+n2
    print("add of{0} and {1} is {2}".format(n1,n2,res))
print("function with default value")
addition(15)
addition()
addition(10,6)
print("end of the program")