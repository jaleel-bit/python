#Ejercicio
def lee(A):
    x = int(input("x: "))
    i = 0
    while x != -1:
        A[i] = x
        x = int(input("x: "))
        i = i + 1
    return i

def Promedio(A,n):
    s = 0
    for i in range(0,n+1,1):
        s  = s + A[i]
    return s/n

def cantidad(A,n,prom):
    cM = 0
    for i in range(0,n+1,1):
        if A[i] >= prom:
            cM = cM + 1
    return cM, n-cM
#Entrada
#x = int(input("x: "))

A = [0] * 20
n = lee(A)
prom = Promedio(A,n)
cM,cm = cantidad(A,n,prom)
print("La cantidad de digitos es:",n)
print("El promedio es:",prom)
print("La cantidad de mayores es:",cM)
print("La cantidad de menores es:",cm)    
    
