exp = [2200, 2350, 2600, 2130, 2190]
print(exp[1]-exp[0])
print(sum(exp[:3]))
print(2000 in exp)
exp.append(1980)
print(exp)
exp[3]=(exp[3]-200)
print(exp)

heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']
print(len(heros))
# heros.append('black panther')
# print(heros)
# heros.remove('black panther')
# print(heros)
heros.insert(3, 'black panther')
print(heros)
heros[1:3]=['doctor strange']
print(heros)
#print(dir(heros))
heros.sort()
print(heros)