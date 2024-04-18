def smallest(list):
    small=list[0]
    for i in list:
        if i<small:
            small=i
    return small
list=[1,2,3,4,8,9,10]
print("smallest in",list,"is")
print(smallest(list))