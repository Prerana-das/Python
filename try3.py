import numpy as np
A=np.array([1,2,3,4,5,6])
B=A.reshape(3,2)
print ('B=', B)

print('Shape', B.shape, type(B))

###all element are zero
arr=np.zeros((4,4))
print(arr)

###all element are one
arr2=np.ones((4,4))
print(arr2)

###all elemnet are constant
arr3=np.full((4,4),4)
print(arr3)

###all element are random values
arr4=np.random.random((4,4))
print(arr4)

###Indentity matrix
arr5=np.eye(4,4)
print(arr5)

###arange means all numbers from 0 to n-1
arr6=np.arange(10)
print(arr6)

###Mix of tuple and lists
arr7 = np.array([[0, 1,2.0],[0,0,0],(1+1j,3.,2.)])
print(arr7)

j = np.linspace(1, 8, 3)
print(j)

arr8=np.linspace(1,20,4)
print(arr8)











