print("Se va addeterminar el IVA (19%)de su compra")
precio = int
iva = 19
while True:
    try:
        precio = int(input("precio = "))
        break
    except:
        print("solo numeros")
        continue

print("precio normal es", precio, " - el valor del iva es {}%".format(iva), " - el precio final es",((precio * iva) / 100) + precio)