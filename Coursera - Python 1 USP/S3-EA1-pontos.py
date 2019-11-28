# Semana 03 - Exercício Adicional 1 - pontos.py

# Calcule a distância entre dois pontos num plano cartesiano, ou seja, com coordenadas (x,y).
# Se a distância for maior ou igual a 10, imprima 'longe' na saída.
# Caso o contrário, quando a distância for menor que 10, imprima 'perto'.

import math;
# Input do usuário
x1 = float(input('Informe a coordenada x do ponto1: '));
y1 = float(input('Informe a coordenada y do ponto1: '));
x2 = float(input('Informe a coordenada x do ponto2: '));
y2 = float(input('Informe a coordenada y do ponto2: '));
# A menor distância entre dois pontos é uma reta.
# d(x,y) = sqrt[(x1 - x2)^2 + (y1 - y2)^2]
dist_xy = math.sqrt((x1-x2)**2 + (y1-y2)**2);
if dist_xy >= 10:
    print('longe');
else:
    print('perto');
