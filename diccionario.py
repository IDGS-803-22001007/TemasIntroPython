import os
from io import open  

class Diccionario:
    def __init__(self):
        self.diccionario = {}

    def agregar(self):
        os.system("cls")
        espa = input("Ingrese la palabra en español: ")
        ingl = input("Ingrese la palabra en inglés: ")
        archivo = open("diccionario.txt", "a")
        archivo.write(f"{espa}:{ingl}\n")
        archivo.close() 
        self.diccionario[espa] = ingl
        print("Palabra agregada.")
        input("")

    def buscar(self):
        os.system("cls")  
        print("Buscar palabra:")
        print("1. Buscar por español")
        print("2. Buscar por inglés")
        opcion = input("Seleccione una opción: ")

        with open("diccionario.txt", "r") as archivo:
            for linea in archivo:
                espa, ingl = linea.strip().split(":")
                self.diccionario[espa] = ingl

        if opcion == '1':
            espa = input("Ingrese la palabra en español: ")
            if espa in self.diccionario:
                print(f"La traducción en inglés es: {self.diccionario[espa]}")
            else:
                print("Palabra no encontrada.")
        elif opcion == '2':
            ingl = input("Ingrese la palabra en inglés: ")
            found = False
            for esp, value in self.diccionario.items():
                if value == ingl:
                    print(f"La traducción en español es: {esp}")
                    found = True
                    break
            if not found:
                print("Palabra no encontrada.")
        else:
            print("Opción no válida.")
        input("enter por continuar")

    def mostrar_menu(self): 
        os.system("cls")
        print("Menú de opciones:")
        print("1. Capturar Palabra")
        print("2. Buscar Palabra")
        print("3. Salir")

def main():
    diccionario = Diccionario()
    while True:
        diccionario.mostrar_menu()  
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            diccionario.agregar()
        elif opcion == '2':
            diccionario.buscar()
        elif opcion == '3':
            break

if __name__ == "__main__":
    main()
