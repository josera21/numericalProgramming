# -*- coding: utf-8 -*-
import numpy as np

def eliminacionAtras(A, b):
  tamano = A.shape # Tomando la dimension
  n = tamano[0]
  if tamano[0] != tamano[1]:
    print "error"
    return

  naux = n + 1
  Mau = np.c_[A, b] # Construyendo la matriz ampliada
  print "Matriz ampliada"
  print(Mau)

  # Eliminacion hacia atras
  for k in reversed(range(1,n)):
    for i in reversed(range(k)):
      factor = Mau[i,k] / Mau[k,k]
      print "Factor {}".format(factor)
      Mau[i, 0:naux] = Mau[i, 0:naux] - factor * Mau[k, 0:naux]
  
  print(Mau)
  
  x = []
  for zero in range(0, n):
    x.append(0)

  x[0] = Mau[0,naux - 1] / Mau[0,0]

  # Sustitucion hacia adelante
  for i in range(1,n):
    x[i] = ( Mau[i, naux - 1] - sum(Mau[i, 0:i] * x[0:i]) ) / Mau[i,i]
  
  return x
  

if __name__ == "__main__":
  # Cada primer valor de cada array, representa la primera fila, y asi respectivamente con los demas elementos
  # Para las otras filas.
  # A = np.array([[255, 0, -225, 0], [0, 175, 0, 25], [-25, 0, 275, 250], [0, 125, -50, -275]])
  # b = np.array([1400, 100, 2000, 0])
  # A = np.array([[1, 1, 0, 3], [2, 1, -1, 1], [3, -1, -1, 2], [-1, 2, 3, -1]])
  # b = np.array([4, 1, -3, 4])
  A = np.array([[2, -1, 1], [3, 3, 9], [3, 3, 5]], dtype=float)
  b = np.array([-1, 0, 4], dtype=float)
  x = eliminacionAtras(A, b)
  print "Solucion final: {}".format(x)