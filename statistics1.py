import math

def mean(data):
    """Calcula la media de un conjunto de datos."""
    return sum(data) / len(data)

def variance(data):
    """Calcula la varianza de un conjunto de datos."""
    mean_value = mean(data)
    return sum((x - mean_value)**2 for x in data) / len(data)

def standard_deviation(data):
    """Calcula la desviación estándar de un conjunto de datos."""
    return math.sqrt(variance(data))

def correlation_coefficient(x, y):
    """Calcula el coeficiente de correlación de Pearson."""
    mean_x = mean(x)
    mean_y = mean(y)
    numerator = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
    denominator = math.sqrt(sum((xi - mean_x)**2 for xi in x) * sum((yi - mean_y)**2 for yi in y))
    return numerator / denominator
