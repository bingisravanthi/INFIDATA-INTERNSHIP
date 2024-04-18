'''
a=[1,2,3,4]
b=[3,4,5,6]
c=[x for x in a if x not in b]
print(c)

numbers=(4,7,19,2,89,45,72,22)
sorted_numbers=sorted(numbers)
odd_numbers=[x for x in sorted_numbers if x%2!=0]
print(odd_numbers)

t1=("hello","hi")
print(t1+("include helps","welcome you all"))

print(t1.count("can"))

t1=("can","you","can","a","can","as","a","canner","can","a","can")

tup=('30','3','2','8')
print(sorted(tup),reverse=True)

a=(1,2,3,4)
print(a[1:-1])

def tuple_comparison(tup1,tup2):
    return tup1<tup2
tup1=(66,4,17,4)
tup2=(66,4,16,5)
tuple_comarison(tup1,tup2)

def tuple_indexing(tup):
    tup[1]=800
    return tup
atuple=(100,200,300,400,500)
print(tuple_indexing(aTuple))

complete val=to set val to 20 by scling

def practice(tup):
    a,b,c=tup
    return a
atuple="Yellow",20,"Red"
practice(atuple)'''



