t1=(2,3,5,6,8,10)
print("t1 is:",t1)
l1=[]
l1=list(t1)#type conversion from tuple to list
print("list l1 is:",l1)
num=int(input("enter the element to add"))
l1.append(num)
t1=tuple(l1)#type conversion from list to tuple
print("update tuple is:",t1)