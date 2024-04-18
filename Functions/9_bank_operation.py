def create_account():
    global name,mobile,branch,balance
    name=input("enter your name:")
    mobile=input("enter your mobile number:")
    branch=input("enter your branch:")
    balance=float(input("enter initial balance"))
def deposite():
    global balance
    dep=float(input("enter an amount to deposite:"))
    balance=balance+dep
    print("update balance after deposite:",balance)
def withdraw():
    global balance
    wd=float(input("enter an amount to withdraw"))
    if(balance>=wd):
        balance=balance-wd

        print("update balance after withdraw:",balance)
    else:
         print("insufficient balance:")
def display():
    print("customer name:",name)
    print("customer mobile number:", mobile)
    print("customer branch:", branch)
    print("available balance:",balance)


print("welcome to SBI bank,create your account")
create_account()
while(True):
    ch=int(input("enter your choice 1:deposite 2:withdraw 3:display 4:exit"))
    if(ch==1):
        deposite()
    elif (ch==2):
        withdraw()
    elif (ch==3):
        display()
    elif (ch==4):
        exit(0)
    else:
        print("invalid choice")




