print ("\n****Nombre Completo:Kenneth Israel Hdz C.***\n")
print ("***Matrícula:AL07100683***\n")

print ("*** Ejercicio 4: MIS ESTADÍSTICAS ***\n")

usuario = input("¿Cuál es tu nombre?")
seguidores = int(input("¿Cuántos seguidores tienes?"))
likes = int(input("¿Cuántos likes tuvo tu último post?"))

if seguidores >= 1000:
    print ("Ya puedes hacer lives!")
else:
    print ("Te faltan", 1000 - seguidores, "seguidores para hacer lives")

if likes > seguidores:
    print ("¡Felicidades, Tú último vídeo se hizo viral!\n")
else:
    print ("Sigue publicando, vas bien!\n")
    