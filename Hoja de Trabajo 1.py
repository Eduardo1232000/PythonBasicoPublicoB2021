
print("=================== Triangulo de asteriscos ===================")
numero= int(input("introduce el tamaño del triangulo: "))
for filas in range(numero):
    for columnas in range(filas+1):
        print("*", end="")
    print("")
print("===============================================================")
print(" ")


print("============= Determinar si un numero es primo ================")
numero = int(input("ingresa un numero mayor a 2: "))
dividir=2
if (numero > 1):
    while numero % dividir !=0:
        dividir+= 1
    if dividir == numero:
        print(str(numero) +" "+"es primo")
    else: 
        print(str(numero) +" "+"no es primo")

    print("===============================================================")

else: print ("el numero debe ser mayor a 1")

    
