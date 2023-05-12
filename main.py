from procesos.operaciones import *
def funcion2():
    v1 = "Hola"
    v2 = "POO"
    v4 = True
    v3 = v1+" "+v2+str(v4)
    print(v3)
def funcion3():
    a = float(input("Numero 1:"))
    b = float(input("Numero 2:"))
    r = suma(a,b)
    print("Total:"+str(r))

def funcion4():
    edad = int(input("Edad:"))
    res = getEdad(edad)
    print(res)

def funcion5():
    materia = input("Materia:")
    nombre = input("Estudiante:")
    n1 = float(input("Nota 1:"))
    n2 = float(input("Nota 2:"))
    n3 = float(input("Nota 3:"))
    r = promedio(n1,n2,n3)
    print("Promedio es:"+str(r))
    msg = getMessage(r)
    print(msg)

def funcion6():
    c = 1
    ac =0
    ci =0
    while c<10:
        c= c+1
        if c%2!=0:
          print(c)
          ac = ac + c
          ci = ci + 1

    print("Total :"+str(ac))
    print("Total impares :"+str(ci))

    cp =0
    ac = 0
    for c in range(1,11):
        if c%2==0:
            print(c)
            cp = cp +1
            ac = ac + c
    print("Total acumulado:"+str(ac))
    print("Total de pares es:"+str(cp))

def funcion7():
    datos =("2G",6,100,True,100.56,"POO")
    print(len(datos))
    datos=(10,88)
    for i in range(len(datos)):
        print(datos[i])

    lista = []
    lista.append("POO")
    lista.append(100)
    lista.append(True)
    lista.append("2G")
    print(lista)
    lista[2]= False
    print(lista)
    del lista[1]
    print(lista)
    lista.clear()
    print("Tam ",len(lista))
    for i in range(len(lista)):
        print(lista[i])

    dic = {
        "2G" : 200,
        12 : False,
        True : [5,5,6],
        (6,7,8): 300
    }
    print(dic["2G"])
    dic[(6,7,8)]=1000
    del dic[12]
    dic["ISTG"]=450
    print(dic)

def funcion1():
    print("Hola mundo")
    print("2G")

funcion4()



