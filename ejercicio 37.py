print("Ingrese tres números teniendo en cuenta el orden en que los digita:")

n1 = input()
n2 = input()
n3 = input()

if n1 < n2 < n3:
    print("Los números estan incrementando")
else:
    if n1 > n2 > n3:
        print("Los números estan disminuyendo")
    else:
        print("Los números no estan incrementando ni disminuyendo")
