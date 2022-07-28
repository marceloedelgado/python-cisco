

hat_list = [1, 2, 3, 4, 5]
print("Lista Original:", hat_list)

# Paso 1
hat_list[2] = int(input("Ingresa un número para reemplazar el central de la lista: "))
print("Lista con el numero reemplazado:", hat_list)

# Paso 2
del hat_list[-1]

print("Lista con el ultimo numero borrado: ", hat_list)

# Paso 3 
print("La cantidad de elementos de la lista es de:", len(hat_list))