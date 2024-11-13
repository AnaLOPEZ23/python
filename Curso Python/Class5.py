x = 10
y = 5.678
#z = 1.2E6
#a = 1.2E-6
print(type(x))
print(type(y))
#print(z)
#print(a)
print(x + x)
print(x + y)
print(y + y)
is_true = True
is_false = False
print(is_true)
print(type(is_true))
print(is_false)
print(type(is_false))
print("Nunaca pares de aprender")
print("Nunca", "pares", "de", "aprender")
print("Nunca" + "pares" + "de" + "aprender")
print("Nunca"+" " + "pares" + " " + "de" + " " + "aprender")
print("Nunca", "pares", "de", "aprender", sep=",")
print("Nunca" , "pares" , "de" , "aprender", sep=";")
print("Nunca", "pares", "de","aprender", sep="/")
print("Nunca", "pares", "de", "aprender", sep="_")
print("Nunca", "pares", "de", "aprender\n", sep="_")
print("Hola", "mundo", "como", "estan?\n")
#Uso del END
#Espesifica lo que se imprimira al  final de la cadena.puedes cambiar como deseas acabar la cadena
#puedes evitar saltos de linea, agregar espacios,tabulaciones.
print("Hola", end="@")
print("mundo\n")
#uso de F-string
#podemos incluir expresiones dentro de las cadenas, insertando valores o expresiones directamente en la cadena
#sintaxis
# se coloca una f o F antes de las comillas para luego cerrar las expresiones dentro de unas llaves {}
nombre = " PEREZ"
edad = 23

print(f"Mr llamo{nombre} y tengo {edad} anos\n")
# Uso de end
#El parametro end cambia lo que se imprime al final de la llamda a print.En lugar de imprimir cada mensaje en una nueva linea, end="" asegura que "Nunca"
#y "pares" se impriman en la misma linea, resultando en  "Nunca pares".Por defecto, end es un salto de linea("\n")lo que hace que cada llamda a print comienze en una nueva linea.
print("Nunca", end=" ")
print("pares de aprender")
# Impresion de variables
#puedes usar print para mostrar el valor de las variables.En este ejemplo,imprimira "Frase:Nunca pares de aprender" y "Autor: Platzi".Esto es util para depurar y ver los valores de las variables en diferentes puntos de tu programa.
frase = "Nunca pares de aprender"
author = "Platzi"
print("Frase:",frase, "Autor:", author)

#6. Uso de formato con f-strings
#Las f-strings permiten insertar expresiones dentro de cadenas de texto.Al anteponer una f a la cadena de texto,
#puedes incluir variables derectamnete de las llaves{}.En este ejemplo,frase y autor se insertaran en la cadena, resultando en "Frase:Nunca pares de aprender, Autor:Platzi".
#Esto hace que el codigo sea mas legible y facil de escribir.

frase = "Nunca pares de aprender"
author = "Platzi"
print(f"Frase: {frase}, Autor:{author}")

