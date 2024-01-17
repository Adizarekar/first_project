f =open("F://Education//DS_Roadmap//first_project//funny.txt", "w")
f.write("i love python")
f.write("i love java")
f.write("\ni love php")

f =open("F://Education//DS_Roadmap//first_project//funny.txt", "a")
f.write(" i love google")
f.close()

f =open("F://Education//DS_Roadmap//first_project//funny.txt", "r")
print(f.read())
f.close()

f =open("F://Education//DS_Roadmap//first_project//funny.txt", "r")
for line in f:
    print(line)
f.close()

f =open("F://Education//DS_Roadmap//first_project//funny.txt", "r")
for line in f:
    token = line.split(" ")
    print(str(token))
f.close()

f =open("F://Education//DS_Roadmap//first_project//funny.txt", "r")
for line in f:
    token = line.split(" ")
    print(len(token))
f.close()

with open("F://Education//DS_Roadmap//first_project//funny.txt", "r") as f:
    print(f.read())
print(f.closed)


