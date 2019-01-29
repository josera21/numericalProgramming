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

tablaDistribucionNormal <- function(n) {
  tnormal = matrix(,nrow=35, ncol=10, byrow=TRUE)

  rownames(tnormal) = seq(0, 3.4, by=0.1)
  colnames(tnormal) = seq(0.0, .09, by=0.01)
  
  t = seq(0, 3.5, 0.1)
  t2 = seq(0.0, .09, .01)

  for (i in 1:35) {
    for (k in 2:10) {
      rtrapecio = trapecio(0,t[i]+t2[k], n, f=fx)
      tnormal[i,k] = round(rtrapecio + 0.5, 4)
    }
    rtrapecio = trapecio(0, t[i], n, f=fx)
    tnormal[i,1] = round(rtrapecio + 0.5, 4)
  }

  tresultados = cbind(tnormal)
  imprimir = list("Tabla Distribucion Normal estandar con Trapecio" = tresultados)

  return (imprimir)
}

ejecutar <- function() {
  opts <- c("Reproducir tabla distribucion normal", "Calcular Probabilidad", "Salir")
  opts2 <- c("Calcular P{X<x}", "Calcular P{a<X<b}")
  salir = FALSE

  while(!salir) {
    opc <- menu(opts, title="Distribucion normal con la Regla del Trapecio")

    if(opc == 1) {
      n = 500 
      resultado <- tablaDistribucionNormal(n)
      print(resultado)
    }
    if(opc == 2) {
      opc2 <- menu(opts2,  title="Elige una opcion")

      if(opc2 == 1) {
        print("Nota: con media = 0 y desviacion estandar = 1")
        x <- as.numeric(readline("Valor de x: "))
        media = 0
        desvStandar = 1
        z = (x-media) / desvStandar
        
        prob = trapecio(0, z, 100, f=dnorm) + 0.5
        
        graficar(prob, z, 100)
        mtext(paste("P(X<x)=",round(prob,4)), adj=1)
        mtext(paste("Para X<=",z, " n=",100), side=3)

        print("--- RESULTADO ---")
        print(paste("P (X<x): ", prob))
        print("-----------------")
      }
      if(opc2 == 2) {
        print("Nota: con media = 0 y desviacion estandar = 1")
        print("P{ a<X<b }")

        a <- as.numeric(readline("Valor de a: "))
        b <- as.numeric(readline("Valor de b: "))
        media = 0
        desvStandar = 1
        a = (a-media) / desvStandar
        b = (b-media) / desvStandar

        prob = trapecio(a, b, 100, f=dnorm)

        graficar(prob, a, 100)
        mtext(paste("P(",a,"<X<",b,")=",round(prob,4)), adj=1)
        mtext(paste("Para P(",a,"<X<",b,")", " n=",100), side=3)

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