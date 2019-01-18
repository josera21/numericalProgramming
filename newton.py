# -*- coding: utf-8 -*-
import math

def newton(x, tol, n):
	xa = float("inf") # Numero infinito para la primera iteracion
	i = 0
	
	while i < n and abs(x - xa) > tol:
		i += 1
		xa = x
		x = xa - (function(xa) / derivada(xa))

	if abs(x - xa) <= tol:
		print "En {0} iteraciones".format(i)
		print "Solucion: {0}".format(x)
	else:
		print("Error")

def function(x):
	# Comente o descomente segun la funcion que quiera usar
	return (-0.4)*(pow(x, 2)) + (2.2)*(x) + 4.7
	# return 12 * (1 - math.exp(-0.04*x)) + 5 * (math.exp(-0.04*x)) - (85/100)*12

def derivada(x):
	# Comente o descomente segun la funcion que quiera usar
	# OJO: Debe coincidir la derivada con la funcion que defina en el metodo function
	return -0.8*(x) + 6.9
	# return (12*0.04)*math.exp(-0.04*x) - 5*0.04*(math.exp(-0.04*x))

if __name__ == "__main__":
	# Colocar: valor inicial, tolerancia, tope maximo de iteraciones
	newton(-1.65, 0.001, 30)