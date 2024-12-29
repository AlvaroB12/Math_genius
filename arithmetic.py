import math

def add(num1, num2):
  return num1 + num2

def substract(num1, num2):
  return num1 - num2

def multiply(num1, num2):
  return num1 * num2

def divide(num1, num2):
  if b == 0:
    raise ZeroDivisionError('Can\'t divide by zero.')
  return a / b

def power(base, exponent):
    """Calcula la potencia base^exponent."""
    return base ** exponent

def root(n, degree):
    """Calcula la raíz n-ésima de un número."""
    return n ** (1 / degree)

def gcd(a, b):
    """Calcula el máximo común divisor (MCD) de dos números."""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Calcula el mínimo común múltiplo (MCM) de dos números."""
    return abs(a * b) // gcd(a, b)

def is_prime(n):
    """Verifica si un número es primo."""
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def nth_fibonacci(n):
    """Calcula el n-ésimo número de Fibonacci."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a