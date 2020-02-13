# Semana 02 - Exercício 2 - menor_nome.py

def menor_nome(nomes):
    '''(string) -> string
    A função recebe uma lista de strings com nome de pessoas como parâmetro
    e devolve o nome mais curto presente na lista.
    '''

    for i in range(len(nomes)):
        nomes[i] = nomes[i].strip()  # retirando espaços em branco
        nomes[i] = nomes[i].capitalize()  # capitalizando cada string

    menor_nome = nomes[0]
    
    for i in range(len(nomes)):
        if len(nomes[i]) < len(menor_nome):
            menor_nome = nomes[i]
   
    return menor_nome
