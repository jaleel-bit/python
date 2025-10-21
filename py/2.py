def LeeVector(A,n):
    for i in range(0,n,1):
        A[i] = int(input("x: "))
    
n = int(input("Ingrese la cantodad de elementos: "))

A = [0] * n

LeeVector(A,n)

print(A)
