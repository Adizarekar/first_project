class employee:
    def __init__(self,i,n):
        self.id = i
        self.name = n
    def display(self):
        print(f"ID: {self.id} \nName:{self.name}")

emp = employee(1,"coder")
emp.display()

del emp.id
try:
    print(emp.id)
except Exception as e:
    print("Employee id not defined by error:", e)

del emp
try:
    emp.display()
except NameError:
    print("employee is not defined")
