def fib(n):
    """
    This function iterates through the Fibonacci sequence and
    prints each number up to the provided limit (n).
    """

    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


def fib2(n):
  """Calculates the Fibonacci sequence up to a specified limit (n) 
  and returns it as a list of numbers.

  Args:
      n (int): The upper limit for the Fibonacci sequence.

  Returns:
      list: A list containing the Fibonacci numbers up to n.
  """
  result = []
  a, b = 0, 1
  while a < n:
    result.append(a)
    a, b = b, a + b
  return result
