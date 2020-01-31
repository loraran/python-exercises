def matrix(num_lines,num_columns):
    '''(int,int) -> matrix (lista de listas)
    A função matrix() cria e retorna uma matriz com um dado número de
    linhas e colunas, em que cada elemento é digitado pelo usuário.
    '''

    matrix = []  # lista vazia
    for i in range(num_lines):
        line = []  # lista vazia
        for j in range(num_columns):  # para cada linha i, adicionamos j colunas
            value = int(input(' Digite o elemento [' + str(i) + '][' + str(j) +']: '))
            line.append(value)
        matrix.append(line)  # adiciona cada linha à matriz inicial

    for k in range(len(matrix)):
        print(matrix[k])
    
    return matrix

def readmatrix():
    lin = int(input('Digite o número de linhas da matriz: '))
    col = int(input('Digite o número de colunas da matriz: '))

    return matrix(lin,col)
