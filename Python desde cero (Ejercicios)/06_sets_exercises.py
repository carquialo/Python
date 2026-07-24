# 1. Crea un set con los números del 1 al 5 e imprímelo.
my_set = {1, 2, 3, 4, 5}
print (my_set)

# 2. Añade el número 6 al set {1, 2, 3, 4, 5} e imprímelo.
my_set = {1, 2, 3, 4, 5}
my_set.add(6)
print (my_set)

# 3. Intenta añadir el número 5 al set {1, 2, 3, 4, 5} nuevamente. ¿Qué sucede?
my_set = {1, 2, 3, 4, 5}
my_set.add(5) # El sets no puede duplicar los elementos como las listas o las duplas.

# 4. Verifica si el número 3 está en el set {1, 2, 3, 4, 5} e imprime el resultado.
print (3 in my_set)

# 5. Elimina el número 4 del set {1, 2, 3, 4, 5} e imprime el set resultante.
my_set = {1, 2, 3, 4, 5}
my_set.remove(4)
print (my_set)

# 6. Usa el método clear() para vaciar un set y luego imprime su longitud.
my_set.clear()
print (len(my_set))

# 7. Convierte el set {"manzana", "naranja", "plátano"} en una lista e imprime el primer elemento de la lista.
my_set = {"manzana", "naranja", "plátano"}
my_list = list(my_set)
print(my_list[0])

# 8. Realiza la unión de dos sets: {1, 2, 3} y {4, 5, 6}, e imprime el set resultante.
sets_1 = {1, 2, 3}
sets_2 = {4, 5, 6}
my_set_union = sets_1.union(sets_2)
print(my_set_union)

# 9. Calcula la diferencia entre los sets {1, 2, 3, 4} y {3, 4, 5, 6} e imprime el resultado.
sets_1 = {1, 2, 3, 4}
sets_2 = {3, 4, 5, 6}
sets_difference = sets_1.difference(sets_2)
print (sets_difference)

# 10. Elimina un set llamado my_set usando del y luego intenta imprimirlo para ver el resultado.
del my_set
print (my_set) #name 'my_set' is not defined (No está definido porque nos lo hemos cargado con del).
