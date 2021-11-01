print("Ingrese las 5 notas para calcular su promedio:")
while True:
    try:
        n1= int(input("Nota 1:"))
        n2= int(input("Nota 2:"))
        n3= int(input("Nota 3:"))
        n4= int(input("Nota 4:"))
        n5= int(input("Nota 5:"))
        break
    except:
        print("solo numeros")
        continue

p1 = ((n1*15)/100)
p2 = ((n1*20)/100)
p3 = ((n1*15)/100)
p4 = ((n1*30)/100)
p5 = ((n1*20)/100)
pt = ((p1+p2+p3+p4+p5)/5)

if pt < 2.0:
    print("No puede habilitar, su promedio es ",pt)
else:
    if pt < 3:
        print("Usted reprobó, su promedio es",pt)
    else:
        if pt >= 3:
            print("Usted aprobó, su promedio es",pt)
        else:
            if pt > 4.5:
                print("Felicitaciones por su esfuerzo y dedicación, su promedio es",pt)
