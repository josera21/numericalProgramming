# -*- coding: utf-8 -*-
import numpy as np

def DescomposicionLU(A, b):
  U = A
  dim = U.shape
  n = dim[0]
  L = np.diag( np.ones( (n,), dtype=float ) ) # Diagonal principal con 1
  print("Matriz inicial")
  print(U)
  # Contruyendo U y L
  for k in range(0, n -1):
    for i in range(k+1, n):
      factor = U[i, k] / U[k, k]
      L[i,k] = factor
      U[i, k:n] = U[i, k:n + 1] - factor*U[k, k:n + 1]
      print("U")
      print(U)
      print("L")
      print(L)

  # Vector solucion y
  y = np.zeros( (n,), dtype=float )
  y[0] = b[0]

  for i in range(1, n):
    y[i] = ( b[i] - sum(L[i, 0:(i)] * y[0:(i)]) ) / L[i,i]

  print "y: {}".format(y)

  # Vector solucion x
  x = np.zeros( (n,), dtype=float )
  x[n-1] = y[n-1] / U[n-1,n-1]

  for i in reversed(range(n-1)):
    x[i] = ( y[i] - sum(U[i,(i+1):n] * x[(i+1):n]) ) / U[i,i]

  return x

if __name__=="__main__":
  A = np.array([ [2, -1, 1], [3, 3, 9], [3, 3, 5] ], dtype=float)
  b = np.array([-1, 0, 4], dtype=float)
  x = DescomposicionLU(A, b)
  result = np.array(x, dtype=int)
  print "Solucion es: {}".format(x)