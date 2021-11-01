#43.Escribe un algoritmo o el respectivo diagrama de flujo que imprima los primeros 10 números naturales pares

numero=0

print("Los 10 primeros números naturales pares son:")

while numero<=20:
    numero= numero+1
    if numero % 2 == 0:
        print(numero)