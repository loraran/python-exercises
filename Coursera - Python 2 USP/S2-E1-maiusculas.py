# Semana 02 - Exercício 1 - maiusculas.py

def maiusculas(frase):
    '''(string) -> string
    A função recebe uma frase (uma string) como parâmetro e devolve uma
    string com as letras maiúsculas que existem nesta frase, na ordem em
    que elas aparecem.
    '''

    frase = frase.strip()  # retirando espaços em branco
    maiusculas = ''
    for i in range(len(frase)):
        if 65 <= ord(frase[i]) <= 90:
            maiusculas = maiusculas + frase[i]
    print(maiusculas)
    return maiusculas


def test_maiusculas():
    frase = 'PrOgRaMaMoS em python!'
    assert maiusculas(frase) == 'PORMMS'


frase = 'PrOgRaMaMoS em python!'
maiusculas(frase)
