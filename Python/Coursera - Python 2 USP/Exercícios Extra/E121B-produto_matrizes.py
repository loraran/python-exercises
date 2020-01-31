# Introdução à Computação com Python - Parte II - IME/USP
# Funções com Matrizes - Exercício 12.1B

def produto_matrizes(A,B):
    '''(matriz real, matriz real) -> matriz real
    A função lê duas matrizes reais, A e B, e imprime a matriz C que é o
    produto de A por B. Dimensões: A[m X n] * B[n X p] = C[m X p]
    Nota: o número de colunas de A deve ser igual ao número de linhas de B.
    '''

    # pré-condição: num_colunas(A) == num_linhas(B)
    if multiplicaveis(A,B) == True:
        
        produto = matrix(int(dimensoes(A)[0]),int(dimensoes(B)[-1]),0)
        
        for i in range(len(A)):  # i/j: para cada elemento da matriz produto...
            for j in range(len(B[0])):
                #print()
                #print(' Estamos na linha i =',i,', coluna j =',j,'...')
                step = 0
                calc = 0
                while step < len(A[0]):
                    #print('calc =',calc,'+ ( A [',i,'] [',step,'] * B [',step,'] [',j,'] )')
                    calc = calc + (A[i][step]*B[step][j])
                    #print('calc =',calc)
                    step = step + 1
                produto[i][j] = calc
                
        print('O produto das matrizes é:')
        imprime_matriz(produto)

#---------------------------------------------------------
    
def multiplicaveis(m1,m2):
    ''' (matriz, matriz) -> bool
    A função recebe duas matrizes como parâmetro e devolve True se elas
    forem multiplicáveis (na ordem dada), ou False caso contrário.
    Matrizes são multiplicáveis se num_colunas(m1) = num_linhas(m2).
    '''    
    dim_m1 = dimensoes(m1)  # formato iXj
    dim_m2 = dimensoes(m2)  # formato iXj

    if dim_m1[-1] == dim_m2[0]: # dim[-1] = j ; dim[0] = i
        return True
    else:
        print('As matrizes não são multiplicáveis.')
        return False


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
    
    return (str(i)+'X'+str(j))  # formato iXj


def matrix(num_lines,num_columns,value):
    '''(int,int,float) -> matrix (lista de listas)
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

#---------------------------------------------------------

def main():
    A = [[1, 2, 1],
         [2, 2, 2],
         [1, 3, 2]]
    B = [[1, 2],
         [2, 2],
         [0, 2]]
##    A = [[2, 3],
##         [1, 0],
##         [4, 5]]
##    B = [[3, 1],
##         [2, 4]]
    produto_matrizes(A,B)

main()
