# Definir el algoritmo bubble_sort 
def bubble_sort(lista):
    # Inicializar n con la cantidad de elementos de la lista
    n = len(lista)

    # Pasar por todos los elementos de la lista excepto el último
    for i in range(n - 1):
        # Pasar por todos los elementos restantes en cada iteración
        # El rango disminuye en cada iteración para evitar comparaciones innecesarias
        for j in range(n - i - 1):
            # Comparar dos elementos adyacentes
            if lista[j] > lista[j + 1]:
                # Intercambiar los elementos si están en el orden incorrecto
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# Pedir al usuario que ingrese los números del arreglo y convertir la n en una lista de números enteros
n = input("Ingrese los números separados por espacios que quiera ordenar: ")
numeros = [int(i) for i in n.split()]
# Imprimir la lista original
print("Lista original:"+ str(numeros))
# Llamar a la función bubble_sort para ordenar la lista
bubble_sort(numeros)
# Imprimir la lista ordenada
print("Lista ordenada:" + str(numeros))
