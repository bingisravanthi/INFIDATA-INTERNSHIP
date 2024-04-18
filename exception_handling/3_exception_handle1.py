a=10
b=0
try:
    div=a/b
    print("res of div:",div)
except ZeroDivisionError as e:
    print("you are trying to divide an int num by Zero")
    print("e value:",e)
except Exception as e:#generalised exception
    print("you are at generalised Exception block")
    print("e value:",e)
print("end")
