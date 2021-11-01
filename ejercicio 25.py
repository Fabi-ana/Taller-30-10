print("Ingrese un número:")
while True:
    try:
        a = int(input("número:"))
        break
    except:
        print("solo numeros")
        continue
if a>=10:
    b = a**3
    print("El número es:",b)
else: 
    c = a/4
    print("El número es:",c)

