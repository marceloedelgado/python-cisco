#hour = int(input("Hora de inicio (horas): "))
#mins = int(input("Minuto de inicio (minutos): "))
#dura = int(input("Duración del evento (minutos): "))

#final_hour = round(((hour * 60)+ dura)/ 59)
#final_mins = round(((mins * 60)+ dura)/ 59)

#print(final_hour, final_mins, sep=':')

hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# calcula los minutos y los convierte a una cadena
minutos=str((mins+dura) %60)
# calcula los minutos totales y luego lo convierte a horas y despues a una cadena
horas= str( ((hour*60 + mins + dura)//60) % 24)
 
 
print("Hora: " +horas +":" +minutos)















