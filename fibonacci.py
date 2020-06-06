n = int(input("enter the number of elements you want of series:"))
n1 = 0
n2 = 1
x = 0
print("the fibonacci series is:")
while(x<n):
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    x += 1
