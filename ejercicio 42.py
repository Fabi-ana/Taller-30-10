#42. Escribe un algoritmo o el respectivo diagrama de flujo que imprima los primeros 10 números naturales impares

numero=0

print("Los 10 primeros números naturales impares son:")

while numero<=19:
    numero= numero+1
    if numero % 2:
        print(numero)