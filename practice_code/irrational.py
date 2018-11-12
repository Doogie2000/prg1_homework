def _factorial(n):
    if n < 1:
        return 1
    else : 
        return (n * _factorial(n-1))
