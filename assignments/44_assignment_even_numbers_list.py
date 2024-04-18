def even(list):
    new=[]
    for i in list:
        if i%2==0:
            new.append(i)
        return new
li=[]
n=int(input("enter size of list"))
for i in range(0,n):
    e=int(input("enter element of list"))
    li.append(e)

print("even number in ",li)
print(even(li))
