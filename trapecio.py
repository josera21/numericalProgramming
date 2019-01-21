import math
import numpy as np

def function(x):
  return (1.0 / math.sqrt(2.0*(math.pi))) * math.exp(-0.5*(x**2.0))

def distribucionNormal(p,n):
  tabla = np.zeros( (35,3) )
  # error = np.zeros( (35,1) )
  # tabintegral = np.zeros( (35,1) )

  for i in range(0,35):
    tabla[i,0] = 21
    tabla[i,1] = 22
    tabla[i,2] = 23

  print ""
  print tabla

if __name__ == '__main__':
  distribucionNormal(1,1)