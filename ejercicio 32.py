print("Ingrese un año para comprobar si es bisiesto :")

año = int(input())

if año % 4 != 0:
    print("No es bisiesto")
elif año % 4 == 0 and año % 100 != 0: 
	print("Es bisiesto")
elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0: 
	print("No es bisiesto")
elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0: 
	print("Es bisiesto")