### Sets (Conjuntos) ###
# En python como en matemáticas un conjunto es una colección desordenada y no indexada de elementos distintos. 


## Crear conjuntos. 
st = set()
print(type(st))
st = {"item1","item2","item3","item4"}   # Se crea con llaves {}.
print(st)   # Se imprime de forma desordenada. 
my_other_st = st[0]    # NameError = No tiene orden, ni índice.
print(my_other_st)

## Obtener la longitud del conjunto.
st = {"item1","item2","item3","item4"}
len(st)


## Acceder a elementos del conjunto.
# Usamos bucles para recorrer los elementos.
## Comprobar elementos. Usamos in.
st = {"item1","item2","item3","item4"}
"item2" in st   # True

fruits = {"plátano", "naranja", "mango", "limón"}
print("mango" in fruits )   # True
"mango" in fruits


## Añadir elementos al conjunto.
# .add para agregar un solo elemento.
st = {"item1","item2","item3","item4"}
st.add("item5")
print(st)

# .update para agregar más elementos.
st = {"item1","item2","item3","item4"}
st.update(["item5","item6","item7"])    # FÍJATE EN el paréntesis y corchetes.
print(st)


## Eliminar elementos del conjunto.
# remove() para eliminar un elemento de un set. Sale error si el elemento no existe. Con discard() se borra indicando el elemento y si no existe no sale error.
st = {"item1","item2","item3","item4"}
st.remove("item5")   # KeyError. Porque no existe ese elemento.
print(st)
st.discard("item5") # No ocurre nada.
print(st)

fruits = {"plátano", "naranja", "mango", "limón"}
fruits.pop()    # Elimina un elemento y devuelve uno aleatorio.
print(fruits)


## Vaciar el conjunto.
fruits = {"plátano","naranja","mango","limón"}
fruits.clear()
print(fruits)


## Eliminar conjunto.
# Para eliminar el conjunto por completo, podemos usar el operador del.
fruits = {"plátano","naranja","mango","limón"}
del fruits


## Convertir lista a conjunto.
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)  # {'item2', 'item4', 'item1', 'item3'} - El orden es aleatorio y elimina duplicados. 
print(st)


## Unir conjuntos.
# Podemos usar los métodos union() o update() para combinar dos conjuntos.
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)
print(st3)

# Update Este método inserta los elementos de un conjunto en el conjunto dado.
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2) # Los elementos de st2 se añaden a st1.
print(st2)


## Encontrar intersección.
# La intersección devuelve un conjunto con los elementos que están presentes en ambos conjuntos.
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2) # {'item3', 'item2'}
print(st2)

