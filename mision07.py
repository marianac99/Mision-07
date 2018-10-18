# Mariana Caballero Cabrera
#Programa que despliega un menú y da opción al usuario de elegir entre 3 opciones


# función para calcular residuo y cosciente
def dividir(dividendo, divisor):
    cociente = 1
    residuo = 0
    while dividendo-divisor >= residuo:
        cociente += 1
        residuo = divisor * cociente
    residuo=dividendo-residuo
    print(dividendo,"/",divisor,"=",cociente,", sobra", residuo)

#Función que calcula el número mayor entre todos los números que de el usuario
def encontrarMayor():
        mayor = -1
        print()
        numero = int(input("Teclea un número [-1 para salir]: "))
        while numero != -1:
            if numero > mayor:
                mayor = numero
                numero = int(input("Teclea un número [-1 para salir]: "))
            else:
                numero = int(input("Teclea un número [-1 para salir]: "))
        if numero == -1 and mayor != -1:
            print("El mayor es:", mayor)
        if numero == -1 and mayor == -1:
            print("No hay valor mayor")




#Funci´ón principal
def main():
    opcion = -1
    while opcion != 0:
        print("Misión 07. Ciclos while ")
        print("Autor: Mariana Caballero Cabrera")
        print("Matricula: A01376544 ")
        print("1. Calcular divisiones ")
        print("2. Encontrar el mayor ")
        print("3. Salir ")
        opcion = int(input("Teclea tu opción: "))
        print()


        if opcion ==1:
            print ("Calcula divisiones")
            dividendo = int(input("Dividendo: "))
            divisor = int(input("Divisor: "))
            dividir(dividendo, divisor)
            print()

        elif opcion ==2:
            encontrarMayor()
            print()
        elif opcion==3:
            print("Gracias por usar este programa, regresa pronto.")
            print()
            break
        else:
            print("ERROR, teclea 1, 2 o 3")
            print()

#Llamamos a la función principal
main()
