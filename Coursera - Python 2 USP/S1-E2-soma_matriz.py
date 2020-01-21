# Semana 01 - Exercício 2 - soma_matriz.py

def soma_matrizes(m1,m2):
    ''' (list,list) -> matriz/bool
    A função recebe duas matrizes, m1 e m2, e devolve uma matriz que
    represente sua soma CASO as matrizes tenham dimensões iguais.
    Caso contrário, a função deve devolver o booleano False.
    '''

    dim1 = dimensoes(m1)  # dim[0] = linhas, dim[1] = colunas
    dim2 = dimensoes(m2)

    if dim1 == dim2:
        soma = matrix(int(dim1[0]),int(dim1[2]),0)  # cria uma matriz nula
        for i in range(len(m1)):
            if type(m1[0]) == int:  # matriz 1x1
                soma[i] = m1[i] + m2[i]
            else:
                for j in range(len(m1[0])):
                    soma[i][j] = m1[i][j] + m2[i][j]                
        #print(soma)
        return soma
    else:
        return False

# Importando dimensoes_matriz.py...
def dimensoes(matriz):
    '''(matriz) -> string
    A função dimensoes() retorna as dimensões (linhas e colunas) de uma matriz
    inserida pelo usuário, no formato 'iXj'.
    Exemplo: dimensoes([[1, 2, 3] , [4, 5, 6]]) = 2X3
    '''

    if type(matriz) == int:  # há apenas uma linha
        i = 1
    elif type(matriz) == list:  # há mais de uma linha
        i = len(matriz)  # número de colunas

    if type(matriz[0]) == int:  # há apenas uma coluna
        j = 1
    elif type(matriz[0]) == list:  # há mais de uma coluna
        j = len(matriz[0])  # número de colunas
    
    return str(i)+'X'+str(j)


# Importando matriz.py...
def matrix(num_lines,num_columns,value):
    '''(int,int,float) -> matriz (lista de listas)
    A função matrix() cria e retorna uma matriz com um dado número de
    linhas e colunas, em que cada elemento é igual a um dado valor.
    '''

    matrix = []  # lista vazia
    for i in range(num_lines):
        line = []  # lista vazia
        for j in range(num_columns):  # para cada linha i, adicionamos j colunas
            line.append(value)            
        matrix.append(line)  # adiciona cada linha à matriz inicial

    return matrix
