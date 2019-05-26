
import os
from sympy import *

def menu():

	os.system("clear")
	print ("Selecciona una opción")
	print ("\t1:Suma de matrices")
	print ("\t2:Suma polinomios")
	print ("\t3:Suma numeros complejos")
	print ("\t4:Salir")


while True:

	menu()


	opcionMenu = input("introduce una opcion: ")

	if opcionMenu=="1":

		os.system("clear")
		fil = int(input ("Introduzca el numero de filas: "))
		col = int(input ("Introduzca el numero de columnas: "))

		m1 = []
		m2 = []
		m3 = []
		for i in range (fil):
			m1.append( [0] * col)
			m2.append( [0] * col)
			m3.append( [0] * col)

		print('Ingrese la Matriz 1')
		for i in range(fil):
				for j in range(col):
					m1[i][j] = float(input('Elemento (%d,%d): ' % (i, j)))
		print('Ingrese su Matriz 2')
		for i in range(fil):
			for j in range(col):
					m2[i][j] = float(input('Elemento (%d,%d): ' % (i, j)))

		for i in range(fil):
			for j in range(col):
					m3[i][j] += m1[i][j] + m2[i][j]
		print('el resultado es:')
		print(m3)

		input("\npulsa una tecla para continuar")
	elif opcionMenu=="2":

		os.system("clear")
		init_printing(use_latex="mathjax")
		x= symbols("x")
		y= symbols("y")
		print("""           Calculadora suma Polinomios

		Bienvenido
		En este apartado podras hacer la suma de dos polinomios
		Las variables que puedes usar son x o y
		Antes de que puedas empezar el programa debes saber 3 cosas
		1.Para poder expresar el exponente debes usar dos asteriscos **
		Por Ejemplo:
		x**2
		En este ejemplo la x esta elevada al cuadrado
		2.Para asignar el coefiente a una variable debes usar solo un asterisco
		Por ejemplo:
		6*x**2
		En este ejemplo la x tiene como coeficiente 6
		3. Puedes usar parentesis para jerarquizar operaciones""")

		expand(input("Escribe los polinomios a sumar: \t"))
		input("\npulsa una tecla para continuar")

	elif opcionMenu=="3":

		os.system("clear")
		init_printing(use_latex="mathjax")
		x= symbols("x")
		print("""               BIENVENIDO AL APARTADO DE NUMEROS IMAGINARIOS
		Aqui podras realiza sumas,restas,multiplicaciones y divisiones con números imaginarios, pero antes debes saver algunas cosas
		1.La letra que usaremos para expresar un numero imaginarios sera I mayuscula

		2.Para asignar el coeficiente al numero imaginario se usa un asterisco *
		Ejemplo:2+3*I
		En este caso el coeficiente de I es 3

		3.Para poder indicar el exponente de I deberas usar dos astericos
		Ejemplo:3+6*I**2
		En este caso el exponente de I es 2

		4.Para la multiplicacion de dos numeros imaginarios es necesario encerrar con parentesis cada numero imaginario y usar * mara muliplicarlos
		Ejemplo:(2+8*I)*(9+12*I)

		5.Para realizar una division deberas encerrar con parentesis cada numero imaginario
		Ejemplo: (8+9*I**3)/(10+12*I**4)""")

		simplify(input("Escribe la operacion que deseas realizar: \t "))

		input("\npulsa una tecla para continuar")
	elif opcionMenu=="4":
		break
	else:

		input("pulsa una tecla para continuar")
