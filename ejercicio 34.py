sesion = { "usuario" : "carlos" , "contraseña" : "1234" }
usuario = input ( "Ingrese su usuario:" )
contraseña = input ( "Ingrese su contraseña:" )
if  sesion . get ( "usuario" ) == usuario  and  sesion . get ( "contraseña" ) == contraseña :
    print ( "La sesión ha sido iniciada" )
else:
    print ( "El usuario o contraseña está mal. No se ha podido iniciar sesión" ) 