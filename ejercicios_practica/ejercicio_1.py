# Funciones [Python]
# Ejercicios de práctica

# Autor: Gaston Ricciuti
# Version: 2.2

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con funciones

def imprimir_mayor(numero_1, numero_2):
    print("Funcion imprimir mayor")
    # En esta función debe determinar cual de los dos
    # números ingresados por parámetro es mayor
    # y luego imprimir dicho valor en pantalla
    if numero_1 >= numero_2:
        numero_mayor = numero_1
    else:
        numero_mayor = numero_2
        print('El numero mayor es: ',numero_mayor)
    return numero_mayor

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Alumno: Complete la función "imprimir_mayor"
    imprimir_mayor(2, 10)
 
    print("terminamos")