#Escribe un algoritmo o el respectivo diagrama de flujo que lea 3 números e indique si al 
# menos 2 de ellos son iguales 

num = []

n = int ( input ( 'Ingrese la cantidad de números que quiere ingresar:' ))

for  i  in range ( n ):
    numero = int ( input ( 'Ingrese el valor del número:' ))
    num.añadir(numero)

if  len ( num ) == len ( set ( num )):
    print ( 'No hay números repetidos!' )

else:
    print ( '¡Hay números repetidos!' )