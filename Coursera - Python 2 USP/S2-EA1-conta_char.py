# Semana 02 - Exercício Adicional 1 - conta_char.py

def conta_letras(frase, contar='vogais'):
    '''(string,string) -> int
    A função recebe como primeiro parâmetro uma string contendo uma frase
    e como segundo parâmetro uma outra string. Este segundo parâmetro deve
    ser opcional.
    Quando o segundo parâmetro for definido como "vogais", a função deve
    devolver o numero de vogais presentes na frase.
    Quando ele for definido como "consoantes", a função deve devolver o
    número de consoantes presentes na frase.
    Se este parâmetro não for passado para a função, deve-se assumir o valor
    "vogais" para o parâmetro.
    '''

    vogais = 'aeiouAEIOU'
    consoantes = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'

    frase = frase.strip()
    counter = 0
    if contar == 'consoantes':
        for i in range(len(frase)):
            if frase[i] in consoantes:
                counter += 1
    else:
        for i in range(len(frase)):
            if frase[i] in vogais:
                counter += 1

    return counter


conta_letras('programamos em python')
# deve devolver 6

conta_letras('programamos em python', 'vogais')
# deve devolver 6

conta_letras('programamos em python', 'consoantes')
# deve devolver 13
