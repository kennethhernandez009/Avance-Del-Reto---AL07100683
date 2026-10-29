
print ("****Nombre Completo:Kenneth Israel Hdz C.***\n")
print ("***Matrícula:AL07100683***\n")
print ("***Ejercicio 1: Estado de mi Celular***\n")

batería = int(input("¿Cuánta batería tienes?"))
espacio = int(input("¿Cuántos GB libres tienes?"))
notificaciones = int(input("¿Cuántas notificaciones sin leer tienes?"))

if batería <= 20: 
    print ("Batería baja, conecta tu cargador")

if espacio < 5:
    print ("Poco espacio, deberías borrar fotos o apps que no uses")

if notificaciones > 0:
    print ("Tienes", notificaciones, "notificaciones sin leer\n")
else:
    print ("Estás al día, no tienes notificaciones nuevas\n")
    