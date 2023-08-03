x,y,z = input().split(" ")
x = float(x)
y = float(y)
z = float(z)

if ((x>=y) and (y>=z)):
    A = x
    B = y
    C = z
if ((y>=x) and (y>=z)):
    A = y
    B = x
    C = z
if ((z>=x) and (z>=y)):
    A = z
    B = x
    C = y

if (A>=(B+C)):
    print("NAO FORMA TRIANGULO")
elif (A**2 == B**2 + C**2):
    print("TRIANGULO RETANGULO")
elif (A**2 > B**2 + C**2):
    print("TRIANGULO OBTUSANGULO")
elif (A**2 < B**2 + C**2):
    print("TRIANGULO ACUTANGULO")
if ((A == B) and (B == C)):
    print("TRIANGULO EQUILATERO")
elif (B == C) or (A == B):
    print("TRIANGULO ISOSCELES")