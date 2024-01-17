result = ["h","t","t","h","t","h","h","t","t","t"]

head_count = 0
for i in result:
    if i=="h":
        head_count=head_count+1
print(head_count)

for i in range(1,11):
    if i%2==0:
        continue
    print(i**2)

month_list = ["jan", "feb", "mar", "apr","may"]
exp= [2100, 3400, 4500, 4300, 6500]

e =input("enter expense amount:")
e= int(e)

month = -1
for i in range(len(month_list)):
    if e==exp[i]:
        month=i
        break

if month!=-1:
    print(f'you spent {e} in {month_list[month]}')
else:
    print(f"you didn't spent {e} in any month")

race = 5
for i in range(1,5):
    print(f"you ran {i}kms")
    tired = input("are you tired:")
    if tired == "yes":

        print(f"you didnt finish the race but you ran {i} kms!!!")
        break
    elif tired == "no":
        continue

if i==4 and tired=="no":
    print("Congratulation for completing 5kms!!!")


for i in range(1,6):
    print("*"*i)

for i in range(1,6):
    s =""
    for j in range(i):
        s += "*"
    print(s)

