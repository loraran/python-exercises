# Semana 7 - Exercício 1 - imprime_retangulo_cheio.py

# Escreva um programa que recebe como entrada dois números inteiros
# correspondentes à largura e à altura de um retângulo, respectivamente.
# O programa deve imprimir uma cadeia de caracteres que represente o
# retângulo informado com caracteres '#' na saída.

largura = int(input('Indique a largura do retângulo: '))
altura = int(input('Indique a altura do retângulo: '))
while largura < 1 or altura < 1:
    print('Favor inserir números positivos.\n')
    largura = int(input('Indique a largura do retângulo: '))
    altura = int(input('Indique a altura do retângulo: '))

linha = 1
while linha <= altura:
    print('#'*largura)
    linha = linha + 1
