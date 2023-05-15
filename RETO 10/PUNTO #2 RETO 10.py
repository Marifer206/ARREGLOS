# Definir una función para calcular el producto punto de dos arreglos de números enteros
def producto_punto(arreglo1, arreglo2):
    # Verificamos que los arreglos tengan el mismo tamaño
    if len(arreglo1) != len(arreglo2):
        return None
    # Calculamos el producto punto
    resultado = 0
    for i in range(len(arreglo1)):
        resultado += arreglo1[i] * arreglo2[i]
    return resultado

if __name__ == "__main__":
    # Pedir al usuario que ingrese los números del primer arreglo y convertir la l en una lista de números enteros
    l = input("Ingrese los números separados por espacios del primer arreglo: ")
    arreglo1 = [int(i) for i in l.split()]
    # Pedir al usuario que ingrese los números del segundo arreglo y convertir la n en una lista de números enteros
    n = input("Ingrese los números separados por espacios: ")
    arreglo2 = [int(i) for i in n.split()]
    # Se llama a la funcion y toma como argumentos las listas previamente dadas por el usuario 
    resultado = producto_punto(arreglo1, arreglo2)
    # Se imprime el resultado
    if resultado is None:
        print("Los arreglos no tienen el mismo tamaño.")
    else:
        print("El producto punto de", arreglo1, "y", arreglo2, "es:", resultado)