#Tarea No. 1, Proyectos de Computación A.E.I Junio 2020
# ROCÍO MISHELL JOERIN DOMINGO

N= int (input("ingrese N cantidad de numeros perfectos que desea conocer:  "))
m=0 #Contador de N
numero=1 #Contador de numero perfecto
while (numero):#mientras numero sea diferente de 0, se ejecutara el programa
    numero+=1
    r = 0 #contador del resultado
    for i in range(1,numero):
        if (numero%i) == 0:
            r=r+i
    if numero == r: 
        print (numero, " es un numero perfecto")
        m+=1
        
    if m==N:#si se alcanza la cantidad N de numeros perfectos requeridos se para el ciclo
        break
    