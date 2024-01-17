x = input('enter a number:')
y = input("Enter second number:")

z = int(x)/int(y)
print("Division is: ", z)

x = input('enter a number:')
y = input("Enter second number:")
try:
    z = int(x)/int(y)
except Exception as e:
    print("Exception occured:", e)
    z= None
print("Division is: ", z)

x = input('enter a number:')
y = input("Enter second number:")
try:
    z = int(x)/int(y)
except ZeroDivisionError as e:
    print("Division by zero exception")
    z= None
except TypeError as e:
    print("Type error exception")
    z = None
print("Division is: ", z)



