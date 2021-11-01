while True:
    try:
        segundos = int(input("segundos: "))
    except:
        print("solo numeros")
        continue
    print(segundos,"segundos a minutos es:",segundos/60)
    break
