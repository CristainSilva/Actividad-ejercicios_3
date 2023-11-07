#Solicitar al usuario el numero de repeticiones 
N= int(input("Ingrese el numero de repeticiones:"))

aux1= int(input("Ingrese un segundo dato entero"))

for i in range(N): 
    valor=aux1 ** N
    print("Valor en la interaccion",i + 1,"es", valor)
    
    