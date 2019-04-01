data = [5, 10, 15, 20, 25]

print("list of array data is", data)

x = int(input("enter a item to search: "))

loc = 0
k=1

while(loc==0):
    for k in range(len(data)):
        if data[k-1] == x:
            loc = k
            k=k+1
    if loc==0:
        print("Item is not in array data")
        break
    else:
        print("Item is in array data")



