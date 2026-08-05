### Condicionales ###

## Condición if.
# if se usa para saber si la condición es verdadera y ejecutar un bloque de código. RECUERDA, la indentación después de los dos puntos.
# Sintaxis
#if condition:
    # Si la condición es verdadera, ejecutar este bloque de código.

a = 3
if a > 2:   # Al ser True, se ejecuta el siguiente código.
    print("a, es mayor que 2")



## If Else. 
# Si la condición es verdadera se ejecuta el primer código, de lo contrario se ejecuta el código del bloque else.
# Sintaxis
#if condition:
    # Si la condición es verdadera, ejecutar este bloque
#else:
    # Si la condición es falsa, ejecutar este bloque

a = 3
if a < 0: 
    print("a, es menor que 0")
else:
    print("a, es mayor que 0")



## If Elif Else.
# Cuando tenemos múltiples condicionales usamos elif. Como en la vida, tomamos decisiones cada día que implican más de una condición.

a = 0 
if a > 0:
    print("a es mayor que 2")
elif a < 0:
    print("a es menor que 2")
else:
    print("a es 0")



## Condicionales anidados.
# Los condicionales pueden anidarse.

a = 0
if a > 0:
    if a % 2 == 0:
        print('A es un número positivo y par')
    else:
        print('A es un número positivo')
elif a == 0:
    print('A es cero')
else:
    print('A es un número negativo')



## If y operadores lógicos. 
# Sintaxis
#if condición and condición:
    # código


a = 0 
if a > 0 and a %2 == 0:
    print("a es un número positivo y par.")
elif a > 0 and a != 0:
    print("a es un número positivo.")
elif a == 0:
    print("a es igual a cero.")
else:
    print("a es un número negativo")



## If y operador lógico Or 
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
    print('Acceso concedido!')
else:
    print('Acceso denegado!')