### Operadores ###

# Operadores aritméticos.
print(3 + 2)
print(3-2)
print(3*3)
print(3/3)      # La división en Python da un número flotante. 
print(3//3)     # Sin número flotante. 
print(3%2)      # Da el resto. 
print(2**3)     # Significa 2*2*2.

# Operadores de comparación.
print(3>2)      # True, 3 es mayor que 2.
print(3<2)      # False, 3 no es menor que 2.
print(3>=2)     # True, 3 es mayor o igual que 2.
print(3<=2)     # False, 3 no es menor o igual que 2.
print(3==2)     # False, 3 no es igual que 2.
print(3!=2)     # True, 3 es diferente que 2.
print(len("zanahorias") > len("arroz"))     # True
print(len("zanahorias") < len("arroz"))     # False
print((len("zanahorias") >= len("arroz")))  # True
print((len("zanahorias") <= len("arroz")))  # False
print((len("patata") == len("tomate")))     # True
print((len("zanahorias") != len("arroz")))  # True

print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)

# Operadores lógicos. 
print(3 > 2 and 4 > 3)  # True - porque ambas expresiones son True
print(3 > 2 and 4 < 3)  # False - porque una de las expresiones es False
print(3 < 2 and 4 < 3)  # False - porque ambas expresiones son False
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)  # True - porque una o ambas expresiones son True
print(3 > 2 or 4 < 3)  # True - porque una de las expresiones es True
print(3 < 2 or 4 < 3)  # False - porque ambas expresiones son False
print('True or False:', True or False)
print(not 3 > 2)     # False - 3 > 2 es True, not True es False
print(not True)      # False - not convierte True en False
print(not False)     # True
print(not not True)  # True
print(not not False) # False


