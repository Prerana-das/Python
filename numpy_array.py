import numpy as np
a=np.array([1,2,3,4,5,6])
print(a)
print("Index Two is",a[2])
a = np.array([[1, 1], [2, 2], [3, 3],[4, 4]])
print(a)
print("Array Dimension",a.ndim)
print("Array Size",a.size)
print("Array Shape",a.shape)
print("Datatype",a.dtype)
a = np.array([[1, 1], [2, 2], [3, 3]], dtype=complex)
print(a)
a=np.zeros((2,2))
print(a)
b=np.arange(1,4)
print(b)


