N = input()
N = float(N)

cem = N//100
N = N%100
cinquenta = N//50
N = N%50
vinte = N//20
N = N%20
dez = N//10
N = N%10
cinco = N//5
N = N%5
dois = N//2
N = N%2
um = N//1
N = N%1
N = N*100
cinquenta_cent = N//50
N = N%50
vinte_cinco_cent = N//25
N = N%25
dez_cent = N//10
N = N%10
cinco_cent = N//5
N = N%5
um_cent = N//1
print("NOTAS:")
print("%d nota(s) de R$ 100.00" %cem)
print("%d nota(s) de R$ 50.00" %cinquenta)
print("%d nota(s) de R$ 20.00" %vinte)
print("%d nota(s) de R$ 10.00" %dez)
print("%d nota(s) de R$ 5.00" %cinco)
print("%d nota(s) de R$ 2.00" %dois)
print("MOEDAS:")
print("%d moeda(s) de R$ 1.00" %um)
print("%d moeda(s) de R$ 0.50" %cinquenta_cent)
print("%d moeda(s) de R$ 0.25" %vinte_cinco_cent)
print("%d moeda(s) de R$ 0.10" %dez_cent)
print("%d moeda(s) de R$ 0.05" %cinco_cent)
print("%d moeda(s) de R$ 0.01" %um_cent)