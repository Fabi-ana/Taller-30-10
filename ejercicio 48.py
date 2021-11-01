#Escribe un algoritmo o el respectivo diagrama de flujo que lea 10 números y calcule su suma y su promedio

suma  =  0
print ( "Ingrese 10 números ...." )
for i in range ( 10 ):
    numero  =  int (input())
    suma  =  suma + numero
print ( "La suma de los números = {} \ n El promedio de los números es = {: .2f}" . formato ( suma , suma / 10 ))