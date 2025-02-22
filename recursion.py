def fibonacci_rec(n, a=0, b=1):
    if n <= 0:
        return
    print(a, end=" ")
    fibonacci_rec(n - 1, b, a + b)

def sumar_elementos_rec(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + sumar_elementos_rec(arr[1:])

def multiplicar_rec(a, b):
    if b < 0:
        return -multiplicar_rec(a, -b)
    if b == 0:
        return 0
    return a + multiplicar_rec(a, b - 1)

def dividir_rec(dividendo, divisor):
    if divisor == 0:
        raise ValueError("No se puede dividir entre cero.")
    
    negativo = (dividendo < 0) ^ (divisor < 0)
    
    dividendo = abs(dividendo)
    divisor = abs(divisor)
    
    def helper(d, s):
        if d < s:
            return 0
        return 1 + helper(d - s, s)
    
    resultado = helper(dividendo, divisor)
    
    return -resultado if negativo else resultado
