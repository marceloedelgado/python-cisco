secret_number = 777

print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")

#Inicio

number = int(input("Ingrese el número secreto: "))

while number != 777 :
    print("¡Ja, Ja! Estás atrapado en mi bucle")
    number = int(input("Ingrese el número secreto: "))

else :
    print("¡Bien hecho muggle!, Eres libre ahora")