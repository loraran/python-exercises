# Semana 8 - Exercício 1 - remove_repetidos.py

# Escreva a função 'remove_repetidos' que recebe como parâmetro uma lista com
# números inteiros, verifica se tal lista possui elementos repetidos e os
# remove. A função deve devolver uma lista correspondente à primeira lista,
# sem elementos repetidos. A lista devolvida deve estar ordenada.

def remove_repetidos(lista):
    sortlista = []
    lista = sorted(lista)
    i = 0
    length = len(lista)
    while i < len(lista)-1:
        if lista[i] != lista[i+1]:
            sortlista.append(lista[i])
        i = i + 1
    sortlista.append(lista[-1])
              
    return sortlista

# Para o futuro: implemente essa função utilizando FOR!
