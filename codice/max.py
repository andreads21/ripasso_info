l = [0, 1, 2, 3, 4, 2, 5]
print(l)

# ciclo for (funziona solo per i positivi)
m = 0 # imposto il max al numero minore possibile
pos = 0
for i in range(len(l)):
	if l[i] > m:
		# se trovo un max salvo valore e posizione
		m = l[i]
		pos = i

print(f'massimo {m} in pos {pos}')

print('-'*30)

l = [-9, -1, -2, 0, -4, -2, -5]
print(l)
# ciclo for (trova anche per i negativi)
m = l[0] #imposto il max al primo elemento
pos = 0
for i in range(1,len(l)): #il controllo parte dal secondo
	if l[i] > m:
		# se trovo un max salvo valore e posizione
		m = l[i]
		pos = i

print(f'massimo {m} in pos {pos}')
