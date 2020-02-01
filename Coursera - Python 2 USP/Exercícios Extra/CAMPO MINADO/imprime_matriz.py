def imprime_matriz(matriz):
    '''(list(list)) -> imprime_matriz()
    A função recebe uma matriz como parâmetro e a imprime linha por linha.
    '''
    print()
    for i in range(len(matriz)):  # número de linhas
        print(' ',end='')
        for j in range(len(matriz[i])):  # número de colunas
            print(matriz[i][j],end ='\t')
            if not j == len(matriz[i]) - 1:
                print(' ',end='')
        print()
