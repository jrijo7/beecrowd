l1=[]
l2=[]
nl1 = 0
nl2 = 0
for i in range(15):
    a=int(input())
    if (a%2 == 0):
        l1.append(a)
        if (len(l1)%5 == 0):
            for j in range(nl1 * 5, (nl1 + 1) * 5):
                print("par[{:d}] = {:d}".format((j%5), l1[j]))
            nl1 += 1
    else:
        l2.append(a)
        if(len(l2)%5 == 0):
            for j in range(nl2 * 5, (nl2 + 1)*5):
                print("impar[{:d}] = {:d}".format((j%5), l2[j]))
            nl2 += 1
for j in range(nl2 * 5, len(l2)):
    print("impar[{:d}] = {:d}".format((j%5), l2[j]))
for j in range(nl1 * 5, len(l1)):
    print("par[{:d}] = {:d}".format((j%5), l1[j]))