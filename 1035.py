a = str.split(raw_input())
A,B,C,D = int(a[0]),int(a[1]),int(a[2]),int(a[3])
if B > C and D > A and C + D > A + B and C > 0 and D > 0 and A%2==0:
    print ("Valores aceitos")
else:
    print ("Valores nao aceitos")
