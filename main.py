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
            newCaja=(x,z,y)
            if newCaja not in cajas2:     
                cajas2.append(newCaja)
            newCaja=(y,z,x)
            if newCaja not in cajas2:     
                cajas2.append(newCaja)
            newCaja=(y,x,z)
            if newCaja not in cajas2:     
                cajas2.append(newCaja)
            newCaja=(z,x,y)
            if newCaja not in cajas2:     
                cajas2.append(newCaja)
            newCaja=(z,y,x)
            if newCaja not in cajas2:     
                cajas2.append(newCaja)
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

def programacionDinamica():
    cajas=cajasRotadas(obtenerCajas())
    for i in cajas:
        print(max_altura(i))

def stack(caja_1, caja_2):
    validacion = caja_1[0] < caja_2[0] and caja_1[1] < caja_2[1]
    return validacion

def max_altura(rotaciones):

    rotaciones.sort(key = lambda caja: (caja[0],caja[1]))
    cantidad = len(rotaciones)
    Altura = [0]*cantidad

    for i in range(cantidad):
        Altura[i] = rotaciones[i][2]

        for j in range(i):
            if stack(rotaciones[j],rotaciones[i]):
                Altura[i] = max(Altura[i], Altura[j] + rotaciones[i][2])
    
    return max(Altura)

# Main

print("\nFuerza Bruta")
print("-------------------------------------------------------------")
recursionFuerzaBruta()
print("-------------------------------------------------------------")
print("\nProgrmacion Diamica")
print("-------------------------------------------------------------")
programacionDinamica()
print("-------------------------------------------------------------")
