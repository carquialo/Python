# 1. Declara y asigna valores a las siguientes variables:
# •	name: una cadena que contenga tu nombre.
# •	age: un número entero que represente tu edad.
# •	height: un número flotante que represente tu altura.
# •	Imprime cada variable en una línea separada.

name = "Carlos"
age = 32
height = 1.98
print ("Mi nombre es:", name, "tengo",age, "años y mido", height, "metros.")


# 2. Convierte la variable edad de entero a cadena y concatenala con un texto que diga cuántos años tienes.

print ("Tengo " + str(age) + " años")

# 3. Declara una variable booleana is_student que indique si eres estudiante o no. Usa True o False según corresponda e imprímela.

is_student = False
print("¿Soy estudiante?", is_student)

# 4. Usa la función len() para calcular cuántos caracteres tiene tu nombre completo, almacenado en una variable.

nombre= "Carlos Pérez Gómez" 
print ("Mi nombre completo tiene", len(nombre), "caracteres.")

# 5. Declara tres variables en una sola línea que representen tu nombre, apellido y ciudad de origen. Luego, imprime estos valores.

nombre, apellido, ciudad = "Carlos", "Caín", "Madrid"
print("Nombre:", nombre, "Apellido:", apellido, "Ciudad:", ciudad)

# 6. Usa la función input() para solicitar al usuario su color favorito y almacénalo en una variable color. Luego, imprime el valor ingresado.

#color = input("¿Cuál es tu colos favorito? ")
print("Tu color favorito es:", color)


# 7. Declara una variable fruit e inicialízala con un valor. Luego, cambia el valor de la fruta a otro diferente y vuelve a imprimirla.

fruit = "Plátano"
print("Fruta inicial:", fruit)
fruit = "Fresa"
print("Fruta cambiada:", fruit) 

# 8. Convierte un número decimal, almacenado en la variable price, a un número entero y luego imprímelo.

price = 19.99
print("Precio original:", price)
price = int(price)
print("Precio convertido a entero:", price)

# 9. Declara una variable llamada address_len y almacena en ella la cantidad de caracteres de una dirección usando la función len(). Imprime el resultado.

address_len = len("Calle Falsa 123, Ciudad")
print("La longitud de la dirección es:", address_len)

# 10. Usa un tipo de dato forzado para declarar una variable phone, asegurándote de que siempre será un número. Luego, cambia su valor a un número diferente y verifica el tipo de la variable con type().

phone: int = 123456789
print(type(phone))
phone = 987654321
print(type(phone))
