book= {}

book["tom"] = {
    'name':'tom',
    'address': 'asd,dfg,NY',
    'phone': 4636483479
}

book["bob"] = {
    'name':'bob',
    'address': 'wder,rtyt, paris',
    'phone': 9876543987
}

import json
s= json.dumps(book)
print(s)

with open("F://Education//DS_Roadmap//first_project//book.txt", "w") as f:
    f.write(s)