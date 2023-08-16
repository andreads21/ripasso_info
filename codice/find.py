l = [0, 1, 2, 3, 4, 2, 5]
print(l)
n = int(input('inserisci un numero da cercare '))
pos = -1

# ciclo for (si blocca alla prima occorrenza)
non_trovato = True
for i in range(len(l)):
	# controlla solo se il numero non è stato trovato
	if l[i]==n and non_trovato: 
		pos = i
		non_trovato = False

if(non_trovato):
	print('numero non trovato')
else:
	print('numero trovato in pos ' + str(pos))

print('-' * 30)

# ciclo for (trova ogni occorrenza)
non_trovato = True
for i in range(len(l)):
	if l[i]==n: 
		print('numero trovato in pos ' + str(i))
		non_trovato = False

if(non_trovato):
	print('numero non trovato')
