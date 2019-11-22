# gerando dados (pra simulações) com distro gaussiana normal 
x = seq(-10,10, len=100)
y =  dnorm(x, mean=-1.5, sd = 2.1)

plot(x,y, col='red', type='lines')
abline(v=-1.5, col='blue')

X = rnorm(30,mean=-1.5, sd = 2.1)
rug(X, col='black')


muX = mean(X)
sdX = sd(X)

yAprendidoDosDados = dnorm(x, mean=muX, sd = sdX)
points(x, yAprendidoDosDados, col = 'green', type = 'lines')

# com muitos dados
XX = rnorm(10**(4), mean = -1.5, sd = 2.1)
muXX = mean(XX)
sdXX = sd(XX)
yAprendidoDosMuitodDados = dnorm(x, mean=muXX, sd = sdXX)
points(x, yAprendidoDosMuitodDados, col = 'purple', type = 'lines')

hist(XX, br = 100, col='pink')


library(MASS)
Sigma = matrix(c(10,3,3,2),2,2)
mu = c(2,2)
X = mvrnorm(n=1000,rep(0,2),Sigma)
plot(X)

muAprendido =  apply(X, 2, mean)
sdAprendido =  apply(X, 2, sd)


# simulando gaussiana 5D
# a verdade:
mu = c(10, 0.5, -200, 34.5, 0)
Sigma = matrix(c(2,0,0,0,0,    0,1,0,0,0,    0,0,150,0,0,    0,0,0,1,0,    0,0,0,0,10.1), nrow = 5, ncol = 5)

S = Sigma
S[1,4] = -1
S[4,1] = -1
S[3,5] = 2.3
S[5,3] = 2.3

A = mvrnorm(10**(2), mu, S)

# reconstruindo
muChapeu = apply(A, 2, mean)

round(cov(A),1) 
S

round(cov(A),1) - S 



# gerando duas nuvens A e B separadas

library(MASS)
plot(1, type = 'n', xlim = c(-10,10), ylim = c(-10,10))

Sigma = matrix(c(10,3,3,2),2,2)
muA = c(-2,1)
XA = mvrnorm(n=100,Sigma, mu = muA)
points(XA, col = 'red')


Sigma = matrix(c(5/2,1,1,5/2),2,2)
muB = c(3,-3)
XB = mvrnorm(n=100,mu = muB, Sigma)
points(XB, col = 'blue')

linear_separation(muA,muB)

linear_separation <- function(c1,c2, draw_centroids = FALSE){
  p1 = list(x = c1[1],y = c1[2])
  p2 = list(x = c2[1],y = c2[2])
  pm = list(x = (p1$x + p2$x)/2, y = (p1$y + p2$y)/2)
  
  if(draw_centroids){
    points(x = p1$x, y = p1$y, col = 'red')
    points(x = p2$x, y = p2$y, col = 'blue')
    points(x = pm$x, y = pm$y, col = 'purple')
  }
  
  # abline(a = (p1$y - ((p2$y - p1$y)/(p2$x - p1$x))*p1$x), b = ( (p2$y - p1$y)/(p2$x - p1$x) ), col = 'purple')
  
  abline(a = pm$y +  ( (p2$x - p1$x)/(p2$y - p1$y) )*pm$x , b = -(p2$x - p1$x)/(p2$y - p1$y), col = 'purple'  )
}

linear_separation(muA,muB)

