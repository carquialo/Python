# 1. Escribe un programa que verifique si un número es positivo, negativo o cero.
number = int(input("Introduce un número: "))
if number > 0:
    print("El número es positivo")
elif number < 0: 
    print("El número es negativo")
else:
    print("El número es cero")

# 2. Solicita al usuario que ingrese su edad y muestra un mensaje indicando si es mayor de edad(18 años o más) o menor de edad.
age = int(input("Introduce tu edad: "))
if age >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")


# 3. Escribe un programa que verifique si una cadena de texto está vacía y muestre un mensaje en consecuencia.
text = input("Introduce una cadena:")
if not text:
    print ("La cadena está vacía.")
else:
    print ("La cadena no está vacía.")

# 4. Crea un programa que solicite dos números al usuario y compare cuál es mayor. Si son iguales, muestra un mensaje indicando la igualdad.
number1 = int(input("Introduce el primer número:"))
number2 = int(input("Introduce el segundo número:"))

if number1 > number2:
    print("El número primero es mayor")
elif number2 > number1:
    print ("El número segundo es mayor")
else:
    print ("Son iguales")


# 5. Escribe un programa que verifique si un número es divisible por 3 y por 5 al mismo tiempo.
number = int(input("Introduce número para ver si es divisible por 3 y por 5: "))
if number % 3 == 0 and number %5 == 0:
    print (f"{number} es divisible por 3 y por 5.")
else: 
    print (f"{number} no es dibisible ni por 3 ni por 5.")


# 6. Solicita al usuario que ingrese un número y verifica si es par o impar.
number = int(input("Introduzca un número para ver si es par o impar: "))
if number % 2 == 0 :
    print ("El número es par.")
else:
    print ("El número es impar.")


# 7. Escribe un programa que determine si una persona puede votar en función de su edad(mayor o igual a 18). Si tiene 16 o 17 años, indica que puede votar con permiso especial.
age = int(input("Introduce tu edad: "))
if age >= 18:
    print("Puedes votar")
elif 16 <= age < 18:
    print("Puedes votar con permiso especial")
else:
    print("No puedes votar")


# 8. Crea un programa que solicite una contraseña al usuario y verifique si coincide con una contraseña predefinida. Si no coincide, muestra un mensaje de error.
user_password = input("Hola usuario, introduzca una contraseña: ")
password = "python"

if user_password == password:
    print("Contraseña correcta")
else: 
    print("Error, contraseña incorrecta.")


# 9. Escribe un programa que determine si un número está entre 10 y 20 (ambos incluidos).
number = int(input("Introduzca número, por favor : "))

if number >= 10 and number <= 20:
    print(f"El número {number} está entre 10 y 20.")
else: 
    print(f"El número {number} no se encuentra entre 10 y 20.")

# 10. Escribe un programa que simule un semáforo: solicita al usuario que ingrese un color(rojo, amarillo, verde) y muestra un mensaje indicando si debe detenerse, estar alerta o avanzar.

color = input("Introduce un color (rojo, amarillo, verde): ").lower()
if color == "rojo":
    print("Detente")
elif color == "amarillo":
    print("Precaución")
elif color == "verde":
    print("Avanza")
else:
    print("Color no válido")

