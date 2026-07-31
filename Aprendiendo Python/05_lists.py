### Lists ###

# Podemos usar la función incorporada list().
my_list = list()
print(my_list)

# O también usando corchetes []
my_list = []
print(my_list)



# Lista de frutas, ejemplo.
fruits =["plátano","manzanas","peras","melón"]
print("Frutas : ", fruits)
print(len(fruits))



## Acceder por índice positivo.
fruits =["plátano","manzanas","peras","melón"]
first_fruit = fruits [0]
print("Primera fruta : ", first_fruit)
second_fruit = fruits[1]
print("Segunda fruta : ", second_fruit)
last_fruit = fruits[3]
print("Última fruta : ", last_fruit)



## Acceder por índice negativo.
fruits =["plátano","manzanas","peras","melón"]
first_fruit = fruits [-4]
print("Primera fruta : ", first_fruit)
last_fruit = fruits[-1]
print("Última fruta : ", last_fruit)



## Desempaquetado de listas.
lst = ["item1","item2","item3","item4","item5"]
first_item,second_item,third_item, *rest = lst
print(first_item)
print(second_item)
print(third_item)
print(*rest)    # El resto de item. 



## Slicing de listas.

# Índice positivo.
fruits =["plátano","manzanas","pera","melón"]
all_fruits = fruits[0:4]
print(all_fruits)   # Devuelve todas las frutas. 
all_fruits = fruits[0:] # Lo mismo que arriba.
print(all_fruits)
apple_and_melon = fruits[1:3]
print(apple_and_melon)  # Se excluye el índice último. 
apple_pear_melon = fruits[1:]
print(apple_pear_melon)  # Desde manzana y los siguientes. 
banana_and_pear = fruits[::2]   # Paso cada 2 elementos. plátano y pera.
print(banana_and_pear)

# Índice negativos.
fruits =["plátano","manzanas","pera","melón"]
all_fruits = fruits[-4:]    # Devuelve todas las frutas.
print(all_fruits)
apple_and_pear = fruits[-3:-1]
print(apple_and_pear)
apple_pear_melon = fruits[-3:]  # Devuelve desde el elemento -3 hasta al final. 
print(apple_pear_melon)
reverse_fruits = fruits[::-1]   # Invierte la lista.
print(reverse_fruits)



## Modificar listas.
fruits =["plátano","manzanas","pera","melón"]
fruits[0] = "limón" # Desde la variable fruits del índice 0 cambiamos por limón. 
print(fruits)
fruits[1] = "aguacate"
print(fruits)



## Buscar elementos.
fruits =["plátano","manzanas","pera","melón"]
doest_exist = "pera" in fruits  # Usar el operador in para saber si existe tal elemento en la lista.
print(doest_exist)  # True
doest_exist = "limón" in fruits
print(doest_exist)   # False



### Agregar elementos.

## Añadir un elemento. 
fruits =["plátano","manzanas","pera","melón"]
fruits.append("limón")  # Se añade UN SÓLO elemento a lo último de la lista. 
print(fruits)



## Añadir más elementos.
fruits =["plátano","manzanas","pera","melón"]
fruits.extend(["limón","aguacate"]) # Usar los corchetes [].
print(fruits)



## Insertar elementos. 
fruits =["plátano","manzanas","pera","melón"]
fruits.insert(2, "limón")   # Inserta limón en el índice 2. 
print(fruits)



## Eliminar elementos.
fruits =["plátano","manzanas","pera","melón"]
fruits.remove("plátano")    # Usamos remove() para eliminar el elemento específico.
print(fruits)



## Eliminar con pop()
fruits =["plátano","manzanas","pera","melón"]
fruits.pop()    # Elimina el último elemento si no se indica.
print(fruits)

fruits.pop(0)
print(fruits)



## Eliminar con del.
# del para eliminar un índice específico, también puede eliminar un rango de índices o eliminar por completo la lista.
fruits =["plátano","manzanas","pera","melón"]
del fruits[0]
print(fruits)
del fruits[1:2]
print(fruits)
del fruits
print(fruits) # Da un NameError.



## Vaciar listas. clear()
fruits =["plátano","manzanas","pera","melón"]
fruits.clear()
print(fruits)



## Copiar listas. copy()
fruits =["plátano","manzanas","pera","melón"]
fruits_copy = fruits.copy()
print(fruits_copy)



## Contar elementos. count() para devolver el número de veces que se repite un elemento.
fruits =["plátano","manzanas","pera","melón","pera"]
print(fruits.count("pera"))



## Encontrar el índice de un elemento. index().
fruits =["plátano","manzanas","pera","melón","pera"]
print(fruits.index("plátano"))



## Invertir listas. reverse()
fruits =["plátano","manzanas","pera","melón","pera"]
fruits.reverse()
print(fruits)



## Ordenar listas. sort()
fruits =["plátano","manzanas","pera","melón","pera"]
fruits.sort()
print(fruits)   # Ordena alfabéticamente. 
