import numpy as np

#create ana array from list with type float
a1=np.array([[1,2,3],[4,5,6]],dtype='float')#creating an array with all float numbers
print("array contents are:",a1)#displaying the created array

#create array from tuple
a2=np.array((1,2,3))#creating an array from tuple
print("array created from tuple is:",a2)#displaying the created array

#creating a 16x173 array with all zeros
a3=np.zeros((16,173))
print("\nAn array initialized with all zeros:\n",a3)

#creating a 17x17array with all zeros
one=np.ones((17,17))
print("\nAn array initialized with all one:\n",one)

#create a matrix full of one number
a4=np.full((17,17),-24.6782)#order=17x17,required number=-24.6782
print("\nAn array initialized with all -24.6782 is:\n",a4)

#Create an array with random values
a5=np.random.random((3,2))
print("\nA random array:\n",a5)

#Create a sequence of integers from 0 to 40 with steps of 5
a6=np.arange(0,40,5)#start value displayed,end value is
print("\nA sequential array:\n",a6)

#Create a sequence of integers from 0 to 40 with steps of 5
a7=np.linspace(0,40,10)#both starting and end point is displayed in result
print("\nA sequential array with 10 value between 0 and 5:\n",a7)

#Flatten array
all=np.array([[11,2,3],[4,5,6]])
reshaped_array=all.reshape((1,-1))
reshaped_array_2=all.reshape((-1,1))

print("\nOriginal array:\n",all)
print("Reshaped array:\n",reshaped_array)
print("Reshaped array:\n",reshaped_array_2)



