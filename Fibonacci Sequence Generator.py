print("Fibonacci Sequence Generator as 4th Beginner Project")

def fibonacci_sequence(n):
    """
    Generates the Fibonacci sequence up to the nth term.
    Args:
        n (int): The number of terms in the sequence to generate.
    Returns:
        list: The Fibonacci sequence up to the nth term.
    """
    # Initialize the sequence with the first two terms
    sequence = [0, 1]

    # Generate the next terms in the sequence using a loop
    for i in range(2, n):
        # Calculate the sum of the previous two terms
        next_term = sequence[i - 1] + sequence[i - 2]

        # Add the next term to the sequence
        sequence.append(next_term)

    return sequence

series = fibonacci_sequence(10)
print(series)