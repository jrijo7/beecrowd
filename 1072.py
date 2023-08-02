contin = 0
contout = 0
N = int(input())
for i in range(N):
    a = int(input())
    if (a >= 10 and a<=20):
        contin+=1
    else:
        contout+=1
print ("{:d} in" .format(contin))
print ("{:d} out" .format(contout))