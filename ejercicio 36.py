while True:
    try:
        numero= int(input("Ingrese un número:"))
        break
    except:
        print("solo numeros")
        continue

if numero < 100000:
    digitos = len(str(numero))
    print("La cantidad de digitos de su número es:",digitos)
else:
    print("Su número es:",numero)


    