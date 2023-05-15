# Pedir al usuario que ingrese los números separados por espacios
l = input("Ingrese los números separados por espacios: ")
# Convertir la l en una lista de números reales y se utiliza el split para dividir los numeros de manera individual
numeros = [float(i) for i in l.split()]
# Calcular la suma de los elementos en la lista numeros
suma = sum(numeros)
# Calcular la cantidad de elementos en la lista numeros
n = len(numeros)
# Calcular el promedio
promedio = suma / n

# Imprimir el resultado
print("El promedio de" + str(numeros) + " es: " + str(promedio))
