# Semana 05 - Exercício 3 - vogais.py

# Escreva a função 'vogal' que recebe um único caractere como parâmetro e devolve 'True' se ele for uma vogal e 'False' se for uma consoante.

def vogal(char):
    if not len(char) == 1:
        print('A entrada deve conter um único caractere.')
    else:
        if (char[0] == 'a') or (char[0] == 'A') or (char[0] == 'e') or (char[0] == 'E') or (char[0] == 'i') or (char[0] == 'I') or (char[0] == 'o') or (char[0] == 'O') or (char[0] == 'u') or (char[0] == 'U'):
            return True # char é uma vogal
        else:
            return False # char é uma consoante
