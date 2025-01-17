
from io import open # Importamos la librería io y la función open

texto = "una line"

archivo = open("archivo.txt", "r")
texto = archivo.readlines()
print(texto)
texto = archivo.read()
print(texto) 
archivo.close()
 