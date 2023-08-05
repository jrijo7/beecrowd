N = int(input())

horas = N//360
minutos = (N%360)//60
segundos = (N%360)%60

print("{}:{}:{}".format(horas, minutos, segundos))