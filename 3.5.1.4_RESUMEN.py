"""
Puntos Clave

1. Puedes usar el método sort() para ordenar los elementos de una lista, por ejemplo:
 """

lst = [5, 3, 1, 2, 4]
print(lst)

lst.sort()
print(lst)  # outputs: [1, 2, 3, 4, 5]


#2.También hay un método de lista llamado reverse(), que puedes usar para invertir la lista, por ejemplo:

lst = [5, 3, 1, 2, 4]
print(lst)

lst.reverse()
print(lst)  # salida: [4, 2, 1, 3, 5]





#Ejercicio 1

#¿Cuál es la salida del siguiente fragmento de código?

lst = ["D", "F", "A", "Z"]
lst.sort()

print(lst)


#Revisar
#['A', 'D', 'F', 'Z']

#Ejercicio 2

#¿Cuál es la salida del siguiente fragmento de código?

a = 3
b = 1
c = 2

lst = [a, c, b]
lst.sort()

print(lst)


#Revisar
#[1, 2, 3]

#Ejercicio 3

#¿Cuál es la salida del siguiente fragmento de código?

a = "A"
b = "B"
c = "C"
d = " "

lst = [a, b, c, d]
lst.reverse()

print(lst)


#Revisar
#[' ', 'C', 'B', 'A']

