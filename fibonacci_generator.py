#Create a function for the Fibonnaci generation
def fibonacci_generator():
    a, b = 0, 1
    yield a

    while True:
        a, b = b, a + b
        yield a

try:
    # Create an instance of the generator
    fib_gen = fibonacci_generator() 
    num_terms = int(input("Enter the range:")) #Get the range from user
    fib_sequence = []
except ValueError:
    print("Please enter Whole numbers.")

print(f"Generating the first {num_terms} Fibonacci numbers:")

for _ in range(num_terms):
    # next() calls the generator until it yields a value
    fib_number = next(fib_gen)
    fib_sequence.append(fib_number)
    print(fib_number)
