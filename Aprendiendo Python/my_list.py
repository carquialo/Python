
# Para añadir un sólo elemento a la lista.
my_list = []
print(my_list)
my_list.append(1)         
print(my_list)


# Para añadir varios elementos.
my_list.extend([2,3,4])   
print(my_list)


# El método pop borra por índice y retorna el elemento, también si invocas el método pop sin argumentos pop() elimina el último elemento.
my_list = [1,2,3,4,5,5]
my_list.pop(5)             
print(my_list)


# Si quisiera eliminar el elemento sin que se retorne, usamos del. 
my_list = [1,2,3,4,5,6]
del my_list[2]
print(my_list)


# Para borrar todo los elementos, usaríamos clear. 
my_list = [1,2,3,4,5,6]
my_list.clear()
print(my_list)

# Para eliminar un elemento que se conoce, usamos el método remove y si no se pone argumento remove() elimina el primer elemento.
my_list = [1,2,3,4,5,6]
my_list.remove(4)
print(my_list)


# Para cambiar el índice usaremos lo siguiente: 
my_list = [1,2,3,4,5,6]
my_list[2] = "Rojo"
print(my_list)

# Para cambiar el orden reverse.
my_list = [1,2,3,4,5,6]
my_list.reverse()
print(my_list)

# Para ordenarlo sort, en caso de cadena de texto se haría de forma alfabética.
my_list = [6,5,4,3,2,1]
my_list.sort()
print(my_list)

# Para hacer sublistas: 
my_list = [6,5,4,3,2,1]
print(my_list[0:2])