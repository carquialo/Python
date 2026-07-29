### Cadena de texto ###

my_string = "Mi string" # Cadena de texto con comillas dobles.
my_other_string = 'Mi otro string'  # Cadena de texto con comillas simples.
print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string) # Podemos concatenarlas.

# Salto de línea.
my_string = "Esta es una cadena de texto\ncon salto de línea"
print(my_string)

# Tabulación. 
my_string = "\tEsta es una cadena de texto con tabulación."
print(my_string)


# Formateo.
name,surname,age = "Carquialo", "Pérez", 32
print("Mi nombre es %s %s y mi edad es %d" %(name,surname,age))
print("Mi nombre es {} {} y mi edad es {}" .format(name,surname,age))

# La siguiente cadena es más compleja y habría que pasar el número entero (32) a texto.
print("Mi nombres es " + name + " " + surname + " " + "y mi edad es " + str(age))

# Inferencia de datos.
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaquetado de caracteres.
language = "Python"
a,b,c,d,e,f = language # Habría que poner por cada caracter de la cadena de texto la mismas variables. Python tiene 6 letras. a(1), b(2), etc.
print(a)
print(b)

# Obtener caracteres por índice.
language_slice = language [1:3]
print(language_slice)

language_slice = language [1:]
print(language_slice)

language_slice = language [-2]
print(language_slice)


# Reverse
greeting = 'Hello, World!'
print(greeting[::-1]) # !dlroW ,olleH



# Funciones. 
language = "python"
print(language.capitalize()) # Devuelve la primera letra en mayúsculas.
print(language.upper()) # Todas las letras en mayúsculas.
print(language.count("t")) # Contar cuantas "t" tiene. 
print(language.isnumeric()) # Si es numérico. (False)
print(language.lower()) # Todas en minúsculas. 

