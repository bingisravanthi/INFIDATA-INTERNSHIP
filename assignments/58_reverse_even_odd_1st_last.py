t1=(10,12,2.4,"bengaluru",('a','b'))
l1=[]
l1=list(t1)
print("list l1 is:",l1)
print("l1[3]:",l1[2])#even index element
print("l1[3]:",l1[-2])#odd index element
print("l1[4][0] is:",l1[4][0])#display 'a' from t1
print("l1[4][0] is:",l1[4])#display last element from t1
l1.reverse()#reverse order
print("reverse of l1:",l1)