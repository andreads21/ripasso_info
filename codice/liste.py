l = [1, 4, 3, 0, 1]
print(l)

#operatore 'in' per fare ricerche all'interno della lista
print('operatore "in" <2 in l>')
b = 2 in l
print('type', type(b))
print('bool', b)

print('-' * 30)

#operatore 'del' per eliminare elementi della lista
print('operatore "del" <del l[2]>')
del l[2]
print(l)

print('-' * 30)

#metodo pop per eliminare elementi della lista e ritornarli
print('metodo "pop" <pop(1)>')
print('elemento rimosso', l.pop(1))
print(l)

print('-' * 30)

#metodo 'sort' ordina una lista
l = [8, 2, 0, 4, 6]
print(l)
l.sort()
print('lista ordinata con metodo "sort" (lista modificata)', l)

print('-' * 30)

#funzione 'sorted' ritorna la lista ordinata
l = [8, 2, 0, 4, 6]
print(l)
print('lista ordinata con funzione "sorted"', sorted(l))
print('lista non modificata', l)

print('-' * 30)

#cicla su una lista usando l'indice
print('ciclo per indice:')
for i in range(len(l)):
    print('index:',i)
    print('element:',l[i])

print('-' * 30)

#cicla su una lista usando gli elementi 
print('ciclo per elemento:')
for el in l:
    print('element:',el)

print('-' * 30)

#cicla su una lista usando indici e elementi 
print('ciclo per indice e elemento:')
for (i,el) in enumerate(l):
    print('index:',i)
    print('element:',el)
