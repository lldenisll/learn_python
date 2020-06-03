#exercício final

#Neste exercício utilizaremos as seguintes estatísticas para detectar a doença:

#Tamanho médio de palavra: Média simples do número de caracteres por palavra.
#Relação Type-Token: Número de palavras diferentes utilizadas em um texto divididas pelo total de palavras.
#Razão Hapax Legomana: Número de palavras utilizadas uma vez dividido pelo número total de palavras.
#Tamanho médio de sentença: Média simples do número de caracteres por sentença.
#Complexidade de sentença: Média simples do número de frases por sentença.
#Tamanho médio de frase: Média simples do número de caracteres por frase.

import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def somapalavras(texto):
    sentenca = separa_sentencas(texto)
    frase = list()
    for i in sentenca:
        x = separa_frases(i)
        frase = x + frase
    palavra = list()
    for i in frase:
        x = separa_palavras(i)
        palavra = palavra + x

    soma = 0
    for i in palavra:
        soma =soma+ len(i)
    return soma
def listadepalavras(texto):
    sentenca = separa_sentencas(texto)
    frase = list()
    for i in sentenca:
        x = separa_frases(i)
        frase = frase + x
    palavra = list()
    for i in frase:
        x = separa_palavras(i)
        palavra = palavra+x
    return palavra
def caracteres(texto):
    sentenca = separa_sentencas(texto)
    frase = 0
    for i in sentenca:
        x = len(i)
        frase = frase + x
    return frase
def numeropalavras(texto):
    return len(listadepalavras(texto))
def numerosentencas(texto):
    return len(separa_sentencas(texto))
def numerofrases(texto):
    c = separa_sentencas(texto)
    frases = []
    for w in c:
        f = separa_frases(w)
        frases += f
    return len(frases)

def tamanho_médio_palavra(texto): #Média simples do número de caracteres por palavra.

    return somapalavras(texto)/numeropalavras(texto)
def typetoken (texto):#Relação Type-Token: Número de palavras diferentes utilizadas em um texto divididas pelo total de palavras.

    return n_palavras_diferentes(listadepalavras(texto))/numeropalavras(texto)
def hapaxlegomana(texto):    #Número de palavras utilizadas uma vez dividido pelo número total de palavras.

    n_palavras_unicas(listadepalavras(texto))/numeropalavras(texto)

def tamanho_médio_sentenca(texto):    #Média simples do número de caracteres por sentença.

    return caracteres(texto)/numerosentencas(texto)

def complexidade_sentenca(texto):    #Média simples do número de frases por sentença.

    return numerofrases(texto) / numerosentencas(texto)

def tamanho_frase(texto):    # Média simples do número de caracteres por frase.

    return caracteres(texto)/numerofrases(texto)

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    a=tamanho_médio_palavra(texto)
    b=typetoken(texto)
    c=hapaxlegomana(texto)
    d=tamanho_médio_sentenca(texto)
    e=complexidade_sentenca(texto)
    f=tamanho_frase(texto)
    return [a, b, c, d, e, f]
def compara_assinatura(ass_cp, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    i = 0
    j = 0
    k = 0
    comp_ass = list()
    while i <= 5:
        j = ass_cp[i] - as_b[i]
        if j < 0:
            comp_ass.append(j * -1)
        else:
            comp_ass.append(j)
        i = i + 1
    for k in comp_ass:
        j = i
        k = j + k
    return k / 6

def avalia_textos(lista_textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    comp_ass=[]
    for i in lista_textos:
        as_b = calcula_assinatura(i)
        comp_ass.append(as_b)
    ava = []
    for i in comp_ass:
        x = compara_assinatura(ass_cp, i)
        ava.append(x)
    return ava.index(min(ava)) + 1


ass_cp = le_assinatura()

lista_textos = le_textos()

print ('O autor do texto', avalia_textos(lista_textos, ass_cp), 'está infectado com COH-PIAH')