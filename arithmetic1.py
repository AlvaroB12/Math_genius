from math import *

def add(num1, num2):
  return num1 + num2

def substract(num1, num2):
  return num1 - num2

def multiply(num1, num2):
  return num1 * num2

def divide(num1, num2):
  if num2 == 0:
    raise ZeroDivisionError('Can\'t divide by zero.')
  return num1 / num2

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
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def nth_fibonacci(n):
    """Calcula el n-ésimo número de Fibonacci."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def divisors(n):
    """Devuelve los divisores de un número entero."""
    return [i for i in range(1, n + 1) if n % i == 0]

def prime_factorization(n):
    """Devuelve la factorización en primos de un número."""
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    return factors

def modular_inverse(a, m):
    """Calcula el inverso modular de a módulo m."""
    for x in range(1, m):
        if (a * x) % m == 0:
            return x
    return None

def chinese_remainder_theorem(n, a):
    """Teorema chino del resto."""
    p = prod(n)
    result = 0
    for n_i, a_i in zip(n, a):
        p_i = p // n_i
        result += a_i * modular_inverse(p_i, n_i) * p_i
    return result % p

def prod(arr):
    """Calcula el producto de los elementos de un arreglo."""
    p = 1
    for x in arr:
        p *= x
    return p

def is_palindrome(n):
    """Verifica si un número es palíndromo."""
    return str(n) == str(n)[::-1]

def is_armstrong(n):
    """Verifica si un número es de Armstrong."""
    return n == sum([int(x) ** len(str(n)) for x in str(n)])

def is_perfect(n):
    """Verifica si un número es perfecto."""
    return n == sum(divisors(n)[:-1])

def is_abundant(n):
    """Verifica si un número es abundante."""
    return n < sum(divisors(n)[:-1])

def is_deficient(n):
    """Verifica si un número es deficiente."""
    return n > sum(divisors(n)[:-1])

def is_pandigital(n):
    """Verifica si un número es pandigital."""
    return set(str(n)) == set('123456789')

def is_harshad(n):
    """Verifica si un número es Harshad."""
    return n % sum([int(x) for x in str(n)]) == 0

def is_pronic(n):
    """Verifica si un número es prónico."""
    return n == int(sqrt(n)) * (int(sqrt(n)) + 1)

def is_amicable(a, b):
    """Verifica si dos números son amigables."""
    return sum(divisors(a)[:-1]) == b and sum(divisors(b)[:-1]) == a

def factorial(n):
    """Calcula el factorial de un número."""
    return 1 if n == 0 else n * factorial(n - 1)
