gender=input("enter your gender(male/female):")
first_name=input("enter your first name:")
last_name=input("enter your last name:")
age=input("enter your age:")
marital_status=input("are you married? (yes/no):")

if gender=='female':
    if marital_status=='married':
        print('Mrs')
    else:
        print('Ms.')
else:
    print('Mr.')

print("\nhello",first_name,last_name,age,"yearsold.")