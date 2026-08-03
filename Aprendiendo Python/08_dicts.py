### Diccionarios ###
# Un diccionario es un tipo de datos compuestos por pares claves-valor desordenados y mutables (se puede modificar).


## Crear diccionarios.
empty_dict = {}

person = {
    "name":"Carquialo",
    "surname":"Pérez",
    "age":32,
    "country":"Sevilla",
    "is_married":False,
    "skills":["Python","Ciberseguridad","Análisis"]

}
print(person)


## Longitud del diccionario.
person = {
    "name":"Carquialo",
    "surname":"Pérez",
    "age":32,
    "country":"Sevilla",
    "is_married":False,
    "skills":["Python","Ciberseguridad","Análisis"]

}
print(len(person))  # 6.



## Acceder a elementos del diccionario.
# Podemos acceder a lso elementos del diccionario referenciando su clave.
person = {
    "name":"Carquialo",
    "surname":"Pérez",
    "age":32,
    "country":"Sevilla",
    "is_married":False,
    "skills":["Python","Ciberseguridad","Análisis"]

}

print(person["name"])
print(person["age"])

# Con el método get podríamos usarlo para averguar primero si existe esa clave. Con get devuelve None si no existe.
person = {
    "name":"Carquialo",
    "surname":"Pérez",
    "age":32,
    "country":"Sevilla",
    "is_married":False,
    "skills":["Python","Ciberseguridad","Análisis"]

}
print(person.get("name"))   # Carquialo
print(person.get("city"))   # None



## Añadir elementos al diccionario.
person = {
    "name":"Carquialo",
    "surname":"Pérez",
    "age":32,
    "country":"Sevilla",
    "is_married":False,
    "skills":["Python","Ciberseguridad","Análisis"]

}
person["Job"] = "Cibersecurity"
person["skills"].append["Bash"]
print(person)



## Modificar elementos del diccionario.
person = {
    "name":"Carquialo",
    "surname":"Pérez",
    "age":32,
    "country":"Sevilla",
    "is_married":False,
    "skills":["Python","Ciberseguridad","Análisis"]

}
person["age"] = 33
print(person)



## Comprobar claves en el diccionario.
# in para saber si existe una clave en el diccionario.
person = {
    "name":"Carquialo",
    "surname":"Pérez",
    "age":32,
    "country":"Sevilla",
    "is_married":False,
    "skills":["Python","Ciberseguridad","Análisis"]

}
print("name" in person) # True
print("city" in person) # False



## Eliminar pares clave-valor del diccionario.
# pop(key): elimina el elemento con la clave especificada.
# popitem(): elimina el último elemento.
# del: elimina el elemento con la clave especificada.

person = {
    "name":"Carquialo",
    "surname":"Pérez",
    "age":32,
    "country":"Sevilla",
    "is_married":False,
    "skills":["Python","Ciberseguridad","Análisis"]

}
person.pop("name")  # Elimina el elemento name.
person.popitem()    # Elimina el último elemento.
del person["age"]   # Elimina el elemento age.
print(person)



## Convertir diccionario a lista de tuplas.
# El método items() convierte el diccionario en una lista de tuplas.
person = {
    "name":"Carquialo",
    "surname":"Pérez",
    "age":32,
    "country":"Sevilla",
    "is_married":False,
    "skills":["Python","Ciberseguridad","Análisis"]

}
print(person.items())



## Vaciar diccionario.
# Con clear().
person = {
    "name":"Carquialo",
    "surname":"Pérez",
    "age":32,
    "country":"Sevilla",
    "is_married":False,
    "skills":["Python","Ciberseguridad","Análisis"]

}
print(person.clear())   # None



## Eliminar diccionario.
# Si ya no necesitamos el diccionario usamos del
person = {
    "name":"Carquialo",
    "surname":"Pérez",
    "age":32,
    "country":"Sevilla",
    "is_married":False,
    "skills":["Python","Ciberseguridad","Análisis"]

}
del person



## Copiar diccionario.
# Usar copy evita que el diccionario original sea modificado.
person = {
    "name":"Carquialo",
    "surname":"Pérez",
    "age":32,
    "country":"Sevilla",
    "is_married":False,
    "skills":["Python","Ciberseguridad","Análisis"]

}

person_copy = person.copy()



## Obtener lista de claves del diccionario.
person = {
    "name":"Carquialo",
    "surname":"Pérez",
    "age":32,
    "country":"Sevilla",
    "is_married":False,
    "skills":["Python","Ciberseguridad","Análisis"]

}
keys = person.keys()    # keys() para obtener sólo las claves.
print(keys)



## Obtener lista de valores del diccionario.
person = {
    "name":"Carquialo",
    "surname":"Pérez",
    "age":32,
    "country":"Sevilla",
    "is_married":False,
    "skills":["Python","Ciberseguridad","Análisis"]

}
values = person.values()
print(values)