library(MASS)

f1 = list(mu = 0, sigma = 1, col = 'red')
f2 = list(mu = 1, sigma = 2, col = 'green')

normal_1d = function(vals, mu=0, sigma=1) {
    res = c()
    for(x in vals){
        p1 = 1/(sigma*sqrt(2*pi))
        p2 = exp(-0.5*((x - mu)**2/sigma**2))
        
        res = c(res,p1*p2)
    }
    return(res)
}

insertPoint = function(p){
    if(normal_1d(p, f1$mu, f1$sigma) < normal_1d(p, f2$mu, f2$sigma)){
        points(p,0, col=f2$col, cex = 0.5, pch = 20,)
    } else if(normal_1d(p, f1$mu, f1$sigma) > normal_1d(p, f2$mu, f2$sigma)){
        points(p,0, col=f1$col, cex = 0.5, pch = 20,)
    } else {
        print(p)
        points(p,0, col='black', cex = 0.5, pch = 20)
    }
    
}

# testing one variable normal plot:
vals = seq(-5, 5, length=1000)

plot(1, type="n", xlab="", ylab="", xlim=c(-5, 5), ylim=c(0, 0.5))

lines(vals, normal_1d(vals, f1$mu, f1$sigma), lwd=1, col=f1$col)
lines(vals, normal_1d(vals, f2$mu, f2$sigma), lwd=1, col=f2$col)

for(i in seq(-5,5,by=0.001)){
    insertPoint(i)    
}

# points(1,0.4, cex = 0.5, pch = 20, col = 'red')
