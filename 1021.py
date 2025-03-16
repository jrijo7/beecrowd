valor_centavos = float(input()) * 100
notas = [10000, 5000, 2000, 1000, 500, 200]
moedas = [100, 50, 25, 10, 5, 1]

print('NOTAS:')
for nota in notas:
    quant_notas = int(valor_centavos//nota)
    print('{} nota(s) de R$ {:.2f}'.format(quant_notas, nota/100))
    valor_centavos = valor_centavos - quant_notas * nota
print('MOEDAS:')
for moeda in moedas:
    quant_moedas = int(valor_centavos//moeda)
    print('{} moeda(s) de R$ {:.2f}'.format(quant_moedas, moeda/100))
    valor_centavos = valor_centavos - quant_moedas * moeda