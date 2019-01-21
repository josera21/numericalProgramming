fx <- function(x) {
  return (1 / sqrt(2*pi)) * exp(-0.5*(x^2))
}

trapecio <- function(a, b, n) {
  c <- numeric(n+1)
  d <- numeric(1)
  X <- numeric(n+1 )

  if (n == 1) {
    h <- (b -a)
    
    for (i in 1:(n+1)) {
      X[i] <- a + (i-1)*h
      c[i] <- fx(X[i])
    }
    integral <- (h/2) * (c[1] + c[n+1])
  } else {
    h <- (b-a)/n
    
    for(i in 1:(n+1)) {
      X[i] <- a+(i-1)*h
      c[i] <- fx(X[i])
    }
    for(i in 2:n) {
      d <- d + c[i]
    }
    integral <- (h/2) * (c[1] + 2*d + c[n+1])
  }

  return (integral)
}

distribucionNormal <- function(p, n) {
  tnormal = matrix(, 35, 1)
  terror = matrix(, 35, 1)
  tintegral = matrix(, 35, 1)

  rownames(tnormal) <- seq(0, 3.4, 0.1)
  colnames(tnormal) <- c("R")
  colnames(terror) <- c("Error")
  colnames(tintegral) <- c("Integral")
  t <- seq(0, 3.5, 0.1)

  for (i in 1:35) {
    rtrapecio <- trapecio(0, t[i], n)
    tnormal[i,] <- rtrapecio + 0.5
    terror[i,] <- (tnormal[i] - rtrapecio) / tnormal[i]
    tintegral[i,] <- rtrapecio
  }

  if(p < 0) {
    prob <- trapecio(0, p, n)
  } else if(p > 3.4) {
    prob <- 1
  } else {
    prob <- trapecio(0, p, n) + 0.5
  }

  tresultados <- cbind(tnormal, terror, tintegral)
  imprimir <- list("Tabla Normal estandar con Trapecio" = tresultados, "Probabilidad P(X<x) " = prob)

  return (imprimir)
}

p = 2.5
n = 10 
resultado <- distribucionNormal(p,n)
resultado