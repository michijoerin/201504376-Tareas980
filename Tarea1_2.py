
#201504376 - ROCIO MISHELL JOERIN DOMINGO
#TAREA 1- NUMEROS AMIGOS
#Para hallar los pares de numeros amigos se aplica el teorema de Thabit 

N = int(input("ingrese numero N de pares de amigos que desea: "))


def Thabit_func(N): # a=(2**n)*p*q  y  b=(2**n)*r

    lista_amigos = []    #Lista de números amigos
    num = 0 #Contador parejas
    n = 1
    
    while True:
        n += 1 
        div_a = 0
        div_b = 0 

        #Definiendo las ecuaciones del algoritmo
        p = (3 * (2 ** (n-1)) - 1) 
        q = (3*(2**(n))-1)  
        r = (9*(2**(n*2-1))-1) 
        kp = 0 
        kq = 0 
        kr = 0
        
        # Vector donde se almacenan los pares de amigos
        amigos = []
        
        for i in range(1,p): 
            l = p % i     
            if (l == 0):
                kp = kp + i

        # Verificando que p sea un numero primo para avanzar
        if kp == 1:           
            for j in range(1,q): 
                l = q % j         
                if (l == 0):
                    kq = kq + j

        # Verificando que q sea primo para avanzar
            if kq == 1: 
                for k in range(1,r):        
                    l = r % k
                    if (l == 0):
                        kr = kr + k

        # verficar que r sea primo
                if kr == 1:

        # a y b son amigos si se cumplen las condiciones anteriores         
                    a=(2**n)*p*q        
                    b=(2**n)*r         

                    for x in range(1,a):
                        l = a % x
                        if (l == 0):
                            div_a = div_a + x

                    if (div_a == b):    
                        amigos.append(a)

                        for y in range(1,b):   
                            l = b % y
                            if (l == 0):
                                div_b = div_b + y
                                
                        if (div_b == a):      
                            amigos.append(b)
                            num=num+1      
                            lista_amigos.append(amigos)
                        
                        if num == N:     
                            print("Los pares de amigos son: ", lista_amigos)
                            break
                        
Thabit_func(N)
