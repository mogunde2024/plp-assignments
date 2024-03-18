#creating Functions & Fibonacci Sequence
def fibonacci(n): 
    """
  This function generates the Fibonacci sequence up to a specified term n using iteration.

  Args:
      n: The number of terms in the Fibonacci sequence.

  Returns:
      A list containing the Fibonacci sequence up to n terms.
  """
    
    sequence = [0, 1]
    #using for loop to generate the fibonacci sequence and appending to the list
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence
#prompting user input
n = int(input("Enter the value of n: \n"))
print(fibonacci(n))