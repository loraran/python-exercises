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
