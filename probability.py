import numpy as np
from scipy.stats import binom, poisson, norm

def probability(event, space):
    """Calcula la probabilidad de un evento en un espacio muestral."""
    return len(event) / len(space)

def conditional_probability(event, condition):
    """Calcula la probabilidad condicional de un evento dado una condición."""
    return probability(event & condition, condition)

def binomial_distribution(n, p, k):
    """Calcula la probabilidad de k éxitos en una distribución binomial."""
    return binom.pmf(k, n, p)

def poisson_distribution(lam, k):
    """Calcula la probabilidad de k eventos en una distribución Poisson."""
    return poisson.pmf(k, lam)

def normal_distribution(x, mean, std_dev):
    """Calcula la densidad de probabilidad de una distribución normal."""
    return norm.pdf(x, mean, std_dev)

def monte_carlo_simulation(func, num_simulations=10000):
    """Simulación de Monte Carlo para estimar un valor."""
    results = [func() for _ in range(num_simulations)]
    return np.mean(results)
