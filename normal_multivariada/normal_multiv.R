# install.packages('plotly')

library(LaplacesDemon)
library(plotly)
library(MASS)

f1 = list(mean = matrix(c(2,1)), S = matrix(c(2,1,1,2),2,2) )
f2 = list(mean = matrix(c(0,0)), S = matrix(c(1,3/5,3/5,2),2,2) )
f3 = list(mean = matrix(c(3,2)), S = matrix(c(1,0,0,1),2,2) )


normal_multivar = function(vals, mean, S){
    # extrair dimensão k
    k = dim(vals)[1]
    p1 = (2*pi)**(-k/2)

    # calcular  a determinante da matriz de covariancia 
    detm = det(S)
    p2 = detm**(-1/2)
    # calcular a matriz inversa da matriz de cov
    dif = (vals - mean)
    p3 = exp( (-0.5*t(dif)%*%ginv(S))%*%dif )
    
    return(p1*p2*p3)
}


vals = matrix(c(2,-2))
res = normal_multivar(vals, f1$mean, f1$S)

# # testing with library
# dmvt(c(vals), c(f1$mean),f1$S)

# plotting
n = 200
seq1 = seq(-5,5, length = n)
seq2 = seq(-5,5, length = n)

A = matrix(0,ncol = n, nrow = n)
B = matrix(0,ncol = n, nrow = n)
C = matrix(0,ncol = n, nrow = n)
for(i in 1:length(seq1)){
    for(j in 1:length(seq2)){
        A[i,j] =  normal_multivar( matrix(c(seq1[i],seq2[j])) , f1$mean, f1$S )
        B[i,j] =  normal_multivar( matrix(c(seq1[i],seq2[j])) , f2$mean, f2$S )
        C[i,j] =  normal_multivar( matrix(c(seq1[i],seq2[j])) , f3$mean, f3$S )
    }
}

image( seq1, seq2, A, col=heat.colors(20) )
contour( seq1, seq2 , A, add = T)
image( seq1, seq2, B, col=heat.colors(20) )
contour( seq1, seq2 , B, add = T)
image( seq1, seq2, C, col=heat.colors(20) )
contour( seq1, seq2 , C, add = T)

# plotting curve level
x11()
contour( seq1, seq2 , A, add = F, col='magenta')
contour( seq1, seq2 , B, add = T, col='blue')
contour( seq1, seq2 , C, add = T, col ='green')

# plotting decision frontier
D = matrix(0, ncol = n, nrow = n)
for(i in 1:length(seq1)){
    for(j in 1:length(seq2)){
        D[i,j] = A[i,j] - B[i,j] - C[i,j]
    }
}
x11()
image(seq1, seq2, D, col = heat.colors(100))
contour(seq1,seq2, D, add = T)

# plotting curve in 2D
par(mfrow = c(1,1))
plot(1, type="n", xlab="", ylab="", xlim=c(0, 40000), ylim=c(0, 0.15))
points(c(A), main = 'function 1', col = 'red', cex = 0.5, pch = 20)
points(c(B), main = 'function 2', col = 'green', cex = 0.5, pch = 20)
points(c(C), main = 'function 2', col = 'blue', cex = 0.5, pch = 20)
