print ("Ingrese tres numeros:")
while True:
    try:
        n1= int(input("Número 1:"))
        n2= int(input("Número 2:"))
        n3= int(input("Número 3:"))
        break
    except:
        print("solo numeros")
        continue

suma = (n1+n2)

if suma > n3:
    print("La suma de los dos primeros números es mayor al tercer número")
else:
    print("La suma de los dos primeros números es menor al tercer número")