a = int(input("enter number:",a))
b = int(input("enter number:",b))
c = int(input("enter number:",c))

if a >= b and a >= c:
    print("Largest:", a)
elif b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)
