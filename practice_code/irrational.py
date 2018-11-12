class Irrational:
    def __init__(self, iterations):
        self.iterations = iterations
        pass

    def _factorial(self, n):
        if n < 1:
            return 1
        else : 
            return (n * self._factorial(n-1))
    def e(self, places):
        #2.71828
        e = 0
        for number in range(0,places):
            e = e + 1/self._factorial(number)
        return e
irrational = Irrational(1000)
print(irrational.e(100))