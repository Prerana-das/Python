a=set([1,2,3])
print(a)
b=set([4,5,6])
print(b)
print(a.difference(b))
print(b.difference(a))
print(a.union(b))
#print(a.intersection(b))
a.update(b)
print(a)
num=[1,2,3,4,5]
print(range(len(num)),"\n")
for i in range(len(num)):
    print(num[i])

print("\n")
for n in num:
    print(n)

####bubble sort
def bubblesot(num):
    for i in range(len(num)-1):
        for j in range(len(num)-i-1):
            if num[j]>num[j+1]:
                temp=num[j]
                num[j]=num[j+1]
                num[j+1]=temp
    print(num)
bubble=[1,5,9,2,6]
bubblesot(bubble)

p=set([1,2,3,4,5,8])
print(p)
p.add(6)
print("Set p contains",p)
#p.discard(6)
print("Now Set p contains",p)
q=set([6,7,8,9,10])
print("union",p.union(q))
print("P-Q",p.difference(q))
print("Q-P",q.difference(p))

p=p.intersection(q)
print(p)
p.update(q)
print(p)

l=([1,2])
k=([1,2,3,4,5,6,7])
print(k)
z = l.issubset(k)
print(z)

A = {4, 1, 3, 5}
B = {6, 0, 4, 1, 5, 0, 3, 5}
print(A.issubset(B))

















