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

cajas=obtenerCajas()
cajas2=cajasRotadas(cajas)

print(cajas2)
