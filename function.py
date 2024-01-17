tom_expense = [12, 45,65,13,45]
joe_expense = [54,45,89,32,78,]

# total= 0
# for i in tom_expense:
#     total = total+i
# print("Toms total expence is: ", total)
#
# total= 0
# for i in joe_expense:
#     total = total+i
# print("joes total expence is: ", total)

def calculate_total(exp):
    """This function takes one argument and returns total of it"""
    total=0
    for i in exp:
        total = total+i
    return total
toms_total= calculate_total(tom_expense)
joes_total = calculate_total(joe_expense)

print("Toms total expence is: ", toms_total)
print("Joes total expence is: ", joes_total)


