to_do = ["Dirigirnos al hotel",
         "Ir a almorzar",
         "Visitar un museo",
         "Volver al hotel"]
print(to_do)
# conseptos basicos sobre listas
#una lista en python es una coleccion ordenada de elementos que puede contener elementos de diferentes tipos(enteros, flotantes, cadenas,etc
# las listas son mutables, lo que significa que sus elementos se pueden cambiar despues de que se ha creado la lista.
# creacion de listas)
#como crear una lista en python?
#para iniciar, se crea se crea una variable llamada utilizando corchetes para indicar que se trata de una lista.Dentro de los corchetes, se anaden los elementos separados por comas, por ejemplo:
# todo = ["Dirijirnos al hotel", "Almorzar", "Visitar un museo", "Volver al hotel"]
#Que tipo de datos se pueden almacenar en una lista?
#Las listas en python pueden almacenar multiples tipos de datos, incluyendo cadenas, numeros enteros,numeros flotantes y valores booleanos.Tambien [ueden contener otras listas. Por ejemplo:]
mix = ["string",1,2.5,True,[3,4]]
print(mix)
#como se determina la longitud de una lista?
#Para saber cuantos elementos hay en una lista, se usa la funcion  len :
print(len(mix))
#como se accede a elementos especificos de una lista?

lista_vacia = []
lista_numeros = [1, 2, 3, 4, 5]
lista_mixta = [1, "dos", 3.0, True]
print("lista vacia:", lista_vacia)
print("lista de numeros:", lista_numeros)
print("lista mixta:", lista_mixta)
numbers = [1,2,3,4,"cinco"]
print(type(numbers))
mix = ["uno",2,3.14, True,[1,2,3]]
print(mix)
print(len(mix))
print("Primer elemento", mix[0])
print("Segundo elemento", mix[1])
print("Ultimo elemento", mix[-1])
string = "Hola mundo"
print("Primer elemento", string[0])
print("Segundo elemento", string[3])
print("Primer elemento", string[-1])
print(mix[2:-2])
print(mix)
mix.append(False)
print(mix)
mix.append(["a","b"])
print(mix)
mix.insert(1,["a","b"])
print(mix.index(["a","b"]))
numbers = [1,2,100.01,90.45,3,4,5]
print(numbers)
print(numbers)
print("Mayor:",max(numbers))
print("Menor:",min(numbers))
del numbers[-1]
print(numbers)

mix.insert
mix.append(["a","b"])

numbers = [1,2,3,4,"cinco"]

x = 10
y = 5.678
#z = 1.2E6
#a = 1.2E-6
print(type(x))
print(type(y))
#print(z)
#print(a)
print(x)
print(x + x)
print(x + y)
print(y + y)


