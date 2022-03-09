def factorial(x):
    if x == 0:
        return 1
    else:
        return x*factorial(x-1)

x = int(input("enter the value of x"))

fact = factorial(x)

print(fact)