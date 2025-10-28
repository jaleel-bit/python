
n = list(map(int,input().split()))
x = []

for i in n:
    if i not in x:
        x.append(i)
print("La cantidad de numeros distintos es",len(x))
print("Los numeros distintos son:",*x)
