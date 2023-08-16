d = {'Edoardo': '- B A - A A B D D -', 'Gabriele': '- B A C A A B D D -'}
# d = {'Edoardo': '- B A C A A B D D -','Gabriele': '- B A C A A B D D -'}

s1 = d['Edoardo']
s2 = d['Gabriele']

if s1 == s2:
    print("esattamente uguali")
else:
    possibile_copia = True
    copiato = -1
    # scorro ogni due caratteri per eliminare gli spazi
    for i in range(0, len(s1), 2):
        # print(s1[i],s2[i])
        if s1[i] != s2[i]:
            if s1[i] == '-' and (copiato == -1 or copiato == 0):
                copiato = 0
            elif s2[i] == '-' and (copiato == -1 or copiato == 1):
                copiato = 1
            else:
                possibile_copia = False

    if not possibile_copia:
        print('compiti diversi')
    elif copiato == 0:
        print('il primo studente forse ha copiato')
    else:
        print('il secondo studente forse ha copiato')

