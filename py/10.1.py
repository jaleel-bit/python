
numeros = []

for i in range(10):
    num = int(input(f"Ingrese el numero{i+1}: "))
    numeros.append(num)
distintos = list(set(numeros))
print(len(distintos))
print(*distintos)
