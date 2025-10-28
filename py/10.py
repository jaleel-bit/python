#Ejercicio 10

#Entrada
n = int(input("n: "))
v = [0]*n
for i in range(n):
    x = int(input())
    #x = list(map(int,input().split()))
    v[i] = x

c = set(v[i])

print("La cantidad de numeros distintos es",len(c))
print("Los numeros distintos son:",*c)
