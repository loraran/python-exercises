BOMBA = -1
A = [[0, -1, 0, 0], [-1, 0, -1, 0], [-1, 0, -1, -1], [-1, -1, -1, 0]]

def livre_bomba(A):
    ''' (matriz) -> list
    A função lê uma matriz A de 0's (posições livres) e -1's (bombas),
    computa e imprime a quantidade de bombas ao redor de cada posição livre (0).
    '''

    print('Posição Livre\tBombas')
    
    for lin in range(int(dim[0])):  # varrendo cada elemento de A
        for col in range(int(dim[-1])):
            if A[lin][col] != BOMBA:  # se temos uma posição livre...
                num_bombas = conta_bomba(A,lin,col)
                print(' (',lin,',',col,')\t ',num_bombas)

livre_bomba(A)
