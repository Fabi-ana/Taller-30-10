print("Ingrese la siguiente información para determinar el costo de su pasaje de avión:")

while True:
    try:
        i1 = int(input("Distancia recorrer en Km:"))
        i2 = int(input("Número de días de estancia:"))
        break
    except:
        print("solo numeros")
        continue


minima = 100000
valor = (i2 * 5000)
valor_minima = (minima + valor)

if i1 < 1000 and i2 < 7 :
    print("El costo de su pasaje de avión es:",int(valor_minima))
else:
    if i1 > 1000 and i2 > 7 :
        descuento = (valor * 0.15)
        valor_total_descuento = (minima+(valor - descuento))

print("El costo de su pasaje de avión es:",int(valor_total_descuento))



