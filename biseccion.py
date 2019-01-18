# -*- coding: utf-8 -*-
import math

def biseccion(a, b, tol, n):
	fa = function(a)
	fb = function(b)
	fc = fa
	i = 1

	while i < n and abs(fc) > tol:
		i += 1
		c = (a + b) / 2
		fc = function(c)

		if ((fa * fc) > 0):
			a = c
			fa = fc
		else:
			b = c
			fb = fc

	if fc == 0 or abs(fc) <= tol:
		print "En {0} iteraciones".format(i)
		print "Solución: {0}".format(c)
	else:
		print("Error")

def function(x):
	# Comente o descomente segun la funcion que quiera usar
	# return (-0.4)*(pow(x, 2)) + (2.2)*(x) + 4.7
	return math.exp(-x) - math.log(x)

if __name__ == "__main__":
	biseccion(1, 1.5, 0.001, 30)