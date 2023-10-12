def obtenerCajas():
    archivo=open('input.dat', 'r')
    count=0
    pilas=[]
    for lineas in archivo:
        lineas=lineas.strip().split(" ")
        if count==0:
            cajas=[]
            n=int(lineas[0])
            count+=1
        else:
            x,y,z=lineas
            x=int(x)
            y=int(y)
            z=int(z)
            cajas.append((x,y,z))
            count+=1
            if count>n:
                count=0
                pilas.append(cajas)
    return pilas

def cajasRotadas(Tcajas):
    Tpilas=[]
    for pilas in Tcajas:
        cajas2=[]
        for cajas in pilas:
            x,y,z=cajas
            if (x,y,z) not in cajas2:
                cajas2.append((x,y,z))
            if (y,z,x) not in cajas2:     
                cajas2.append((y,z,x))
            if (z,x,y) not in cajas2:
                cajas2.append((z,x,y))
        Tpilas.append(cajas2)
    return Tpilas

# Fuerza bruta

def recursion(lista, px, py):
    maxTamano = 0
    for i in range(len(lista)):
        x, y, z = lista[i]
        if x > px and y > py:
            restantes = lista[:i] + lista[i+1:]
            tSubpila = z + recursion(restantes, x, y)
            maxTamano = max(maxTamano, tSubpila)
    return maxTamano

def pilaMasAlta(lista):
    return recursion(lista, 0, 0)

def recursionFuerzaBruta():
    cajas=cajasRotadas(obtenerCajas())
    for i in cajas:
        print(pilaMasAlta(i))

# Progrmacion dinamica

def can_stack(caja_1, caja_2):
    validacion = caja_1[0] < caja_2[0] and caja_1[1] < caja_2[1]
    return validacion

def max_altura(rotaciones):

    rotaciones.sort(key = lambda caja: (caja[0],caja[1]))
    cantidad = len(rotaciones)
    Altura = [0]*cantidad

    for in range(cantidad):


# Main


recursionFuerzaBruta()
