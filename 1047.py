hi, mi, hf, mf = input.split(" ")

hi = int(hi)
mi = int(mi)
hf = int(hf)
mf = int(mf)

duracao_horas = hf - hi
duracao_minutos = mf - mi

print("O JOGO DUROU %d HORA(S) E %d MINUTOS(S)" %(duracao_horas,duracao_minutos))