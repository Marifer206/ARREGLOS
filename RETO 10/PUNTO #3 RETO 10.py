# Definir una función para mover los ceros al final de un arreglo de números
def mover_ceros(arreglo):
    # Creamos una lista para almacenar los ceros
    ceros = []
    # Inicializar variable i en 0
    i = 0
    # Se recorre la lista y se va agregando las caros que se encuentren 
    while i < len(arreglo): #  Mientras que i sea menor a la cantidad de numeros de la lista o arreglo  
        if arreglo[i] == 0: # Se evalua cada elemento del arreglo
            ceros.append(arreglo.pop(i)) # si es igual a cero se agrega a la lista ceros y se elimina de la original 
        else: # si no se le suma una unidad a i para ir llevando un control de iteraciones 
            i += 1
    # Se agrega los ceros al final del arreglo y se devuelve 
    arreglo.extend(ceros)
    return arreglo

if __name__ == "__main__":
    # Pedir al usuario que ingrese los números del arreglo y convertir la n en una lista de números enteros
    n = input("Ingrese los números separados por espacios: ")
    arreglo = [int(i) for i in n.split()]
    #  Imprimir el arreglo original
    print("Arreglo original:" + str(arreglo))
    # Se llama a la funcion y toma como argumento la lista previamente dada por el usuario 
    arreglo = mover_ceros(arreglo)
    #  Imprimir el arreglo con los ceros al final
    print("Arreglo con ceros al final:" + str (arreglo))
