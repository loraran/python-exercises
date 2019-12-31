# Semana 9 - Exercício - coh_piah.py

# Programa completo: Similaridades entre textos - Caso COH-PIAH

# --- TRAÇOS LINGUÍSTICOS ---

# Utilizaremos as seguintes estatísticas para detectar cópias:
#  1 - TAMANHO MÉDIO DE PALAVRA:
#       Média simples do número de caracteres por palavra.
#       Soma dos tamanhos das palavras dividido pelo total de palavras.
#  2 - RELAÇÃO TYPE-TOKEN:
#       Número de palavras diferentes utilizadas no texto divididas pelo
#       número total de palavras.
#  3 - RAZÃO HAPAX LEGOMANA:
#       Número de palavras utilizadas uma única vez dividido pelo número
#       total de palavras.
#  4 - TAMANHO MÉDIO DE SENTENÇA:
#       Média simples do número de caracteres por sentença.
#       Soma do número de caracteres de todas as sentenças dividida pelo
#       número de sentenças. Os caracteres que separam as sentenças NÃO
#       devem ser contabilizados.
#  5 - COMPLEXIDADE DE SENTENÇA:
#       Média simples do número de frases por sentença.
#       Número total de frases dividido pelo número de sentenças.
#  6 - TAMANHO MÉDIO DE FRASE:
#       Média simples do número de caracteres por frase.
#       Soma do número de caracteres em cada frase dividido pelo número
#       de frases no texto. Os caracteres que separam uma frase da outra
#       NÃO devem ser contabilizados.

# --- FUNCIONAMENTO DO PROGRAMA ---

# Seu programa deverá receber diversos textos e calcular os valores dos
# diferentes traços linguísticos. Após calcular esses valores para cada
# texto, você deve comparar com a assinatura fornecida.
# O grau de similaridade entre dois textos, 'a' e 'b', é dado por:

#    S(ab) = { Sigma[i=1,6] ||f(i,a) - f(i,b)|| } / 6   , onde:

#  - S(ab) é o grau de similaridade entre os textos a e b;
#  - f(i,a) é o valor de cada traço linguístico i no texto a; e
#  - f(i,b) é o valor de cada traço linguístico i no texto b.

# Quanto mais similares a e b forem, menor será S(ab).
# Para cada texto, calcule o grau de similaridade e exibir qual o texto
# que mais provavelmente foi escrito pelo plagiador.

import re
import math

# ---------- INICIO - FUNÇÕES SUPORTE (OBRIGATÓRIAS) ---------- #

def le_assinatura():
    # A função lê os valores dos traços linguísticos do modelo e devolve
    # uma assinatura a ser comparada com os textos fornecidos.
    print('Bem-vindo ao detector automático de COH-PIAH.\n')

    print('Insira, a seguir, os valores de assinatura.')
    wal = float(input('Entre o tamanho médio de palavra: '))
    ttr = float(input('Entre a relação Type-Token: '))
    hlr = float(input('Entre a Razão Hapax Legomana: '))
    sal = float(input('Entre o tamanho médio de sentença: '))
    sac = float(input('Entre a complexidade média de sentença: '))
    pal = float(input('Entre o tamanho médio de frase: '))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input('\nDigite o texto ' + str(i) + ' (aperte enter para sair): ')
    while texto:
        textos.append(texto)
        i += 1
        texto = input('\nDigite o texto ' + str(i) + ' (aperte enter para sair): ')

    return textos

def separa_sentencas(texto):
    # A função recebe um texto e devolve uma lista das sentenças dentro
    # de tal texto.
    sentencas = re.split(r'[.!?]+',texto)
    if sentencas[-1] == '':
        del sentencas[-1]

    return sentencas

def separa_frases(sentenca):
    # A função recebe uma sentença e devolve uma lista das frases dentro
    # de cada sentença.

    return re.split(r'[,:;]+',sentenca)

def separa_palavras(frase):
    # A função recebe uma frase e devolve uma lista das palavras dentro
    # de cada frase.

    return frase.split()

def n_palavras_unicas(lista_palavras):
    # Essa função recebe uma lista de palavras e devolve o número de
    # palavras que aparecem uma única vez.
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
    # Essa função recebe uma lista de palavras e devolve o número de
    # palavras diferentes utilizadas.
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

# ----------------------------------------------- #

def calcula_assinatura(texto):
    # IMPLEMENTADO!
    # Essa função recebe UM texto e deve devolver a assinatura do texto.
    # Devolva todos os fatores (traços linguísticos).

    newtexto = div_palavras(texto)

    soma_palavras = 0  # wal    
    for i in range(len(newtexto)):  # para cada palavra...
        soma_palavras = soma_palavras + len(newtexto[i])  # wal
    wal = soma_palavras / len(newtexto)  # TRAÇO 1 - PRONTO.
    # print('wal =',wal)

    diff_words = n_palavras_diferentes(newtexto)  # ttr
    same_words = n_palavras_unicas(newtexto)  # hlr

    ttr = diff_words / len(newtexto)  # TRAÇO 2 (Type-Token) - PRONTO.
    # print('ttr =',ttr)
    hlr = same_words / len(newtexto)  # TRAÇO 3 (Hapax-Legomana) - PRONTO.
    # print('hlr =',hlr)

    sentencas = separa_sentencas(texto)
    char_sentencas = 0
    for i in range(len(sentencas)):  # para cada sentença...
        char_sentencas = char_sentencas + len(sentencas[i])  # sal
    sal = char_sentencas / len(sentencas)  # TRAÇO 4 - PRONTO.
    # print('sal =',sal)

    allfrases = div_frases(texto)
    sac = len(allfrases) / len(sentencas)  # TRAÇO 5 - PRONTO.
    # print('sac =',sac)

    char_frases = 0
    for i in range(len(allfrases)):  # para cada frase...
        char_frases = char_frases + len(allfrases[i])
    pal = char_frases / len(allfrases)  # TRAÇO 6 - PRONTO.
    # print('pal =',pal)

    return [wal, ttr, hlr, sal, sac, pal]


def compara_assinatura(as_a, as_b):
    # IMPLEMENTADO!
    # Essa função recebe duas assinaturas de texto e devolve o grau de
    # similaridade nas assinaturas.
    # Implemente a fórmula do grau de similaridade.

    # as_a = ass_cp (modelo)
    # as_b = sign   (textos[i] vindo de avalia_textos)

    S_ab = 0
    i = 0
    while i < len(as_a):
        passo = math.fabs(as_a[i] - as_b[i])
        S_ab = S_ab + passo
        i = i + 1

    S_ab = S_ab / 6

    return S_ab


def avalia_textos(textos, ass_cp):
    # IMPLEMENTADO!
    # Essa função recebe uma lista de textos e deve devolver o número
    # (1 a n) do texto com maior probabilidade de ter sido plagiado.
    # Compara os valores de grau de similaridade (quanto menor).

    modelo = ass_cp
    assinaturas = []

    for i in range(len(textos)):  # para cada texto recebido...
        sign = calcula_assinatura(textos[i])  # assinatura de cada texto
        comp = [compara_assinatura(sign,modelo),i+1]  # comparativo de assinaturas
        assinaturas.append(comp)

    assinaturas = sorted(assinaturas)  # menor para maior
    print(assinaturas)
    coh_piadoh = assinaturas[0]
    
    return coh_piadoh[1]


# ---------- INICIO - FUNÇÕES EXTRA (OPCIONAIS) ---------- #

def div_palavras(texto):
    newtexto = []
    
    sentencas = separa_sentencas(texto)
    for i in range(len(sentencas)):  # para cada sentença...    
        frases = separa_frases(sentencas[i])
        for j in range(len(frases)):  # para cada frase da senteça...
            palavras = separa_palavras(frases[j])
            for k in range(len(palavras)):
                newtexto.append(palavras[k])

    # print(newtexto)  # o texto foi dividido em todas as palavras.
    return newtexto

def div_frases(texto):
    allfrases = []
    
    sentencas = separa_sentencas(texto)
    for i in range(len(sentencas)):  # para cada sentença...    
        frases = separa_frases(sentencas[i])
        for j in range(len(frases)):  # para cada frase da senteça...
            allfrases.append(frases[j])

    # print(allfrases)  # o texto foi dividido em todas as frases.
    return allfrases

# ---------- FIM - FUNÇÕES EXTRA (OPCIONAIS) ---------- #

ass_cp = le_assinatura()  # assinatura do MODELO.
textos = le_textos()
coh_piah = avalia_textos(textos,ass_cp)

print('\nO autor do texto',coh_piah,'está infectado com COH-PIAH.')
        
