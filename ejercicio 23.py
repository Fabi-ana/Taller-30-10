numero = input("Ingrese un número:")
numero=int(numero)

if numero == 0:
    print("El número es 0")
else:
    if numero % 2 == 0 and numero > 0:
        print(" El número es par positivo")
    else:
        if numero % 2 != 0 and numero > 0:
            print("El número es impar positivo")
        else:
            if numero % 2 == 0 and numero < 0:
                print("El número es par negativo")
            else:
                if numero % 2 != 0 and numero < 0:
                    print("El número es impar negativo")