print("Ingrese dos números:")
numeros = []
for i in range(2):
    numero =input("Número:".format(i+1))


if numero in range(0,5):
    print("Los números estan en el rango de 0 a 5")
else:
    print("false")