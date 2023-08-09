idade_dias = input()
idade_dias = int(idade_dias)

idade_ano = idade_dias//365
idade_dias = idade_dias%365
idade_mes = idade_dias//30
idade_dias = idade_dias%30

print("%d ano(s)" %idade_ano)
print("%d mes(es)" %idade_mes)
print("%d dia(s)" %idade_dias)