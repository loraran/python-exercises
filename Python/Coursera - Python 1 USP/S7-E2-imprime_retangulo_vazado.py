# Semana 7 - Exercício 2 - imprime_retangulo_vazado.py

# Escreva um programa que recebe como entrada dois números inteiros
# correspondentes à largura e à altura de um retângulo, respectivamente.
# O programa deve imprimir uma cadeia de caracteres que represente o
# retângulo informado com caracteres '#' na saída.

# Os retângulos devem ser impressos SEM preenchimento, de forma que os
# caracteres que não estiverem na borda do retângulo sejam espaços em branco.

largura = int(input('Indique a largura do retângulo: '))
altura = int(input('Indique a altura do retângulo: '))
while largura < 1 or altura < 1:
    print('Favor inserir números positivos.\n')
    largura = int(input('Indique a largura do retângulo: '))
    altura = int(input('Indique a altura do retângulo: '))

linha = 1
coluna = 1
while linha <= altura:
    if linha == 1 or linha == altura:
        print('#'*largura)
    else:
        while coluna <= largura:
            if coluna == 1 or coluna == largura:
                print('#', end = '')
            else:
                print(' ', end = '')
            coluna = coluna + 1
        print()
    coluna = 1
    linha = linha + 1

