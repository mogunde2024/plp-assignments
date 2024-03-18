#creating Functions & Fibonacci Sequence
def fibonacci(n):
    sequence = [0, 1]
    #using for loop to generate the fibonacci sequence and appending to the list
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence
#prompting user input
n = int(input("Enter the value of n: \n"))
print(fibonacci(n))