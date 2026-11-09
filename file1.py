def count_digits(s):
    """Counts and returns the number of digits in a given string."""
    return sum(1 for char in s if char.isdigit())