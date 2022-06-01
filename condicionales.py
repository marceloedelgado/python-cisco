clima = input("El clima de hoy es bueno o malo?: ")
cine = input("Hay entradas de cine disponibles?:")
mesas = input("El restaurante tiene mesas disponibles:?")

if clima == 'bueno':
    print("Saldremos de casa")
elif cine == 'si':
    print("Iremos al cine")
elif mesas == 'si':
    print("Almorzaremos en el restaurante")
else:
    print("Jugaremos al Ajedrez en casa")

    