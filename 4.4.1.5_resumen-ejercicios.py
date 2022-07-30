Ejercicio 1

¿Qué ocurrirá cuando se intente ejecutar el siguiente código?

def message():
    alt = 1
    print("¡Hola, mundo!")


print(alt)


Revisar
Se arrojará una excepción NameError (NameError: name 'alt' is not defined)


Ejercicio 2

¿Cuál es la salida del siguiente fragmento de código?

a = 1


def fun():
    a = 2
    print(a)


fun()
print(a)


Revisar
2
1

Ejercicio 3

¿Cuál es la salida del siguiente fragmento de código?

a = 1


def fun():
    global a
    a = 2
    print(a)


fun()
a = 3
print(a)


Revisar
2
3

Ejercicio 4

¿Cuál es la salida del siguiente fragmento de código?

a = 1


def fun():
    global a
    a = 2
    print(a)


a = 3
fun()
print(a)


Revisar
2
2
