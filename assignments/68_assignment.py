d1={1:"java",2:"python",3:"web","name":"infidata"}
d1[2]="machine learning"
print("updated d1 is:",d1)

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


def practice(tup):
    a,b,c=tup
    return a
atuple="Yellow",20,"Red"
practice(atuple)

a=(1,2,3,4)
print(a[1:-1])

