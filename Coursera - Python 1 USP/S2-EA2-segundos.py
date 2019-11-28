# Semana 02 - Exercício Adicional 3 - segundos.py
# Faça um programa em Python que, dada a quantidade de segundos, "quebre" esse valor em dias, horas, minutos e segundos.

fullseg = input('Por favor, entre com o número de segundos que você deseja converter: ');
dias = int(fullseg)//(60*60*24);
horas = (int(fullseg)%(60*60*24))//(60*60);
minutos = ((int(fullseg)%(60*60*24))%(60*60))//60;
segundos = ((int(fullseg)%(60*60*24))%(60*60))%60;

print(dias,'dias,',horas,'horas,',minutos,'minutos e',segundos,'segundos.');
