distancia = int(input())
x = 60
y = 90

vel_relativa = y-x
tempo = distancia / vel_relativa
tempo = tempo * 60

print("%d minutos" %tempo)