def imprime_matriz_resposta(matriz):
    '''(list(list)) -> imprime_matriz()
    A função recebe o campo minado e o imprime como solução, linha por linha.
    '''
    print()
    print(' SOLUÇÃO:\n')
    print('    \\COL ',end='')
    for j in range(len(matriz[0])):  # para cada coluna da matriz
        print('[',j,'] \t ',end='')
    print('\n  LIN\\')

    for i in range(len(matriz)):  # número de linhas
        print('  [',i,']\t ',end='')
        for j in range(len(matriz[i])):  # número de colunas
            print(' ',matriz[i][j],end='\t')
            if not j == len(matriz[i]) - 1:
                print(' ',end='')
        print('\n')

A = [[0, -1, 0, 0], [-1, 0, -1, 0], [-1, 0, -1, -1], [-1, -1, -1, 0]]
imprime_matriz_resposta(A)
