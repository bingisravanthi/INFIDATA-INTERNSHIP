age=int(input("enter the age"))
if(age>=18 and age<30):
    gender=input("enter your gender m/f")
    if(gender=='m'):
        days=int(input("enter days"))
        wages=700*days
        print("wages is:",wages)
    elif(gender=='f'):
        days = int(input("enter days"))
        wages = 750 * days
        print("wages is:", wages)
    elif(gender=='m'):
        days = int(input("enter days"))
        wages = 800 * days
        print("wages is:", wages)
    elif(gender=='f'):
        days = int(input("enter days"))
        wages = 850 * days
    print("wages is:", wages)
