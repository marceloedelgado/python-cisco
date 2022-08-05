"""
inicial=int(input("Ingrese valor inicial: "))
final=int(input("Ingrese valor final: "))
while inicial>final-1:
    inicial+=1
    print("Número: ",inicial)
"""
""""
while True:
    entrada=input("->")
    if entrada=="salir":
        print("Fin de Programa")
        break
    else:
        print(entrada)
"""

deportes=["Tenis", "Basquet", "Ping Pong", "Futbol", "Volley"]
i=0
while i<len(deportes):
    print(deportes[i])
    i+1