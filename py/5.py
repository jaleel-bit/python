#Maximo de los elementos de un vector
def LeeVector(A,n):
    for i in range(0,n,1):
        A[i] = int(input("x: "))
        
    
def Maximo(v,n):
    s = A[0]
    k = 0
    for i in range(1,n,1):
        if A[i] > s:
            s = A[i]
            k = i
    return s,k

#Entrada
n = int(input("n: "))

A = [0] * n

LeeVector(A,n)
m = Maximo(A,n)




#print("El promedio es = ",(s/n))
print("El maximo es =",m)
