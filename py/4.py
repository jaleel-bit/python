#Promedio de los elementos de un vector
def LeeVector(A,n):
    for i in range(0,n,1):
        A[i] = int(input("x: "))
        
    
def Promedio(v,n):
    s = 0
    for i in range(0,n,1):
        s  = s + v[i]
    return s/n

#Entrada
n = int(input("n: "))

A = [0] * n

LeeVector(A,n)
p = Promedio(A,n)




#print("El promedio es = ",(s/n))
print("El promedio es =",p)
