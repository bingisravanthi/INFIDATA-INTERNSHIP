import numpy as np

four_by_five=np.array([[1,2,3,4,5],
                       [6,7,8,9,10],
                       [11,12,13,14,15],
                       [16,17,18,19,20]])
s1=four_by_five[0:1,0:6]
print("array first row:\n",s1)

s2=four_by_five[3:4,0:6]
print("array last row:\n",s2)

s3=four_by_five[2,3]
print("The element is:\n",s3)

s4=four_by_five[0:4,0:1]
print("Display first column:\n",s4)

s5=four_by_five[:,3:]
print("The elements is:\n",s5)

s6=four_by_five[1:3,3:5]
print("printing last two rows and columns:\n",s6)
