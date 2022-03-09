def max(x,y):
    if x>y:
        return "x is greater"
    else:
        return "y is greater"

x = int(input("enter the value of x :"))
y = int(input("enter the value of y :"))

result = max(x,y)

print(result)
