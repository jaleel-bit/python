
n = int(input("n: "))
x = []
for i in range(n):
    num = int(input(f"Ingrese el numero{i+1}: "))
    x.append(num)
print(x)
c = list(set(x))
print("La cantidad de numeros distintos es",len(c))
print("Los numeros distintos son:",*c)
