
from io import open # Importamos la librería io y la función open

texto = "una line"

archivo = open("archivo.txt", "w")
archivo.write(texto)
texto = "\nuna line nueva"
archivo.write(texto)
texto = "\nuna line nueva tres"
archivo.write(texto)
archivo.close()
 