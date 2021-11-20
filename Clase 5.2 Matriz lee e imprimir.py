"""

Video crear una matriz paso a paso
https://www.youtube.com/watch?v=uJy3vPXzjs0&list=PLS4-ShDA9mk-ie85ID1wFzwQVUSo2068c&index=23

Video ver graficamente como se crea
la matriz del vedeo anterior
https://www.youtube.com/watch?v=fTG9S5MzxMQ&list=PLS4-ShDA9mk-ie85ID1wFzwQVUSo2068c&index=24

Video muestra una matriz en forma
de matriz en pantalla
https://www.youtube.com/watch?v=tEAlR5UgcmA&list=PLS4-ShDA9mk-ie85ID1wFzwQVUSo2068c&index=25


"""

# Programa elaborado por Angeles Constantino

def pide_datos_matriz():
    ren=int(input("Cuantos renglones: "))
    col=int(input("Cuantas columnas: "))
    matriz=[]
    for i in range(ren):
        #seccion que crea un renglon con columnas de datos
        renglon=[]
        for j in range(col):
            print("Teclea el dato para el renglon ", i, " y la columna  ", j)
            dato = int(input())
            renglon.append(dato)
        matriz.append(renglon)
    return matriz

def mostrar_matriz(matriz):
    ren=len(matriz)
    col=len(matriz[0])
    for i in range(ren):
        for j in range(col):
            print(matriz[i][j], end=" ")
        print()
    

def main():
    matriz=pide_datos_matriz()
    print(matriz)
    print("Matriz desplegada en forma de matriz")
    mostrar_matriz(matriz)
    
    
main()