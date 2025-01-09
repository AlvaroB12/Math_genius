from itertools import *

def union(set1, set2):
    """Devuelve la unión de dos conjuntos."""
    return set1 | set2

def intersection(set1, set2):
    """Devuelve la intersección de dos conjuntos."""
    return set1 & set2

def difference(set1, set2):
    """Devuelve la diferencia de dos conjuntos (set1 - set2)."""
    return set1 - set2

def symmetric_difference(set1, set2):
    """Devuelve la diferencia simétrica de dos conjuntos."""
    return set1 ^ set2

def is_subset(set1, set2):
    """Devuelve True si set1 es un subconjunto de set2."""
    return set1 <= set2

def is_superset(set1, set2):
    """Devuelve True si set1 es un superconjunto de set2."""
    return set1 >= set2

def is_disjoint(set1, set2):
    """Devuelve True si set1 y set2 son conjuntos disjuntos."""
    return set1.isdisjoint(set2)

def cartesian_product(set1, set2):
    """Devuelve el producto cartesiano de dos conjuntos."""
    return {(a, b) for a in set1 for b in set2}

def power_set(s):
    """Devuelve el conjunto potencia de un conjunto."""
    return {frozenset(c) for c in chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))}

def set_partition(s):
    def set_partition(s):
        """Devuelve todas las particiones de un conjunto."""
        if not s:
            return {frozenset()}
        result = set()
        for i in range(1, len(s)):
            for subset in combinations(s, i):
                subset = frozenset(subset)
                for partition in set_partition(s - subset):
                    result.add(frozenset([subset]) | {frozenset(partition)})
        return result
    return set_partition(frozenset(s))

def set_cardinality(s):
    """Calcula la cardinalidad de un conjunto."""
    return len(s)

def set_complement(universe, s):
    """Calcula el complemento de un conjunto."""
    return universe - s