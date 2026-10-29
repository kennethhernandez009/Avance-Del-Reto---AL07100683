print ("\n****Nombre Completo:Kenneth Israel Hdz C.***\n")
print ("***Matrícula:AL07100683***\n")

print ("<<<<<<<<<<<<<< Ejercicio 7: MI TIEMPO EN PANTALLA >>>>>>>>>>>>>>>\n")

nombre = input("¿Cómo te llamas?")
límite = float(input("¿Cuál es tu límite de horas?"))
horas_redes = float(input("¿Cuántas horas pasas en redes sociales?"))
horas_juegos = float(input("¿Cuántas horas pasas en videojuegos?"))

total = horas_redes + horas_juegos
print (nombre + ",hoy usaste el celular", total, "horas")

if total > límite:
    print ("Te pasaste", total - límite, "horas de tu ímite, ¡Es hora de desconectarte!")
else:
    print ("¡Felicidades!, Cumpliste tu meta de tiempo en pantalla")

if horas_redes > horas_juegos:
    print ("Lo que más usaste fueron las redes sociales\n")
else:
    print ("Lo que más usaste fueron los videojuegos\n")
    