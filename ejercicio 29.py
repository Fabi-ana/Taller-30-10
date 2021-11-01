numeros = []
for i in range (3):
    numero =input("Ingresa el número:".format(i+1))
    numeros.append(numero)

mayor = numeros[0]
menor = numeros[0]

for numero in numeros:
    if numero > mayor:
        mayor = numero
for numero in numeros:
    if numero < menor:
        menor = numero
print("El mayor de los números es:",mayor)
print("El menor de los números es:",menor)

  