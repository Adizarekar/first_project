india = ["mumbai", "bangalore", "chennai", "delhi"]
pakistan = ["lohore", "karachi", "islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city = input("Enter a city:")

if city in india:
    print("This city is in India")
elif city in pakistan:
    print("This city is in Pakistan")
elif city in bangladesh:
    print("This city is in Bangladesh")
else:
    print("This city is unknown")


city1 = input("enter city number 1:")
city2 = input("enter city number 2:")

if city1 and city2 in india:
    print("both cities are in India")
elif city1 and city2 in pakistan:
    print("both cities are in Pakistan")
elif city1 and city2 in bangladesh:
    print("both cities are in Bangladesh")
else:
    print("They dont belong to same country")

sugar = input("Enter fasting sugar level:")

if int(sugar) <=80:
    print("Sugar is low")
elif 80 <int(sugar)<=100:
    print("Sugar is normal")
else:
    print("Sugar is high")

