# Exercício Resolvido (minmax.py)
# Dicas:
#  - Quebre seu problema em problemas menores!
#  - Refatoração: melhore a legibilidade do seu código!
#  - Código duplicado deve ser evitado ao máximo!

def minmax(temps):
    print('A menor temperatura do mês foi',mintemp(temps),'°C.')
    print('A maior temperatura do mês foi',maxtemp(temps),'°C.')

def mintemp(temps):
    mintemp = temps[0]  # valor mínimo atual
    i = 1  # começa em 1 pois o valor inicial de mintemp corresponde a i = 0
    while i < len(temps):
        if temps[i] < mintemp:
            mintemp = temps[i]
        i = i + 1
    return mintemp

def maxtemp(temps):
    maxtemp = temps[0]  # vamor máximo atual
    i = 1  # começa em 1 pois o valor inicial de maxtemp corresponde a i = 0
    while i < len(temps):
        if temps[i] > maxtemp:
            maxtemp = temps[i]
        i = i + 1
    return maxtemp

def test_model(temp,expected_minvalue,expected_maxvalue):
    if mintemp(temp) != expected_minvalue or maxtemp(temp) != expected_maxvalue:
        print('Valor errado para array',temp)
        print('Valor mínimo esperado:',expected_minvalue,'. Valor calculado:',mintemp(temp))
        print('Valor máximo esperado:',expected_maxvalue,'. Valor calculado:',maxtemp(temp))

def test_minmax():
    print('Iniciando testes...')
    
    test_model([0],0,0)
    test_model([0,0,0,0,0,0],0,0)
    test_model([1,2,3,4,5,6,7,8,9,10],1,10)
    test_model([-15,-12,20,105,-2],-15,105)
        
    print('Finalizando testes...')
