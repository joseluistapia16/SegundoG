'''
v1 = "Hola"
v2 = "POO"
v4 = True
v3 = v1+" "+v2+str(v4)
print(v3)

x = float(input("Numero 1:"))
y = float(input("Numero 2:"))
r =(x+y)
print("Total:"+str(r))

edad = int(input("Edad:"))
if edad<0:
    print("Valor invalido")
else:
    if edad>=0 and edad<11:
        print("Infante")
    if edad>10 and edad<18:
        print("Adolescente")
    if edad>17 and edad<26:
        print("Joven")
    if edad > 25 and edad<65:
        print("Adulto")
    if edad>64:
        print("Adulto mayor")

materia = input("Materia:")
nombre = input("Estudiante:")
n1 = float(input("Nota 1:"))
n2 = float(input("Nota 2:"))
n3 = float(input("Nota 3:"))
r = (n1 + n2 + n3) / 3
if r >10 or r<0:
    print("Valor invalido!")
else:
    print("Promedio:" + str(r))
    if r >= 7 and r<=10:
        print("Aprobado")
    if r<= 6 and r>=0:
        print("Reprobado")
'''

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



