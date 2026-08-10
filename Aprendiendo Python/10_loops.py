### Loops ###
# Para gestionar tareas repetitivas se usa los bucles: while y for. 

## Bucle while.
# Repite un bloque de código mientras la condición se cumpla. Cuando la condición se vuelve falsa, el bucle termina y se ejecuta el código que sigue.
count = 0 
while count < 5:
    print(count)
    count = count + 1
    # Nos devuelve del 0 al 4. 


# Si queremos ejecutar un bloque cuando la condición sea falsa, podemos usar la palabra clave else.
count = 0
while count < 5:
    print(count)
    count = count + 1   # Nos devuelve hasta 4
else:   # Cuando count sea falso y se ejecutará el bloque else. 
    print(count)



## break y continue.

# break: cuando queremos salir del bucle.
# syntax
#while condition:
    #code goes here
    #if another_condition:
        #break

count = 0
while count < 5:
    print(count)
    count += 1
    if count == 3:
        break   # Cuando llegue hasta 3 "rompe" el bucle. Se impreme 0, 1 y 2.


# Continue.
# Continue: cuando queremos saltarnos la iteración actual y continuar con la siguiente.
count = 0
while count < 5:
    if count == 3:
        count = count + 1
        continue
    print(count)
    count = count + 1   # Imprime 0, 1, 2, 4 (el 3 lo saltó).


## Bucle for. 
# for se usa para iterar sobre secuencias (listas, tuplas, diccionarios, conjuntos, cadenas, etc.).

# Bucle for para listas.
# syntax
#for iterator in lst:
    #code goes here

# Ejemplo.
numbers = [0, 1, 2, 3, 4, 5]
for num in numbers: # num es un nombre temporal que referencia el elemento de la lista dentro del bucle.
    print(num)  # Se imprimirá cada elemento. 

# Bucle for para cadenas.
language = "Python"
for letter in language:
    print(letter)   # Imprime cada letra de la cadena de texto. 

for i in range(len(language)):
    print(language[i])


# Bucle for para tuplas.
numbers = (0, 1, 2, 3, 4, 5)
for num in numbers:
    print(num)

# Bucle for para diccionarios Al iterar, se recorrerán las claves del diccionario.
person = {
    "name":"Carquialo",
    "surname":"Pérez",
    "age":32,
    "country":"Sevilla",
    "is_married":False,
    "skills":["Python","Ciberseguridad","Análisis"]

}
for key in person:
    print(key)  # Sólo se imprimirá la clave. 

for key, value in person.items():
    print(key,value)    # Así podríamos para sacar la clave y valor. 


# Bucle for para conjuntos.
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)



## break y continue.
# Break
# syntax
#for iterator in sequence:
    #code goes here
    #if condition:
        #break

numbers = (0,1,2,3,4,5)
for num in numbers:
    print(num)
    if num == 3:
        break

# Continue.
  # syntax
#for iterator in sequence:
    #code goes here
    #if condition:
        #continue

numbers = (0,1,2,3,4,5)
for num in numbers:
    print(num)
    if num == 3:
        continue



## Función range()
# Genera una secuencia de números. La forma range(start, end, step) acepta tres parámetros: inicio, fin y paso. Por defecto inicio es 0 y el paso es 1. Se necesita al menos un parámetro (el valor de fin).
# syntax
#for iterator in range(start, end, step):

lst = list(range(11)) 
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # start y stop, paso por defecto 1
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}



## Bucles for anidados.
# syntax
#for x in y:
    #for t in x:
        #print(t)

person = {
    "name":"Carquialo",
    "surname":"Pérez",
    "age":32,
    "country":"Sevilla",
    "is_married":False,
    "skills":["Python","Ciberseguridad","Análisis"]

}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)



## for y else
# else para ejecutar un código después que termine el bucle.
for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('El bucle termina en', number)
