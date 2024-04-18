i=int(input("enter the first int num"))
j=int(input("enter the second int num"))
k=int(input("enter the third int num"))

if i<j:
    if j<k:
        i=j
    else:
        j=k
else:
    if j>k:
       j=i
    else:
        i=k
print(i,j,k)