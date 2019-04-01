data=[20,12,13,14,15]
n=len(data)
print("Array Length:",n)
loc=1
k=1
max = data[0]
while(k<n):
    if max<data[k]:
        loc=k
        max=data[k]
    k=k+1
print("Maximum Number is",max)

