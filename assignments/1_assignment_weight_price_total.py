weight=0.5
numitems=5

if weight<1:
    price=1.45
if weight >=1:
    price=1.15
total=weight*price
if numitems >=10:
    total=total*0.9

print("weight",weight)
print("price",price)
print("total",total)
