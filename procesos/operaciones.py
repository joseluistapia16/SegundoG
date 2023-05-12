def getEdad(edad):
    if edad<0:
        return "Valor invalido"
    else:
        if edad>=0 and edad<11:
            return "Infante"
        if edad>10 and edad<18:
            return "Adolescente"
        if edad>17 and edad<26:
            return "Joven"
        if edad > 25 and edad<65:
            return "Adulto"
        if edad>64:
            return "Adulto mayor"
def promedio(n1,n2,n3):
    return   (n1 + n2 + n3) / 3
def getMessage(r):
    if r >10 or r<0:
        return "Valor invalido!"
    else:
        if r >= 7 and r<=10:
            return  "Aprobado"
        if r<= 6 and r>=0:
            return  "Reprobado"

def suma(x,y):
    return (x+y)