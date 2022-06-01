income = float(input("Introduce el ingreso anual: "))

#Conditionals

if income <= 85528 :
    tax = (income * 0.18) - 556.02
else :
    tax = ((income - 85528) * 0.32) + 14839

if  tax <= 0 :
    tax = 0

tax = round(tax, 0)
print("El impuesto es:", tax, "pesos")