class Teste():
    def __init__(self, x):
        self.x = x          # public
        self._x1 = x**2     # protected
        self.__x2 = x**3    # privated

    def getx2(self):
        return (self.__x2)

t = Teste(2)

print(t.x)
print(t._x1)
print( t.getx2() )
