from math import e,pi

def standard(x,media,desvStandar):
  return (x-media)/desvStandar

def distribucion_normal(x,media,desvStandar):
  Z = standard(x,media,desvStandar)
  resultado = (e**((-Z**2.0)/2.0))/(2.0*pi)**0.5
  return resultado

def simpson(media, desvStandar, n, b, a=float('-inf')):
  flagB= False
  flagA= False
  if a == float('-inf'):
    a = 0
    flagA = True
    if b < 0:
      b=-b
      flag = True

  h=(b-a)/n
  valor = distribucion_normal(a,media,desvStandar) #x0
  for i in range(2,n-1,2):
    x=a+i*h
    valor += 2*distribucion_normal(x,media,desvStandar)
  for i in range(1,n,2):
    x=a+i*h
    valor += 4*distribucion_normal(x,media,desvStandar)
  valor += distribucion_normal(b,media,desvStandar) #xn
  valor *= (h/3)
  
  if flagA:
    if flagB:
      valor = -valor
    valor += 0.5
      
  return round(valor, 4)
    

def funcion_uno():
  """ Calcular P {X<x} """
  print("Nota: con media = 0 y desviacion standar = 1")
  x = float(raw_input("Valor de x: "))

  print("-- RESULTADO --")
  print("P(X<=x) simple: " + str(simpson(0,1.0,2,x)))
  print("P(X<=x) compuesta: " + str(simpson(0,1.0,40,x)))


def funcion_dos():
  """ Calcular P {a<X<b} """
  print("Nota: con media = 0 y desviacion standar = 1")
  a = float(raw_input("Valor de a: "))
  b = float(raw_input("Valor de b: "))

  print("-- RESULTADO --")
  print("P(a<=X<=b) simple: " + str(simpson(0,1.0,2,b,a)))
  print("P(a<=X<=b) Compuesta: " + str(simpson(0,1.0,40,b,a)))

def ejecutar():
  salir = False
  mensaje = 'Ingrese la opcion deseada. Escriba "exit" para salir'
  encabezado = 'Calculos de probabilidad con la Regla de Simpson'

  menu = { 'a' : funcion_uno, 'b' : funcion_dos }
  # Mientras salir sea falso
  while not salir: 
    print('-' * len(encabezado))
    print(encabezado.upper())
    print('-' * len(mensaje))
    print(mensaje)

    for opcion, funcion in menu.items():
      mensaje_final = '{}) {}'.format(opcion, funcion.__doc__)
      print(mensaje_final)

    respuesta = raw_input('\nOpcion : ').lower()
    salir = respuesta == 'exit'
    # Si la respuesta no existe, le paso none
    funcion = menu.get(respuesta, None)
    if funcion:
      funcion()


  else:
    print("Adios.")

if __name__ == '__main__':
  ejecutar()