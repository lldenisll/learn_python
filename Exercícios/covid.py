febre=input("Tem Febre? ")
dorcabeça=input("Tem dor de cabeça? ")
espirro=input("Tem secreção nasal ou espirro? ")
garganta=input("Tem dor de garganta? ")
tosse=input("Tem tosse seca? ")
respiração=input("Tem dificudlade respiratória? ")
dor=input("Tem dores no corpo? ")
diarreia=input("Tem diarréia? ")
viajou=input("Viajou nos últimos 14 dias para algum lugar com casos confirmados de Covid-19? ")
contato=input("Esteve em contato, nos últmos 14 dias, com um caso diagnósticado com Covid-19? ")
'fiz todas as perguntar para o usuário'
if str(febre) == ("Sim"):
    febrer=5
else:
    febrer=0
'determinei o valor caso a resposta do usuário seja sim para a pergunta, e caso contrário o valor é zero, fiz o mesmo para todas as perguntas'
    
if str(dorcabeça)== ("Sim"):
    dorcabeçar=1
else:
    dorcabeçar=0
    
if str(espirro)==("Sim"):
    espirror=1
else:
    espirror=0
    
if str(garganta)==("Sim"):
    gargantar=1
else:
    gargantar=0

if str(tosse)==("Sim"):
    tosser=3
else:
    tosser=0
    
if str(respiração)==("Sim"):
    respiraçãor=10
else:
    respiraçãor=0

if str(dor)==("Sim"):
    dorr=1
else:
    dorr=0
    
if str(diarreia)==("Sim"):
    diarreiar=1
else:
    diarreiar=0

if str(viajou)==("Sim"):
    viajour=3
else:
    viajour=0
if str(contato)==("Sim"):
    contator=10
else:
    contator=0

resultado=febrer+dorcabeçar+espirror+gargantar+tosser+respiraçãor+dorr+diarreiar+viajour+contator
'somei todos os resultados após o teste com o if de acordo com a resposta do usuário'
if resultado>=1 and resultado <=9:
    print("Risco Baixo")
if resultado>=10 and resultado<=19:
    print("Risco Médio")
if resultado>=20 and resultado<=36:
    print("Risco Alto")
'verifico a soma e imprimo a resposta de acordo com o resultado'
    
    