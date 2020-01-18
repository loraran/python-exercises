# Semana 01 - Exercício 1 - dimensoes_matriz.py

def dimensoes(m):
    '''(matriz) -> dimensoes()
    A função dimensoes() retorna as dimensões (linhas e colunas) de uma matriz
    inserida pelo usuário, no formato 'iXj'.
    Exemplo: dimensoes([[1, 2, 3] , [4, 5, 6]]) = 2X3
    '''

    if type(m) == int:  # há apenas uma linha
        i = 1
    elif type(m) == list:  # há mais de uma linha
        i = len(m)  # número de colunas

    if type(m[0]) == int:  # há apenas uma coluna
        j = 1
    elif type(m[0]) == list:  # há mais de uma coluna
        j = len(m[0])  # número de colunas
    
    print(str(i)+'X'+str(j))
    # return str(i)+'X'+str(j)
