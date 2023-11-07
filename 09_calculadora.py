# FUNCION DE LA CALCULADORA
print("*********************************")
def suma(cant1, cant2):
    return cant1 + cant2

def resta(cant1, cant2):
    return cant1 - cant2

def multiplicacion(cant1, cant2):
    return cant1 * cant2

def division(cant1, cant2):
    return cant1 / cant2

def Potencias(cant1, cant2):
    return cant1^cant2

def Raiz(cant1, cant2):
    return cant1^1/cant2

def sumapotencias(cant1, cant2):
    return cant1^cant2+cant2^cant1

def Promedios(cant1, cant2):
    return cant1+cant2/2

def comparar(cant1, cant2):
    return  cant1>cant2, cant1<cant2
   
print("*********************************")
print("MENU PRINCIPAL")
print("Por favor, elige una operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. potencias")
print("6. Raiz")
print("7. Suma de potencias")
print("8. promedios")
print("9. Comparaciones de numeros")
print("*********************************")
#INGRESAR NUMERO DE OPERACION

opcion = input("Ingresa una opción (1/2/3/4/5/6/7/8/9): ")

#INGRESAR NUMEROS DE LA OPERACION

numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

#SE REALIZA LA OPERACION DESEADA

if opcion == '1':
    print(numero1, "+", numero2, "=", suma(numero1, numero2))

elif opcion == '2':
    print(numero1, "-", numero2, "=", resta(numero1, numero2))

elif opcion == '3':
    print(numero1, "*", numero2, "=", multiplicacion(numero1, numero2))

elif opcion == '4':
    print(numero1, "/", numero2, "=", division(numero1, numero2))
    
elif opcion == '5':
    print(numero1, "^", numero2, "=", Potencias(numero1, numero2))
    
elif opcion == '6':
    print(numero1, "^", 1/numero2), "=", Raiz(numero1, numero2)
    
elif opcion == '7':
    print(numero1, "^", numero2)+(numero2, "^", numero1), "=", sumapotencias(numero1, numero2)
    
elif opcion == '8':
    print(numero1, "+", numero2/2), "=", Promedios(numero1, numero2)
    
elif opcion == '9':
    print(numero1, ">", numero2, numero1, "<", numero2), "=", comparar(numero1, numero2)
    
else:
    print("Error_Opción inválida")