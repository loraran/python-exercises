BOMBA = -1

def gera_campo(num_lines,num_columns):
    '''(int,int,float) -> matriz (lista de listas)
    A função matrix() cria e retorna uma matriz com um dado número de
    linhas e colunas, com posições 0 e -1 escolhidas aleatoriamente.
    '''
    matrix = []  # lista vazia
    for i in range(num_lines):
        line = []  # lista vazia
        for j in range(num_columns):  # para cada linha i, adicionamos j colunas
            line.append(random.choices([BOMBA,0],[7,10],k=1)[0])            
        matrix.append(line)  # adiciona cada linha à matriz inicial
    return matrix

num_lines = 5
num_columns = 5
gera_campo(num_lines,num_columns)
