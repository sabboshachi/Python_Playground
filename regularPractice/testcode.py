# Function to find the sum of an arithmetic series
def arithmetic_series_sum(a, d, n):
    """
    a: the first term of the series
    d: the common difference between terms
    n: the number of terms to sum
    """
    # Calculate the sum of the series using the formula
    series_sum = (n / 2) * (2 * a + (n - 1) * d)
    return series_sum

# Example usage
a = 1 # first term
d = 3 # common difference between terms
n = 5 # number of terms to sum
sum_of_series = arithmetic_series_sum(a, d, n)
print(f"The sum of the arithmetic series starting at {a}, with a common difference of {d} and {n} terms is {sum_of_series}.")
