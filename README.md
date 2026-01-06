## 🌀 Infinite Fibonacci Generator:
  A specialized Python implementation that uses Generator Functions to create an infinite Fibonacci sequence. This project serves as a technical deep dive into memory-efficient programming, the `yield` keyword, and manual iteration using the `next()` function.

--

### 🧠 The Core Concept: Why Generators?
In standard Python functions, a `return` statement terminates the function and sends back a complete object (like a list). If you wanted 1 million Fibonacci numbers, a standard list would consume significant RAM.
This project uses a Generator to achieve:
  
  * **Lazy Evaluation**: Numbers are calculated only when requested, one at a time.
  * **State Preservation**: The function "freezes" its variables (`a` and `b`) at the `yield` statement and resumes exactly where it left off when called again.
  * **Infinite Potential**: Because it uses a `while True` loop, this generator could theoretically produce numbers forever without ever crashing the system's memory.

--

### 📦 Keywords & Their Functions

| Keyword/Function | Role in the Code |
| :--- | :--- |
| `yield` | Unlike `return`, it sends a value back to the caller but keeps the function's local variables and state alive. |
| `next()` | The control mechanism. Each time `next(fib_gen)` is called, the function resumes execution until it hits the next `yield`. |
| `while True` | Creates an infinite loop. The generator never ""finishes"" on its own; it simply pauses and waits for the `next` call. |
| `try-except` | Provides robust error handling by catching `ValueError` to ensure the user enters a valid integer for the range. |

--

### 🛠️ Technical Workflow

  * **Initialization**: `fib_gen = fibonacci_generator()` creates a generator object but does not execute the code yet.
  * **Input**: The user defines `num_terms`.
  * **Iteration**: A for loop runs `num_terms` times.
  * **Execution**: Inside the loop, `next(fib_gen)` triggers the generator to calculate the next number in the sequence.
  * **Iteration**: A `for loop` runs `num_terms times`.
  * **Execution**: Inside the loop, `next(fib_gen)` triggers the generator to calculate the next number in the sequence.

--

### 📂 Use Cases for this Logic

  * **Streaming Large Data**: Processing lines of a massive file one-by-one.
  * **Infinite Sequences**: Generating unique IDs or mathematical series without a pre-defined end.
  * **Memory Optimization**: Keeping a low memory footprint while working with large datasets.

--

### 🎓 Learning Outcomes

* **Manual Iteration**: Mastered the use of `next()` to control a generator's execution flow.
* **Resource Management**: Demonstrated how to handle potentially infinite sequences using constant memory (O(1) space complexity).
* **State Management**: Understanding how Python maintains function scope and variable values across multiple calls.
