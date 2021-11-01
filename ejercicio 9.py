#9.	Escribe un algoritmo o el respectivo diagrama de flujo que dados tres números calcule 
# el promedio de dichos números.

promedio = 0
for x in range(1,4):
    while True:
        try:
            promedio += int(input("num"+str(x)+" = "))
            break
        except ValueError:
            print("solo numeros")
            continue
print("promdeio es igual a=",promedio/3)
