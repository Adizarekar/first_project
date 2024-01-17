data = {"china":143, "india":136, "usa":32, "pakistan": 21}

def print_all():
    for country,p in data.items():
        print(f"{country}==>{p}")

def add_country():
    country = input("enter a country:")
    if country in data:
        print("country already exist.. terminating")
        return
    pop = input("enter population:")
    pop = int(pop)
    data[country]=pop
    print_all()

def remove_country():
    country = input("enter country to remove:")
    if country in data:
        data.pop(country)
        print_all()
    else:
        print("country doesnt exist")

def query_country():
    country = input("enter country for query:")
    if country in data:
        print(data[country])
    else:
        print("country doesnt exist")
        return

def main():
    user_input = input("Please provide action(print, add, remove, query):")

    if user_input =="print":
        print_all()

    if user_input == "add":
        add_country()

    if user_input == "remove":
        remove_country()

    if user_input == "query":
        query_country()

if __name__ =='__main__':
    main()
#############################################################################################
import statistics
data = {"info":[600,630,620], "ril":[1430,1490,1567], "mtl":[234,180,160]}

data["info"].append(400)
print(data["info"])

def print_all():
    for s,v in data.items():
        print(f"{s} ==> {v} ==> avg: {statistics.mean(v)} ")

def add_stock():
    stock = input("enter stock to add:")
    price = input("enter price of stock:")
    price = float(price)
    if stock in data:
        data[stock].append(price)
    else:
        data[stock]= [price]
    print_all()
def main():
    operation = input("Enter action to perform(print, add):")

    if operation== "print":
        print_all()

    elif operation== "add":
        add_stock()
    else:
        print("unsupported action:", operation)

if __name__ == "__main__":
    main()
############################################################################################

import math

def circle_cal(r):
    r = float(r)
    diameter = 2*r
    area = 1/2* math.pi *r*r
    cirumference = 2 * math.pi *r
    return diameter, area, cirumference

if __name__ == "__main__":
    r= input("Enter radius of circle:")
    diameter, area, circumference = circle_cal(r)
    print(f"diameter= {diameter}, area = {area}, circumference = {circumference}")

