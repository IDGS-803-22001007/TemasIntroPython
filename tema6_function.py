import os





def function1():
    os.system("cls")    
    print("Dame dos numeros: ")
    num1=int(input("Numero1: "))
    num2=int(input("Numero2: "))    
    print("La suma de los numeros es: ",num1+num2)
    input()
    return run()
    
    
    
def function2():
    os.system("cls")    
    print("Dame dos numeros: ")
    num1=int(input("Numero1: "))
    num2=int(input("Numero2: "))    
    print("La resta de los numeros es: ",num1-num2)
    input()
    return run()
            
def function3():
    os.system("cls")    
    print("Dame dos numeros: ")
    num1=int(input("Numero1: "))
    num2=int(input("Numero2: "))    
    print("La division de los numeros es: ",num1/num2)
    input()
    return run()

            
def function4():
    os.system("cls")    
    print("Dame dos numeros: ")
    num1=int(input("Numero1: "))
    num2=int(input("Numero2: "))    
    print("La multiplicacion de los numeros es: ",num1*num2)
    input()
    return run()
    




        
def run():
    os.system("cls") 
    print("Menu de opciones:")   
    print("1.- Suma")
    print("2.- Resta")
    print("3.- Division")
    print("4.- Multiplicacion")
    print("5.- Salir")
    opcion=int(input("Dame una Opcion: "))
    if opcion==1:
        function1()
    elif opcion==2:
        function2()
    elif opcion==3:
        function3()
    elif opcion==4:
        function4()
    elif opcion==5:
        exit()
        
        
    

if __name__=="__main__":
    run()

#16 archivos