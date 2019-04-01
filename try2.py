check =1
while(check<5):
    print(check)
    check+=1

def foo(p):
    print("foo:", p)
    return
def bar(a,b=90):
    print("bar a:",a ,"bar b:", b)
    return
foo(111)
bar(222,333)
bar(55555555)

def foobar(*a):
    print(a,type(a))
    return
foobar(4)
foobar(1,2,3)
foobar({'Anni','Ruhi'},{'Mitu','Rupali'})








