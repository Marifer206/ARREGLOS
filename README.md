# :star: ARREGLOS :star:
## Un dia nuevo, un nuevo reto
REALIZANDO NUESTRO RETO #10

## 1.EJERCICIOS DE CLASE
### :round_pushpin: EJERCICIO #1 
+   Revisar la diferencia entre sort() y sorted().

La diferencia entre `sort` y `sorted` es:
### :feet: Sort
`sort` es un método que se utiliza para ordenar una lista en su lugar, es decir, modifica la lista original. No devuelve ningún valor, simplemente ordena la lista actual.
Ejemplo:
``` ruby
lista = [3, 1, 2]
lista.sort()
print(lista)  # Imprime: [1, 2, 3]
```
### :feet: Sorted
`sorted` es una función que toma una secuencia iterable (como una lista) y devuelve una nueva lista ordenada con los elementos de la secuencia. No modifica la secuencia original.
Ejemplo:
``` ruby
lista = [3, 1, 2]
lista_ordenada = sorted(lista)
print(lista_ordenada)  # Imprime: [1, 2, 3]
print(lista)  # Imprime: [3, 1, 2] (la lista original no ha sido modificada)
```
+ En resumen, `sort` ordena la lista original, mientras que `sorted` devuelve una nueva lista ordenada sin modificar la original.

## PUNTOS DEL RETO
### :round_pushpin: PUNTO #1 
+ Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.

#### :space_invader: CODIGO DEL PROGRAMA
```ruby
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
```
:checkered_flag: **EL PROGRAMA EJECUTADO SE VE ASI**

<div align='center'>
<figure> <img src=" alt="" width="700" height="auto"/></br>
<figcaption><b> </b></figcaption></figure>
</div>


### :round_pushpin: PUNTO #2
+ Desarrollar un algoritmo que calcule el producto punto de dos arreglos de números enteros (reales) de igual tamaño.

#### :space_invader: CODIGO DEL PROGRAMA
```ruby
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

```
:checkered_flag: **EL PROGRAMA EJECUTADO SE VE ASI**

<div align='center'>
<figure> <img src=" alt="" width="700" height="auto"/></br>
<figcaption><b> </b></figcaption></figure>
</div>

### :round_pushpin: PUNTO #3 
+ Hacer un algoritmo que deje al final de un arreglo de números todos los ceros que aparezcan en dicho arreglo.

#### :space_invader: CODIGO DEL PROGRAMA
```ruby
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

```
:checkered_flag: **EL PROGRAMA EJECUTADO SE VE ASI**

<div align='center'>
<figure> <img src=" alt="" width="700" height="auto"/></br>
<figcaption><b> </b></figcaption></figure>
</div>

### :round_pushpin: PUNTO #4 
+  Revisar que son los algoritmos de sorting, entender bubble-sort (enlace a implementación).

#### :space_invader: CODIGO DEL PROGRAMA
```ruby

```
:checkered_flag: **EL PROGRAMA EJECUTADO SE VE ASI**

<div align='center'>
<figure> <img src=" alt="" width="700" height="auto"/></br>
<figcaption><b> </b></figcaption></figure>
</div>



## :sparkles: Esto es todo hoy amigos :blush:, espero poder haberlos ayudado he inspirado para encontar nuevas solociones para nuevos retos :sparkles: 
