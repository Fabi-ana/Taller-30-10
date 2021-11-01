numeros = {1 : "Lunes" , 2 : "Martes" , 3 : "Miercoles" , 4 : "Jueves" , 5 : "Viernes" , 6 : "Sabado" , 7 : "Domingo" }
numero = int ( input ( "Ingrese un número de día de la semana (entre  1 y 7):" ))
nombre = numeros . get ( numero )
print ( "{} = {}" . format( numero , nombre ))