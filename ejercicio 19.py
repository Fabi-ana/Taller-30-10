billetes = [1000,2000,5000,10000,20000,50000,100000]
monto_dar = int(input("-->"))

def operaciones(monto_dar):
    result = []
    for b in billetes:
        if b == monto_dar:
            print("Un billete de :",b)
            exit()
        cant_billetes_dar= int(monto_dar/b) 
        print(cant_billetes_dar)
        if cant_billetes_dar<0:
            break
        if cant_billetes_dar!=0:
            result.append([cant_billetes_dar,b])

        ordenado = sorted(result)
    for c in ordenado:
        cant =  c[0]
        billete = c [1]
        print(cant, "billetes de",billete)
        dinero_falta = monto_dar-(cant*billete)
        if dinero_falta>0:
            operaciones(dinero_falta)
        else:
            exit()

operaciones(monto_dar)