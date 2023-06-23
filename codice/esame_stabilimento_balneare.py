f=open('stabilimento.txt','r', encoding='utf-8')
#lista di dizionari, ogni dizionario è una fila
file=[]
for fila in f:
    fila=fila.strip().split(', ')
    d={'o':fila[0], 'co':fila[1], 's':fila[2],'cs':fila[3]}
    file.append(d)
print(file)


f1=open('ingressi-uscite.txt','r', encoding='utf-8' )

dict={}
for persona in f1:
    persona=persona.strip().split(', ')
    if len(persona)> 1: #la persona sta entrando
        nome=persona[0]
        nomb=persona[1]
        nsedie=persona[2]
        buget=persona[3]
        trovata=False
        if trovata == False: #se non ho trovato la fila
            for fila in range(len(file)):
                if int(file[fila]['o'])>= int(nomb) and int(file[fila]['s'])>= int(nsedie) and ((int(nomb)*int(file[fila]['co']))+(int(nsedie)*int(file[fila]['cs'])))<= int(buget):
                    dict[nome] = fila + 1
                    trovata=True #se la trovo tolgo le sedie e gli ombrellloni occuoati e non entro più nel ciclo
                    if trovata and int(file[fila]['o'])!=0 and int(file[fila]['s'])!=0:
                            file[fila]['o']=int(file[fila]['o']) - int(nomb)
                            file[fila]['s']=int(file[fila]['s']) - int(nsedie)

                else:
                    trovata=False
    else:#la persona sta uscendo
        nomee=persona[0]
        file[fila]['o'] = int(file[fila]['o']) + int(nomb)
        file[fila]['s'] = int(file[fila]['s']) + int(nsedie)


print(dict)
for persona in f1:
    persona = persona.strip().split(', ')
    if len(persona)> 1:
        print(f'{persona[0]} è in fila {dict[persona[0]]}')
    else:
        print(f'{persona[0]} è uscito')