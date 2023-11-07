#solicitar el usuario el numero de repeticiones #6 
N=int(input("ingrese el numero de repeticiones:"))

#Solicitar eal usuario un segundo data entero 
aux1 = int(input("ingrese un segundo dato entero:"))

#iniciar el ciclo while 
i=0 
while i<N: 
        valor=aux1 ** N
        print("Valor en la interaccion", i*1, "es:", valor )
        i+=1
         