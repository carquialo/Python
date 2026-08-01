### Tuples ###


## Sintaxis.
my_tuple = ()
my_tuple = tuple()


## Creación y longitud de una tupla. 
fruits =("plátano","manzanas","pera","melón")
print(type(fruits))

print(len(fruits))  # Número de elemento.


## Obtener elementos de la tupla.

# Índice positivo.
fruits =("plátano","manzanas","pera","melón")
first_fruits = fruits[0]
print(first_fruits)
second_fruits = fruits[1]
print(second_fruits)

# Índice negativo.
fruits =("plátano","manzanas","pera","melón")
first_fruits = fruits[-4]
print(first_fruits)
second_fruits = fruits[-3]
print(second_fruits)


## Slicing de tuplas.

# Rango de índice positivo.
fruits =("plátano","manzanas","pera","melón")
all_fruits = fruits [0:4]
print(all_fruits)
banana_apple_pear = fruits [0:3]    # Se excluye el último índice.
print(banana_apple_pear)

# Rango de índice negativo.
fruits =("plátano","manzanas","pera","melón")
all_fruits = fruits [-4:]   # Todos los elementos. 
print(all_fruits)
banana_apple_pear = fruits [-4:-1]  # Se excluye el índice 3.
print(banana_apple_pear)


## Convertir tuplas en listas y viceversa.
fruits =("plátano","manzanas","pera","melón")
fruits = list(fruits)   # Cambiamos a lista.
print(type(fruits))
fruits[0] = "limón" # Cambiamos en el índice 0 por limón.
print(fruits)
fruits = tuple(fruits)  # Lo volvemos a convertir en tupla.
print(type(fruits))


## Comprobar si un elemento está en la tupla.
tpl = ("item1", "item2", "item3","item4")
"item2" in tpl  # True


## Unir tupla.
tpl = ("item1", "item2", "item3","item4")
tp2 = ("item5", "item6","item7", "item8")
tp3 = tpl + tp2
print(tp3)


## Eliminar tupla.
tpl = ("item1", "item2", "item3","item4")
del tpl # Se puede eliminar por completo la tupla pero no individualmente.