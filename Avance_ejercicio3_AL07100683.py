print ("\n****Nombre Completo:Kenneth Israel Hdz C.***\n")
print ("***Matrícula:AL07100683***\n")

print ("*** Ejercicio 3: WI-FI DEL CAFÉ ***\n")

contrasena_café = "Latte2026"

nombre = input("¿Cómo te llamas?")
contrasena = input("Escribe la contraseña:")
gasto = float(input("¿Cuánto gastaste?"))

if contrasena == contrasena_café:
    print ("Conectado al Wi-Fi, Bienvenido", nombre)
else:
    print ("Contraseña Incorrecta")

if gasto >= 100:
    print ("Tienes 1 hora de Wi-Fi\n")
else:
    print ("Tienes 30 minutos de Wi-Fi\n")
    