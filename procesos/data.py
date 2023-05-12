def getRepeat(lista,valor):
    res = False
    for i in range(len(lista)):
        if valor == lista[i]:
            res= True
            break
    return res

def inputInt(msg):
    num=-1
    while num < 1:
        try:
            num = int(input(msg))
        except:
            print("Valor invalido!")
            num = -1
    return num
