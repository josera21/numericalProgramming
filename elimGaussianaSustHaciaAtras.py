# -*- coding: utf-8 -*-
import numpy as np

def eliminacionDelante(A, b):
  tamano = A.shape # Tomando la dimension
  n = tamano[0]
  if tamano[0] != tamano[1]:
    print "error"
    return

  naux = n + 1
  Mau = np.c_[A, b] # Construyendo la matriz ampliada
  print "Matriz ampliada"
  print(Mau)

  # Eliminacion hacia adelante
  for k in range(0, n - 1):
    for i in range(k+1, n):
      factor = Mau[i,k] / Mau[k,k]
      print "Factor {}".format(factor)
      Mau[i, k:naux] = Mau[i, k:naux] - factor * Mau[k, k:naux]

      print("i",i)
      print("k", k)
      print(Mau) #impirmr matriz

  x = []
  for zero in range(0, n):
    x.append(0)

  x[n - 1] = Mau[n - 1,naux - 1] / Mau[n - 1,n - 1]

  # Sustitucion hacia atras
  for i in reversed(range(n-1)):
    x[i] = ( Mau[i, naux - 1] - sum(Mau[i, (i+1):n] * x[(i+1):n]) ) / Mau[i,i]
  
  return x

if __name__ == "__main__":
  # Cada primer valor de cada array, representa la primera fila, y asi respectivamente con los demas elementos
  # Para las otras filas.
  # A = np.array([[255, 0, -225, 0], [0, 175, 0, 25], [-25, 0, 275, 250], [0, 125, -50, -275]])
  # b = np.array([1400, 100, 2000, 0])
  # A = np.array([[1, 1, 0, 3], [2, 1, -1, 1], [3, -1, -1, 2], [-1, 2, 3, -1]])
  # b = np.array([4, 1, -3, 4])
  A = np.array([[3.03, 12.1, 14], [-3.03, 12.1, -7], [6.11, -14.2, 21]])
  b = np.array([-119, 126, -134])
  x = eliminacionDelante(A, b)
  print "Solucion final: {}".format(x)