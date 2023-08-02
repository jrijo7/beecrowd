import math

linha = raw_input().split()
a = int(linha[0])
b = int(linha[1])
c = int(linha[2])

MaiorAB = (a+b+abs(a-b))/2
resultado = (MaiorAB + c + abs((MaiorAB) - c))/2

print(str(int(resultado)) + " eh o maior")