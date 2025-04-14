import math

def approximate_ln1x(x, precision, max_terms):
    if not (-1 < x <= 1):
        raise ValueError("x must be between -1 and 1 (excluding -1), inclusive of 1.")

    term = x
    total: float = x
    n: int = 1
    terms_used: int = 1
    prev_total = 0

    print(f"Term {n}: {term:.10f}, Running Total: {total:.10f}, Change: {abs(total - prev_total):.10f}")

    while abs(total - prev_total) >= precision and terms_used < max_terms:
        prev_total = total
        n += 1
        term: float = ((-1) ** (n + 1)) * (x ** n) / n
        total += term
        terms_used += 1
        print(f"Term {n}: {term:.10f}, Running Total: {total:.10f}, Change: {abs(total - prev_total):.10f}")

    # Summary
    exact_value = math.log(1 + x)
    difference = abs(total - exact_value)

    print("\n................. Summary .................")
    print(f"Approximation of ln(1 + {x}): {total}")
    print(f"Exact value using math.log: {exact_value}")
    print(f"Difference from exact value: {difference}")
    print(f"Number of terms used: {terms_used}")


# Example usage
try:
    x = float(input("Enter a value for x (-1 < x ≤ 1): "))
    precision = float(input("Enter desired precision (e.g., 0.000001): "))
    max_terms = int(input("Enter maximum number of terms: "))
    approximate_ln1x(x, precision, max_terms)
except Exception as e:
    print("Error:", e)
