### Funciones ###
# También se puede crear funciones a partir por el usuario.
# Una función es un bloque de código reutilizable o una sentencia de programación que realiza una tarea específica.

# Sintaxis
# Declarar una función
#def function_name():
    #codes
    #codes
# Llamar a una función
#function_name()


## Función sin parámetros
def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers()


## Funciones que retornan valores.
# Una función también puede devolver un valor; si una función no tiene return, devuelve None.
def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_numbers())



## Funciones con parámetros. 

# Parámetro único: si una función necesita un parámetro, la llamamos con un argumento.
  # Sintaxis
  # Declarar una función
  #def function_name(parameter):
    #codes
    #codes
  # Llamar a la función
  #print(function_name(argument))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))


# Dos parámetros: una función puede no tener parámetros o tener uno o varios. Si necesita dos parámetros, la llamamos con dos argumentos.
def sum_two_numbers (num_one, num_two):
    sum = num_one + num_two
    return sum
print('Sum of two numbers: ', sum_two_numbers(1, 9))


## Pasar argumentos por clave y valor.
def add_two_numbers (num1, num2):
    total = num1 + num2
    print(total)
print(add_two_numbers(num2 = 3, num1 = 2)) # el orden no importa


## Funciones con parámetros por defecto.
# Si no proporcionamos un argumento al llamar la función, se usa el valor por defecto.
def greetings (name = 'Peter'):
    message = name + ', welcome to Python!'
    return message
print(greetings())
print(greetings('Carquialo'))

def weight_of_object (mass, gravity = 9.81):
    weight = str(mass * gravity)+ ' N' # gravedad promedio en la superficie de la Tierra
    return weight
print('Weight of an object in Newtons: ', weight_of_object(160)) # 9.81 - gravedad promedio en la Tierra
print('Weight of an object in Newtons: ', weight_of_object(160, 1.62)) # gravedad en la Luna



## Número arbitrario de argumentos
# Si no sabemos cuántos argumentos se pasarán a la función, podemos usar un parámetro con * para aceptar un número arbitrario de argumentos.
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # equivalente a total = total + num
    return total
print(sum_all_nums(2, 3, 5)) # 10