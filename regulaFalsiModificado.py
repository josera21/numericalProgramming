# -*- coding: utf-8 -*-

def regulaFalsiModificado(a, b, tol, n):
	fa = function(a)
	fb = function(b)
	fc = fa
	c = a
	ant = float("inf") # Para la primera iteracion
	i = 0
	ia = 0
	ib = 0

	while i < n and abs(c - ant) > tol:
		i += 1
		ant = c
		c = b - fb*((b - a) / (fb - fa))
		fc = function(c)

		if ((fa * fc) > 0):
			a = c
			fa = fc
			ia = 0
			ib += 1

			if ib >= 2:
			 	fb = fb / 2

		else:
			b = c
			fb = fc
			ib = 0
			ia += 1

			if ia >= 2:
				fa = fa / 2

	if abs(c - ant) <= tol:
		print "En {0} iteraciones".format(i)
		print "Solución: {0}".format(c)
	else:
		print("Error")

def function(x):
	# Comente o descomente segun la funcion que quiera usar
	return (-0.4)*(pow(x, 2)) + (2.2)*(x) + 4.7

def capturarDatos():
	print("-- Inserte los valores requeridos --")
	a = float(raw_input("Valor de a: "))
	b = float(raw_input("Valor de b: "))
	tol = float(raw_input("Tolerancia: "))
	n = float(raw_input("Cantidad maxima de iteraciones: "))
	regulaFalsiModificado(a, b, tol, n)

if __name__ == "__main__":
	resp = raw_input("¿ Desea colocar sus propios datos ? S/N: ")
	if resp.lower() == "s":
		capturarDatos()
	else:
		regulaFalsiModificado(-2, 1.5, 0.05, 30)