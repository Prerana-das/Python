import math

a =float(input("Enter the coefficients of a: "))
b= float(input("Enter the coefficients of b: "))
c = float(input("Enter the coefficients of c: "))

d = (b**2)-4*a*c

if d < 0:
    print ("No real solution")
elif d == 0:
    x = (-b+math.sqrt(b**2-4*a*c))/(2*a)
    print ("Has only one solutions: ", x)
else:
    x1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
    x2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
    print ("Has two solutions: ", x1, "&", x2)