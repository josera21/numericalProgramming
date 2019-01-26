fx <- function(x) {
  (1/sqrt(2*pi))*exp(-0.5*(x^2))
}

graficar <- function(prob, p, n) {
  l=seq(-10,10,0.1)
  x=seq(-4,4,0.1)
  plot(x,fx(x),type="l",axes=FALSE,xlab="X",ylab="Y",col="1",main="Distribucion Normal Aproximada Con Trapecio")
  axis(1)
  axis(2)
  abline(v=seq(-4,prob,0.001),col="red")
  polygon(c(l,length(prob)),c(dnorm(l),length(prob)),col="white",border="black")
  mtext(paste("P(Z<z)=",prob), adj=1)
  mtext(paste("Para Z<=",p, " n=",n), side=4, adj=1)
}

trapecio <- function(a, b, n, f) {
  c = numeric(n+1)
  d = numeric(1)
  X = numeric(n+1 )

  if (n == 1) {
    h = (b-a)
    
    for (i in 1:(n+1)) {
      X[i] = a + (i-1)*h
      c[i] = f(X[i])
    }
    integral = h/2*(c[1] + c[n+1])
  } else {
    h = (b-a)/n
    
    for(i in 1:(n+1)) {
      X[i] = a+(i-1)*h
      c[i] = f(X[i])
    }
    for(i in 2:n) {
      d = d + c[i]
    }
    integral = h/2*(c[1] + 2*d + c[n+1])
  }

  return (integral)
}

tablaDistribucionNormal <- function(p, n) {
  tnormal = matrix(,nrow=35, ncol=1, byrow=TRUE)
  terror = matrix(,nrow=35, ncol=1, byrow=TRUE)
  tintegral = matrix(,nrow=35, ncol=1, byrow=TRUE)

  rownames(tnormal) = seq(0, 3.4, by=0.1)
  colnames(tnormal) = c("R")
  colnames(terror) = c("Error")
  colnames(tintegral) = c("Integral")
  
  t = seq(0, 3.5, 0.1)

  for (i in 1:35) {
    rtrapecio = trapecio(0, t[i], n, f=fx)
    tnormal[i,] = rtrapecio + 0.5
    terror[i,] = (tnormal[i] - rtrapecio) / tnormal[i]
    tintegral[i,] = rtrapecio
  }

  if(p < 0) {
    prob = trapecio(0, p, n, f=fx)
  } 
  if(p > 3.4) {
    prob = 1
  } else {
    prob = trapecio(0, p, n, f=fx) + 0.5
  }

  graficar(prob, p, n)

  tresultados = cbind(tnormal, terror, tintegral)
  imprimir = list("Tabla Normal estandar con Trapecio" = tresultados, "Probabilidad P(Z<z) " = prob)

  return (imprimir)
}

ejecutar <- function() {
  opts <- c("Reproducir tabla distribucion normal", "Calcular Probabilidad", "Salir")
  opts2 <- c("Calcular P{X<x}", "Calcular P{a<X<b}")
  salir = FALSE

  while(!salir) {
    opc <- menu(opts, title="Ejemplos Distribucion normal con la Regla del Trapecio")

    if(opc == 1) {
      p = 1.1
      n = 500 
      resultado <- tablaDistribucionNormal(p,n)
      print(resultado)
    }
    if(opc == 2) {
      opc2 <- menu(opts2,  title="Elige una opcion para correr el ejemplo")

      if(opc2 == 1) {
        prob = trapecio(0, 5, 100, f=dnorm) + 0.5
        print("--- RESULTADO ---")
        print(paste("P (X<x): ", prob))
        print("-----------------")
      }
      if(opc2 == 2) {
        prob = trapecio(2, 7, 100, f=dnorm)
        print("--- RESULTADO ---")
        print(paste("P (a<X<b): ", prob))
        print("-----------------")
      }
    }
    if(opc == 3) {
      salir = TRUE
    }
  }

}

ejecutar()

#p = 1.1
#n = 500 
#resultado <- tablaDistribucionNormal(p,n)
#resultado
#print("Fin del calculo")