# Semana 01 - Exercício Adicional 1 - imprime_matriz.py

def imprime_matriz(matriz):
    '''(list(list)) -> imprime_matriz()
    A função recebe uma matriz como parâmetro e a imprime linha por linha.
    '''
    for i in range(len(matriz)):  # número de linhas
        for j in range(len(matriz[i])):
            print(matriz[i][j],end ='')
            if not j == len(matriz[i]) - 1:
                print(' ',end='')
        print()
