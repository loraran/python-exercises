# Semana 05 - Exercício Adicional 2 - maximo_3.py

# Escreva a função 'maximo' que receba 3 valores inteiros como parâmetros e devolva o maior dentre eles.

def maximo(num1,num2,num3):
    if (num1 >= num2) and (num1 >= num3):
        return num1
    elif (num2 >= num1) and (num2 >= num3):
        return num2
    elif (num3 >= num1) and (num3 >= num2):
        return num3
