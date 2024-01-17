street = "Don Street"
city = "Aberdeen"
country = "Scotland"
address = '\n'+street + '\n' +  city + '\n' + country
print("address using + operator:", address)

print(f'{street}\n{city}\n{country}')

data= "Earth resolves around the sun"
print(data[6:14])
print(data[-3:])

fruits = 4
veges = 5
print(f'I eat {fruits} fruits and {veges} veges daily')

data1 = "Maine 200 banana khaye"
data1 =data1.replace('banana', 'samosa')
data1 =data1.replace('200','10')
print(data1)

data2 = "Maine 200 banana khaye"
print(data2)
data2 = data2.replace('banana', 'samosa').replace('200','10')
print(data2)