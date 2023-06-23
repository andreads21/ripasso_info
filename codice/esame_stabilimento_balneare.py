f=open('stabilimento.txt','r', encoding='utf-8')
#lista di dizionari, ogni dizionario è una fila
file=[]
for fila in f:
    fila=fila.strip().split(', ')
    """ io le conversioni le metterei qui """
    d={'o':int(fila[0]), 'co':int(fila[1]), 's':int(fila[2]),'cs':int(fila[3])}
    file.append(d)
# print(file)


f1=open('ingressi-uscite.txt','r', encoding='utf-8' )

dict={}
"""devi memorizzare anche l'incasso"""
incasso = 0
for persona in f1:
    persona=persona.strip().split(', ')
    if len(persona)> 1: #la persona sta entrando
        nome=persona[0]
        nomb=persona[1]
        nsedie=persona[2]
        buget=persona[3]
        trovata=False
        for fila in range(len(file)):
            """occhio a dove piazzi questo if, come l'avevi messo tu all'inizio entrava e non lo ripassava mai """
            if trovata == False:  # se non ho trovato la fila
                if not trovata and file[fila]['o']>= int(nomb) and file[fila]['s']>= int(nsedie) and ((int(nomb)*file[fila]['co'])+(int(nsedie)*file[fila]['cs']))<= int(buget):
                    """ devi memorizzare anche gli ombrelloni e le sedie occupate altrimenti quando si libera il posto
                        non sai quante rimetterne libere"""
                    dict[nome] = {'f':int(fila), 'o':int(nomb), 's':int(nsedie)}
                    trovata=True #se la trovo tolgo le sedie e gli ombrellloni occuoati e non entro più nel ciclo
                    """ mi sembra inutile questo controllo"""
                    # if trovata and int(file[fila]['o'])!=0 and int(file[fila]['s'])!=0:
                    file[fila]['o']=file[fila]['o'] - int(nomb)
                    file[fila]['s']=file[fila]['s'] - int(nsedie)
                    incasso += int(nomb)*file[fila]['co']+(int(nsedie)*file[fila]['cs'])

                    print(f'{nome} è in fila {fila + 1}')

                """ puoi evitare di mettere questa parte"""
                # else:
                #     trovata=False

        """ tutte le file sono state controllate e non è stato trovato posto """
        if not trovata:
            print(f'Il cliente {nome} non ha trovato posto')

    else:#la persona sta uscendo
        nomee=persona[0]
        """ occhio che fila qui non è definito (lo è solo nel for a linea 24). fai attenzione a queste cose l'IDE 
            comunque ti avvisa """
        # file[fila]['o'] = int(file[fila]['o']) + int(nomb)
        # file[fila]['s'] = int(file[fila]['s']) + int(nsedie)
        file[dict[nomee]['f']]['o'] += dict[nomee]['o']
        file[dict[nomee]['f']]['s'] += dict[nomee]['s']

        print(f'{nomee} è uscito')

print(f"L'incasso della giornata è {incasso}")
"""
il dizionario 'dict' è solo usato per tenere traccia delle persone presenti in quel momento nello stabilimento non si
può usare alla fine per stampare le entrate/uscite in questo caso è molto più semplice farlo all'interno del programma
"""
# print(dict)
# for persona in f1:
#     persona = persona.strip().split(', ')
#     if len(persona)> 1:
#         print(f'{persona[0]} è in fila {dict[persona[0]]}')
#     else:
#         print(f'{persona[0]} è uscito')