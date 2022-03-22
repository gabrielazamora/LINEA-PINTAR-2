def obtienelicencia(edad,ine,nombre):
    if edad>=18 and ine == 's':
        print(nombre,' si tiene licencia')
    else:
        print(nombre,' no tiene licencia')
        
def leer():
    edad=int(input('edad '))
    ine=input('INE s o n ')
    nombre=input('nombre ')
    obtienelicencia(edad,ine,nombre)

n=int(input('cuantas personas '))
for i in range(n):
    print('i ',i)
    leer()

print('valor final de i ',i,' fin del programa')