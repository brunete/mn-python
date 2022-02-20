import gauss_seidel as gs
import jacobi as j
import lagrange as l
import numpy as np
import util

if __name__ == "__main__":
    def ejecutar_jacobi_gauss():
        f1 = lambda y,z: (960-3*y-2*z)/4
        f2 = lambda x,z: (510-x-z)/3
        f3 = lambda x,y: (610-2*x-y)/3

        print('Sistema de funciones:')
        print('4x + 3y + 2z = 960')
        print('x + 3y + z = 510')
        print('2x + y + 3z = 610\n')

        est_x = 100
        est_y = 100
        est_z = 100

        quiere_estimar = util.solicitar_bool('Desea definir las estimaciones iniciales? S/N: ')
        if quiere_estimar:
            est_x = util.solicitar_float('Estimacion para x: ')
            est_y = util.solicitar_float('Estimacion para y: ')
            est_z = util.solicitar_float('Estimacion para z: ')
        print()

        if opcion == 1:
            print('- - - - Jacobi - - - -')
            max_iter = util.solicitar_int('Ingrese numero de iteraciones de Jacobi: ')
            print()
            j.jacobi(f1,f2,f3,est_x,est_y,est_z,max_iter)
        
        if opcion == 2:
            print('- - - - Gauss-Seidel - - - -')
            max_iter = util.solicitar_int('Ingrese numero de iteraciones de Gauss-Seidel: ')
            print()
            gs.gauss_seidel(f1,f2,f3,est_y,est_z,max_iter)

    def ejecutar_lagrange():
        xi = None; fi = None

        if util.solicitar_bool("Cargar automaticamente el ejercicio 18.7 de Chapra? S/N: "):
            xi = np.array([1.0,3.0,5.0,7.0,13.0])
            fi = np.array([800.0,2310.0,3090.0,3940.0,4755.0])
            print(f"x = {xi}")
            print(f"f(x) = {fi}")
        else:
            num_puntos = util.solicitar_int("Cuantos puntos iniciales?: ")
            print()

            xi = np.empty(num_puntos)
            fi = np.empty(num_puntos)

            for i in range(num_puntos):
                xi[i]= float(input(f"x[{i}] = "))
                fi[i]= float(input(f"y[{i}] = "))
                print()

        l.lagrange(xi,fi)

    opcion = -1
    while opcion != 0:
        opciones = np.array([0,1,2,3])

        print("- - - - METODOS NUMERICOS - - - -")
        print("1. Metodo de Jacobi\n2. Metodo de Gauss-Seidel\n3. Interpolacion de Lagrange\n0. Salir\n")
    
        opcion = util.solicitar_int("Elija una opcion: ")
        while not opcion in opciones:
            opcion = util.solicitar_int("Elija una opcion: ")
        print()

        if opcion == 1 or opcion == 2:
            ejecutar_jacobi_gauss()
        if opcion == 3:
            ejecutar_lagrange()
        
        input("Presione ENTER para continuar...")