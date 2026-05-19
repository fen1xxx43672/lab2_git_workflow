def add(a: float, b: float) -> float:
    """Return sum of a and b."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Arguments must be numbers")
    return a + b

def subtract(a: float, b: float) -> float:
    """Return difference of a and b."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Arguments must be numbers")
    return a - b
