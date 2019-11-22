# linear é mais rápido
#
# Se  A ~ N²(muA, S) e B ~ N²(muB, S) então a fronteira de decisão é uma reta
#
# Se  fronteira de decisão for dita como linear, isso é uma aproximação
# Essa conta é feita de forma muito rápida, já que segue a formula simples de uma reta: y = ax + b
# um problema é linearmente separável se uma reta consegue separar duas classes de forma perfeita (eg porta lógica AND)
# se o problema for n linearmente separável, pode-se calcular o grau do erro

# 1. Encontrar coordenadas dos centros
# 2. Tirar equação da reta que passa pelos centros
# 3. Encontrar o ponto médio dos dois pontos 
# 4. Encontrar a reta perpendicular à reta inicial e que passe pelo ponto médio

plot(1, type = 'n', xlim = c(0,10), ylim = c(0,10))

p1 = list(x = sample(0:10,1),y = sample(0:10,1))
p2 = list(x = sample(0:10,1),y = sample(0:10,1))

pm = list(x = (p1$x + p2$x)/2, y = (p1$y + p2$y)/2)

points(x = p1$x, y = p1$y, col = 'blue')
points(x = p2$x, y = p2$y, col = 'green')
points(x = pm$x, y = pm$y, col = 'red')

# abline(a = (p1$y - ((p2$y - p1$y)/(p2$x - p1$x))*p1$x), b = ( (p2$y - p1$y)/(p2$x - p1$x) ), col = 'purple')

abline(a = pm$y +  ( (p2$x - p1$x)/(p2$y - p1$y) )*pm$x , b = -(p2$x - p1$x)/(p2$y - p1$y), col = 'red'  )
