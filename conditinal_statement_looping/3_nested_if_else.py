ch=int(input("select food categorey 1:veg,2:non_veg"))
if(ch==1):
    ch=int(input("select your food 1:dosa 2:bajji"))
    if(ch==1):
        print("you have orderd dosa...")
    elif(ch==2):
        print("you have ordered bajji...")
    else:
        print("invaild choice ")
elif(ch==2):
    print("you have selected non-veg dish")
else:
    print("invaild choice")