# -*- coding: utf-8 -*-

def secante(a, b, tol, n):
	fa = function(a)
	fb = function(b)
	fc = fa
	i = 1

	while i < n and fc != 0 and (abs(b - a) / 2) > tol:
		i += 1
		c = b - fb * ((b - a) / (fb - fa))
		fc = function(c)
		a = b
		fa = fb
		b = c
		fb = fc

	if fc == 0 or (abs(b - a) / 2) <= tol:
		print "En {0} iteraciones".format(i)
		print "Solución: {0}".format(c)
	else:
		print("Error")

def function(x):
	# Comente o descomente segun la funcion que quiera usar
	return (-0.4)*(pow(x, 2)) + (2.2)*(x) + 4.7


if __name__ == "__main__":
	secante(-2, 1.5, 0.05, 30)