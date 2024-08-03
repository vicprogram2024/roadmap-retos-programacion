""" Operadores """

# OPERADORES ARITMETICOS

#print (f"Suma 7 + 15 = {7 + 15}")
num1 = 10
num2 = 15
num3 = 55
resultado_suma = num1 + num2
resultado_resta = num1 - num2
resultado_multiplicacion = num1 * num2
resultado_division = num1 / num2
resultado_porcentaje = num1 % num2
resultado_potencia = num1 ** num2
resultado_diventero = num1 // num2

print (f"La suma de 10 + 15 = {resultado_suma}")
print (f"La resta de 10 - 15 = {resultado_resta}")
print (f"La multiplicacion de 10 * 15 = {resultado_multiplicacion}")
print (f"La division de 10 / 15 = {resultado_division}")
print (f"El porcentaje de 10 % 15 = {resultado_porcentaje}")
print (f"La pontencia de 10 ** 15 = {resultado_potencia}")
print (f"La division de numero entero de 10 // 15 = {resultado_diventero}")

#OPERADORES LOGICOS 

""" Se utiliza para tomar decisiones basadas en multiples condiciones."""

# Operador And 

""" Evalua si los valores de ambos lados son verdaderos,si se cumple nos dara un true, en caso contrario sera false.

(true and true) true
(true and flase) false
(false and true) false 
(false and flase) false """

#Operador Or

"""Nos da true cuando al menos uno de los valores es verdadero.

(true or true) true
(true or flase) true
(false or true) true 
(false or flase) false"""

# Operador not

print (f"El numero 17 es mayor que 15 y 50 es mayor que 15: {17 > 15 and 50 > 15}")
print (f"El numero 50 es menor que 15 or 17 es menor que 50 es: {50 < 15 or 17 < 50}")
print (f"El numero 50 es menor que 15 or 17 es mayor que 50 es: {50 < 15 or 17 > 50}")
print (f"El resultado de 10 + 9 == 20: { not 10 + 9 == 20}")

# OPERADORES DE COMPARACION 

""" Comparan o establecen una relacion entre ellos.
Devolvera un valor true o false basado en una condicion """


print (f"El numero 8 es mayor que el numero 7: {8 > 7}")
print (f"El numero 7 es menor que el numero 9: {7 < 9}")
print (f"El numero 7 es igual que el numero 8: {7 == 8}")
print (f"El numero 7 es mayor o igual que el numero 8: {7 >= 8}")
print (f"El numero 7 es menor o igual que el numero 9: {7 <= 9}")
print (f"El numero 9 es diferente que el numero 7: {9 != 7}")

#OPERADORES DE ASIGNACION 

valor= 45
print (f"Mi valor inicial es: {valor}")
valor += 5
print (f"Suma y asignacion es: {valor}")
valor -= 5
print (f"Resta y asignacion es: {valor}")
valor *= 5
print (f"Multiplicacion y asignacion es: {valor}")
valor /=4
print (f"Division y asignacion es: {valor}")
valor %= 5
print (f"Modulo y asignacion es: {valor}")
valor **= 15
print (f"Exponente y asignacion es: {valor}")
valor //= 5
print (f"Division entera y asignacion es: {valor}")

#OPERADORES DE IDENTIDAD

"""Sirven para comprobar si dos variables emplean la misma ubicacion en memoria

Is nos da true si los operandos se refieren al mismo objeto.
Is not da true si los operandos no se refieren al mismo objeto"""

valor1= valor
print (f"valor is valor1 es: {valor is valor1}")
print (f"valor is not valor1 es: {valor is not valor1}")

# OPERADORES DE PERTENECIA

""" Identifica la pertenencia de un operador en una secuencia """

print (f"La letra 'i' in 'Victor': {'i' in 'Victor'} ")
print (f"La letra 'n' in not 'Victor': {'n' not in'Victor'} ")

"""

ESTRUCTURAS DE CONTROL

"""

# CONDICONALES

"""
Le permite nuestro codigo verificar cual camino puede tomar.
Si algo se cumple toma este camino, sino se cumple entonces toma este otro camino 

"""

a=27
if a >= 10 and a <=25 :
    print ("Mi numero se encuentra entre 10 y 25")
elif a < 10:
    print ("Mi numero es menor a 10") 
else:
    print ("Mi numero es mayor a 25")

# INTERATIVAS 
""" Dentro de las interativas encontramos los bucles de for y while"""

# FOR 
palabra = "Victor"
for list in palabra:
    print (list)

for i in range (4):
    print (i)

# WHILE

num = 1
while num <= 15:
    print(num)
    num += 1

    
    
""" 
EXTRAS

"""
print("CASO EXTRA")

for number in range (10, 56):
    if number % 2 == 0 and number != 16 and number %3 != 0:
        print (number)
    