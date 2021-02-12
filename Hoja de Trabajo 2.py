print("=================== Ingreso de Contraseña ===================")
contraseña= str(input("introduce la contraseña a guardar "))
salida = 0
intentos = 5
while(salida<=5):
    ingreso= str(input("ingresa la contraseña para continuar"))
    if ingreso ==contraseña:
        print ("contraseña correcta")
        break
    else:
        
        print("contraseña incorrecta. Tiene " +str(intentos) +" intentos mas")
        intentos= intentos -1
        salida= salida+1
print("=============================================================")


print("================= Clasificacion de niños =========================")
nombre = str(input("ingresa el nombre del niño(a)"))
genero = str(input("ingresa el genero del niño(a)(debes ingresar M o F)"))
if genero =="M":
    if nombre.lower() < "m":
        grupo = "A"
    else:
        grupo = "B"
else:
    if nombre.lower() > "n":
        grupo ="A"
    else:
        grupo = "B"
print("Tu grupo es " + grupo)
print("==================================================================")
