import numpy as np
import matplotlib.pyplot as plt
import decimal

def interpolacion_newton(x, y, numEvaluar):
	# Para precision en los calculos
	decimal.getcontext().rounding = decimal.ROUND_DOWN

	if len(x) != len(y):
		print "error!"
	
	n = len(x)
	A = np.zeros( (n,n) )
	A[0:n, 0] = y

	for i in range(1,n):
		for k in range(0, n-i):
			a = decimal.Decimal(A[k+1,i-1])
			b = decimal.Decimal(A[k,i-1])
			A[k,i] = ( round(a, 8) - round(b, 8) ) / ( x[k+i] - x[k] )
			print A

	print '** TABLA DE DIFERENCIAS FINITAS **'
	print A

	coeficientes = []
	for i in range(0,n):
		bi = decimal.Decimal(A[0,i])
		coeficientes.append(round(bi, 8))
	print('COEFICIENTES DEL POLINOMIO: ', coeficientes)
	
	valorInterpolado = coeficientes[0]

	for i in range(1,n):
		base = 1
		for k in range(0,i):
			base = decimal.Decimal(( numEvaluar - x[k] ) * base)
			base = round(base, 8)
			print('base', base)
		
		cal =  decimal.Decimal(coeficientes[i]*(base))
		valorInterpolado += round(cal,8)

	return valorInterpolado
			

def graficar(xOri, yOri, xDado, yInter):
	plt.plot(xOri, yOri, 'b--', [xDado], [yInter], 'ro')
	# plt.axis([1, 1.6, 0, 1])
	plt.annotate('Aproximacion', xy=(xDado, yInter), xytext=(1.1,0.96), arrowprops=dict(facecolor='black', shrink=0.05))
	plt.show()
	

if __name__ == '__main__':
	X = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5]
	Y = [0.8427, 0.8802, 0.9103, 0.9340, 0.9523, 0.9661 ]
	resultado = interpolacion_newton(X, Y, 1.32)
	print 'RESULTADO'
	print resultado
	graficar(X, Y, 1.32, resultado)