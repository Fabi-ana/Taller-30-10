segundos=int(input("Ingrese la cantidad de segundos a convertir:"))

horas = segundos //(60*60)
segundos = segundos % (60 * 60)
minutos = segundos //60
segundos =  segundos // 60

print("Horas:{} - Minutos:{} - Segundos:{} ".format(horas,minutos,segundos))
