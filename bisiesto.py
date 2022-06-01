# CODIGO PROPIO MAS CORTO BY MARCELO DELGADO

year = int(input("Introduce un año: "))

if (year % 4) == 0 and (year % 100) != 0 : 
    print("Es un año bisiesto") 

elif (year % 400) == 0 :
    print("Es un año bisiesto")
else :
    print("Es un año comun")

# CODIGO CON AYUDITA
year = int(input("Introduce un año: "))

if year < 1582:
	print("No esta dentro del período del calendario Gregoriano")
else:
	if year % 4 != 0:
		print("Año Común")
	elif year % 100 != 0:
		print("Año Bisiesto")
	elif year % 400 != 0:
		print("Año Común")
	else:
		print("Año Bisiesto")
