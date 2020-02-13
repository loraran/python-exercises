# Semana 02 - Exercício Adicional 2 - primeiro_lex.py

def primeiro_lex(lista):
    '''(list) -> string
    A função recebe uma lista de strings como parâmetro e devolve o primeiro
    string na ordem lexicográfica. Neste exercício, considere letras
    maiúsculas e minúsculas.
    Nota: ordem lexicográfica: ord()
    '''

    menor_lex = lista[0]
    for i in range(len(lista)):
        lista[i] = lista[i].strip()
        if ord(lista[i][0]) < ord(menor_lex[0]):
            menor_lex = lista[i]

    print(menor_lex)
    return menor_lex
        

primeiro_lex(['oĺá', 'A', 'a', 'casa'])
# deve devolver 'A'

primeiro_lex(['AAAAAA', 'b'])
# deve devolver 'AAAAAA'
