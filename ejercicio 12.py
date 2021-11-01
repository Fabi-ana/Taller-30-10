print("Se va a calcular la distacia recorrida por un objeto que va en línea recta")
while True:
    try:
        tiempo = float(input("tiempo en seg = "))
        aceleracion = float(input("aceleración en m/s2= "))
        velocidadi = float(input("velocidad inicial m/seg= "))
        velocidadf = float(input("velocidad final m/seg= "))
    except:
        print("solo numeros")
        continue
    print("la distancia que recorrio el objeto es",(velocidadi*tiempo)+((aceleracion*(tiempo**2))/2),"metros")
    break

