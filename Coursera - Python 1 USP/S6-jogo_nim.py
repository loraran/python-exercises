# Semana 06 - Exercício - jogo_nim.py

# Você deverá escrever um programa que permita a uma "vítima" jogar o NIM contra o computador.
# O computador, é claro, deverá seguir a estratégia vencedora descrita a seguir.

# Sejam 'n' o número de peças inicial e 'm' o número máximo de peças que é possível retirar em uma rodada.
# Para garantir que o computador ganhe sempre, é preciso considerar dois cenários possíveis para o início do jogo:
#  - Se 'n' é múltiplo de (m+1), o computador deve ser "generoso" e convidar o jogador a iniciar a partida com a frase "Você começa".
#  - Caso contrário, o computador toma a inciativa de começar o jogo.

# Uma vez iniciado o jogo, a estratégia do computador para ganhar consiste em deixar sempre um número de peças que seja múltiplo de (m+1) ao jogador.
# Caso isso não seja possível, deverá tirar o número máximo de peças possíveis.

def computador_escolhe_jogada(n,m): # REVISAR
    if n > m:
        i = 1
        n_mult = n
        while not n_mult % (m+1) == 0 and n_mult > 1:
            n_mult = n - i
            i = i + 1
        if n_mult == 0:
            m_comp = m
        else:
            m_comp = n - n_mult
    elif n == m:
        m_comp = m
    else:
        m_comp = n

    if m_comp == 1: # declara peças retiradas
        print('O computador tirou uma peça.')
    else:
        print('O computador tirou',m_comp,'peças.')

    m_used = m_comp
    return m_used # retorna o número de peças retiradas

def usuario_escolhe_jogada(n,m):
    m_user = int(input('Quantas peças você vai tirar? '))
    while m_user > m or m_user <= 0:
        print('\nOops! Jogada inválida! Tente de novo.\n')
        m_user = int(input('Quantas peças você vai tirar? '))

    if m_user == 1: # declara peças retiradas
        print('\nVocê tirou uma peça.')
    else:
        print('\nVocê tirou',m_user,'peças.')

    m_used = m_user
    return m_used # retorna o número de peças retiradas

def partida():
    n = int(input('\nQuantas peças? n = '))
    m = int(input('Limite de peças por jogada? m = '))
    
    while n < 0 or m < 0:# or m > n:
        n = int(input('\nQuantas peças? n = '))
        m = int(input('Limite de peças por jogada? m = '))
        
    if n % (m+1) == 0: # condição para jogada inicial
        print('\nVocê começa!')
        vez = 0
        m_used = usuario_escolhe_jogada(n,m)
    else:
        print('\nComputador começa!')
        vez = 1
        m_used = computador_escolhe_jogada(n,m)

    n_rest = n - m_used # n_rest após a primeira jogada

    while n_rest > 0: # enquanto o jogo não acabou (n > 0)...
        if n_rest == 1: # declara quantas peças ainda existem no tabuleiro.
            print('Agora resta apenas uma peça no tabuleiro.\n')
        elif n_rest > 1:
            print('Agora restam',n_rest,'peças no tabuleiro.\n')

        n = n_rest # n assume novo valor (peças restantes)

        if vez == 0: # se o usuário jogou, a próxima vez é do computador
            vez = 1
            m_used = computador_escolhe_jogada(n,m)
            n_rest = n - m_used
        elif vez == 1: # se o computador jogou, a próxima vez é do usuário
            vez = 0
            m_used = usuario_escolhe_jogada(n,m)
            n_rest = n - m_used

    if vez == 0:
        print('Fim do jogo! Você ganhou!')
    elif vez == 1:
        print('Fim do jogo! O computador ganhou!')

    return vez

def campeonato():
    wins_user = 0
    wins_comp = 0
    
    print('\n**** Rodada 1 ****')
    vez = partida()
    if vez == 0: # Se o jogo acabou na vez do usuário...
        wins_user = wins_user + 1
    elif vez == 1: # Se o jogo acabou na vez do computador...
        wins_comp = wins_comp + 1
        
    print('\n**** Rodada 2 ****')
    vez = partida()
    if vez == 0: # Se o jogo acabou na vez do usuário...
        wins_user = wins_user + 1
    elif vez == 1: # Se o jogo acabou na vez do computador...
        wins_comp = wins_comp + 1
    
    print('\n**** Rodada 3 ****')
    vez = partida()
    if vez == 0: # Se o jogo acabou na vez do usuário...
        wins_user = wins_user + 1
    elif vez == 1: # Se o jogo acabou na vez do computador...
        wins_comp = wins_comp + 1

    print('\n**** Final do campeonato! ****\n')
    print('Placar: Você',wins_user,'X',wins_comp,'Computador')

    

print('Bem-vindo(a) ao Jogo do NIM! Escolha:\n')
print('1 - para jogar uma partida isolada, ou \n2 - para jogar um campeonato.')
mode = input('Modalidade: ')
while not (mode == '1' or mode == '2'):
    mode = input('Modalidade: ')
if mode == '1':
    print('Você escolheu uma partida!')
    partida()
else:
    print('Você escolheu um campeonato!')
    campeonato()
