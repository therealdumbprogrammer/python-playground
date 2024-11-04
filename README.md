---

# Python Cheat Sheet

## Table of Contents

1. [Data Structures](#data-structures)
   - [Lists](#lists)
   - [Tuples](#tuples)
   - [Sets](#sets)
   - [Dictionaries](#dictionaries)
   - [List Comprehensions](#list-comprehensions)
2. [Control Flow](#control-flow)
   - [Conditional Statements](#conditional-statements)
   - [Loops](#loops)
   - [Loop Control Statements](#loop-control-statements)
3. [Functions](#functions)
   - [Defining and Calling Functions](#defining-and-calling-functions)
   - [Parameters and Arguments](#parameters-and-arguments)
   - [Return Values](#return-values)
   - [Variable Scope](#variable-scope)
   - [Chaining Functions and Higher-Order Functions](#chaining-functions-and-higher-order-functions)
   - [Decorators and Closures](#decorators-and-closures)
4. [Modules and Packages](#modules-and-packages)
   - [Creating and Importing Modules](#creating-and-importing-modules)
   - [Understanding Packages](#understanding-packages)
5. [Exception Handling](#exception-handling)
6. [File Input/Output (File I/O)](#file-inputoutput-file-io)

---

## Data Structures

### Lists

- **Definition:** Ordered, mutable collection of items.
- **Syntax:**
  ```python
  my_list = [1, 2, 3, 'a', 'b', 'c']
  ```
- **Common Operations:**
  - **Append:** `my_list.append(4)`
  - **Remove:** `my_list.remove('a')`
  - **Access:** `my_list[0]` → `1`
  - **Slice:** `my_list[1:3]` → `[2, 3]`
  - **Iterate:**
    ```python
    for item in my_list:
        print(item)
    ```

### Tuples

- **Definition:** Ordered, immutable collection of items.
- **Syntax:**
  ```python
  my_tuple = (1, 2, 3, 'a', 'b', 'c')
  ```
- **Common Operations:**
  - **Access:** `my_tuple[0]` → `1`
  - **Slice:** `my_tuple[1:3]` → `(2, 3)`
  - **Unpacking:** `a, b, c = my_tuple[:3]`

### Sets

- **Definition:** Unordered collection of unique items.
- **Syntax:**
  ```python
  my_set = {1, 2, 3, 'a', 'b', 'c'}
  ```
- **Common Operations:**
  - **Add:** `my_set.add(4)`
  - **Remove:** `my_set.remove('a')`
  - **Union:** `set1 | set2`
  - **Intersection:** `set1 & set2`
  - **Difference:** `set1 - set2`
  - **Iterate:**
    ```python
    for item in my_set:
        print(item)
    ```

### Dictionaries

- **Definition:** Unordered collection of key-value pairs.
- **Syntax:**
  ```python
  my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
  ```
- **Common Operations:**
  - **Access:** `my_dict['name']` → `'Alice'`
  - **Add/Update:** `my_dict['age'] = 26`
  - **Remove:** `del my_dict['city']`
  - **Iterate:**
    ```python
    for key, value in my_dict.items():
        print(f"{key}: {value}")
    ```
  - **Keys and Values:**
    ```python
    keys = my_dict.keys()
    values = my_dict.values()
    ```

### List Comprehensions

- **Definition:** Concise way to create lists.
- **Syntax:**
  ```python
  squares = [x**2 for x in range(10)]
  ```
- **With Condition:**
  ```python
  even_squares = [x**2 for x in range(10) if x % 2 == 0]
  ```
- **Nested List Comprehensions:**
  ```python
  matrix = [[x for x in range(3)] for y in range(3)]
  ```

---

## Control Flow

### Conditional Statements

- **Keywords:** `if`, `elif`, `else`
- **Syntax:**
  ```python
  if condition1:
      # Code block
  elif condition2:
      # Code block
  else:
      # Code block
  ```
- **Example:**
  ```python
  age = 20
  if age >= 18:
      print("Adult")
  else:
      print("Minor")
  ```

### Loops

#### `for` Loop

- **Usage:** Iterate over a sequence (list, tuple, dictionary, set, string).
- **Syntax:**
  ```python
  for item in iterable:
      # Code block
  ```
- **Example:**
  ```python
  for num in [1, 2, 3]:
      print(num)
  ```

#### `while` Loop

- **Usage:** Repeat as long as a condition is true.
- **Syntax:**
  ```python
  while condition:
      # Code block
  ```
- **Example:**
  ```python
  count = 0
  while count < 5:
      print(count)
      count += 1
  ```

### Loop Control Statements

- **`break`:** Exit the loop.
  ```python
  for num in range(10):
      if num == 5:
          break
      print(num)
  ```
- **`continue`:** Skip to the next iteration.
  ```python
  for num in range(10):
      if num % 2 == 0:
          continue
      print(num)
  ```
- **`pass`:** Do nothing (placeholder).
  ```python
  for num in range(5):
      pass  # Placeholder for future code
  ```

---

## Functions

### Defining and Calling Functions

- **Definition:**
  ```python
  def function_name(parameters):
      """
      Optional docstring.
      """
      # Function body
      return value  # Optional
  ```
- **Example:**
  ```python
  def greet(name):
      """Greets the user by name."""
      print(f"Hello, {name}!")
  
  greet("Alice")  # Output: Hello, Alice!
  ```

### Parameters and Arguments

- **Positional Arguments:**
  ```python
  def add(a, b):
      return a + b
  
  add(5, 3)  # a=5, b=3 → 8
  ```
- **Keyword Arguments:**
  ```python
  def describe_pet(animal_type, pet_name):
      print(f"I have a {animal_type}.")
      print(f"My {animal_type}'s name is {pet_name}.")
  
  describe_pet(animal_type="hamster", pet_name="Harry")
  describe_pet(pet_name="Rex", animal_type="dog")
  ```
- **Default Parameters:**
  ```python
  def greet(name="Guest"):
      print(f"Hello, {name}!")
  
  greet()           # Output: Hello, Guest!
  greet("Bob")      # Output: Hello, Bob!
  ```
- **Variable-Length Arguments:**
  - **`*args`:** Non-keyword variable-length arguments.
    ```python
    def make_pizza(*toppings):
        print("Making a pizza with:")
        for topping in toppings:
            print(f"- {topping}")
    
    make_pizza('pepperoni')
    make_pizza('mushrooms', 'green peppers', 'extra cheese')
    ```
  - **`**kwargs`:** Keyword variable-length arguments.
    ```python
    def build_profile(first, last, **user_info):
        profile = {}
        profile['first_name'] = first
        profile['last_name'] = last
        for key, value in user_info.items():
            profile[key] = value
        return profile
    
    user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
    print(user_profile)
    # Output: {'first_name': 'albert', 'last_name': 'einstein', 'location': 'princeton', 'field': 'physics'}
    ```

### Return Values

- **Single Return:**
  ```python
  def multiply(a, b):
      return a * b
  
  result = multiply(4, 5)  # 20
  ```
- **Multiple Returns:**
  ```python
  def calculate_statistics(numbers):
      total = sum(numbers)
      average = total / len(numbers)
      maximum = max(numbers)
      return total, average, maximum
  
  total, average, maximum = calculate_statistics([10, 20, 30, 40, 50])
  ```
- **Difference Between `print()` and `return`:**
  - **`print()`:** Outputs to console, returns `None`.
  - **`return`:** Sends value back to caller.
  ```python
  def greet():
      print("Hello!")
  
  def greet_return():
      return "Hello!"
  
  greet()            # Prints: Hello! | Returns: None
  message = greet_return()  # Returns: "Hello!"
  print(message)    # Prints: Hello!
  ```

### Variable Scope

- **Local Variables:**
  ```python
  def my_function():
      local_var = 10
      print(local_var)  # Accessible here
  
  my_function()
  print(local_var)      # Error: NameError
  ```
- **Global Variables:**
  ```python
  global_var = 20
  
  def my_function():
      print(global_var)  # Accessible here
  
  my_function()
  print(global_var)      # Accessible here
  ```
- **Modifying Global Variables:**
  ```python
  counter = 5
  
  def increment():
      global counter
      counter += 1
  
  increment()
  print(counter)  # Output: 6
  ```
- **Nonlocal Variables:**
  ```python
  def outer():
      x = 10
      def inner():
          nonlocal x
          x += 5
      inner()
      print(x)  # Output: 15
  
  outer()
  ```

### Chaining Functions and Higher-Order Functions

- **Chaining Functions:**
  ```python
  def add(a, b):
      return a + b
  
  def multiply(result, factor):
      return result * factor
  
  sum_result = add(5, 3)          # 8
  final_result = multiply(sum_result, 10)  # 80
  print(final_result)             # Output: 80
  ```
- **Higher-Order Functions:**
  - **Functions as Arguments:**
    ```python
    def greet(name):
        return f"Hello, {name}!"
    
    def perform_operation(func, value):
        return func(value)
    
    message = perform_operation(greet, "Alice")
    print(message)  # Output: Hello, Alice!
    ```
  - **Returning Functions:**
    ```python
    def outer_function(msg):
        def inner_function():
            print(msg)
        return inner_function
    
    greet = outer_function("Hello, World!")
    greet()  # Output: Hello, World!
    ```
- **Lambda Functions:**
  ```python
  add_lambda = lambda a, b: a + b
  print(add_lambda(5, 3))  # Output: 8
  ```
- **Built-in Higher-Order Functions:**
  - **`map()`:**
    ```python
    numbers = [1, 2, 3, 4]
    squared = list(map(lambda x: x**2, numbers))
    print(squared)  # Output: [1, 4, 9, 16]
    ```
  - **`filter()`:**
    ```python
    numbers = [1, 2, 3, 4, 5, 6]
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(even_numbers)  # Output: [2, 4, 6]
    ```
  - **`reduce()`:**
    ```python
    from functools import reduce
    numbers = [1, 2, 3, 4]
    sum_all = reduce(lambda a, b: a + b, numbers)
    print(sum_all)  # Output: 10
    ```

### Decorators and Closures

#### Closures

- **Definition:** A nested function that captures and remembers variables from its enclosing scope.
- **Example:**
  ```python
  def outer_function(msg):
      message = msg
      def inner_function():
          print(message)
      return inner_function
  
  greet = outer_function("Hello, World!")
  greet()  # Output: Hello, World!
  ```
- **Use Case (Factory Functions):**
  ```python
  def make_multiplier(factor):
      def multiplier(number):
          return number * factor
      return multiplier
  
  double = make_multiplier(2)
  triple = make_multiplier(3)
  
  print(double(5))  # Output: 10
  print(triple(5))  # Output: 15
  ```

#### Decorators

- **Definition:** Higher-order functions that modify the behavior of other functions without changing their code.
- **Basic Decorator Syntax:**
  ```python
  def my_decorator(func):
      def wrapper():
          print("Before function execution.")
          func()
          print("After function execution.")
      return wrapper
  
  @my_decorator
  def say_hello():
      print("Hello!")
  
  say_hello()
  # Output:
  # Before function execution.
  # Hello!
  # After function execution.
  ```
- **Decorator with Arguments:**
  ```python
  def repeat(num_times):
      def decorator_repeat(func):
          def wrapper(*args, **kwargs):
              for _ in range(num_times):
                  func(*args, **kwargs)
          return wrapper
      return decorator_repeat
  
  @repeat(num_times=3)
  def greet(name):
      print(f"Hello, {name}!")
  
  greet("Alice")
  # Output:
  # Hello, Alice!
  # Hello, Alice!
  # Hello, Alice!
  ```
- **Using `functools.wraps`:**
  ```python
  import functools
  
  def my_decorator(func):
      @functools.wraps(func)
      def wrapper(*args, **kwargs):
          print("Before execution.")
          result = func(*args, **kwargs)
          print("After execution.")
          return result
      return wrapper
  
  @my_decorator
  def say_hello(name):
      """Greets the user by name."""
      print(f"Hello, {name}!")
  
  say_hello("Bob")
  print(say_hello.__name__)  # Output: say_hello
  print(say_hello.__doc__)   # Output: Greets the user by name.
  ```
- **Practical Use Cases of Decorators:**
  - **Logging:**
    ```python
    import functools
    import logging
  
    def log_calls(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
            return func(*args, **kwargs)
        return wrapper
  
    @log_calls
    def add(a, b):
        return a + b
  
    add(2, 3)  # Logs: Calling add with args=(2, 3), kwargs={}
    ```
  - **Access Control:**
    ```python
    import functools
  
    def require_admin(func):
        @functools.wraps(func)
        def wrapper(user, *args, **kwargs):
            if user.role != 'admin':
                raise PermissionError("Admin access required.")
            return func(user, *args, **kwargs)
        return wrapper
  
    @require_admin
    def delete_user(user, user_id):
        print(f"User {user_id} deleted by {user.name}.")
    ```
  - **Timing Functions:**
    ```python
    import functools
    import time
  
    def timer(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"{func.__name__} took {end_time - start_time} seconds to execute.")
            return result
        return wrapper
  
    @timer
    def compute_square(n):
        return n * n
  
    compute_square(1000000)
    ```

---

## Modules and Packages

### Creating and Importing Modules

- **Definition:** A module is a single `.py` file containing Python definitions, functions, classes, variables, and runnable code.
- **Creating a Module:**
  1. **Create a Python File (e.g., `mymodule.py`):**
     ```python
     # mymodule.py
     
     def greet(name):
         """Greets the user by name."""
         return f"Hello, {name}!"
     
     pi = 3.14159
     ```
- **Importing a Module:**
  - **Import Entire Module:**
    ```python
    import mymodule
    
    message = mymodule.greet("Alice")
    print(message)  # Output: Hello, Alice!
    
    print(mymodule.pi)  # Output: 3.14159
    ```
  - **Import Specific Attributes:**
    ```python
    from mymodule import greet, pi
    
    print(greet("Bob"))  # Output: Hello, Bob!
    print(pi)            # Output: 3.14159
    ```
  - **Import with Alias:**
    ```python
    import mymodule as mm
    
    print(mm.greet("Charlie"))  # Output: Hello, Charlie!
    print(mm.pi)                # Output: 3.14159
    ```
- **Reloading Modules:**
  ```python
  import importlib
  import mymodule
  
  importlib.reload(mymodule)
  ```

### Understanding Packages

- **Definition:** A package is a directory containing multiple modules and an `__init__.py` file.
- **Creating a Package:**
  1. **Create Package Directory (e.g., `mypackage/`):**
     ```
     mypackage/
     ├── __init__.py
     ├── module1.py
     └── module2.py
     ```
  2. **Add Modules:**
     ```python
     # mypackage/module1.py
     def function_a():
         return "Function A from Module 1"
     
     # mypackage/module2.py
     def function_b():
         return "Function B from Module 2"
     ```
  3. **Initialize Package (`__init__.py`):**
     ```python
     # mypackage/__init__.py
     from .module1 import function_a
     from .module2 import function_b
     ```
- **Importing from a Package:**
  - **Import Entire Package:**
    ```python
    import mypackage
    
    print(mypackage.function_a())  # Output: Function A from Module 1
    print(mypackage.function_b())  # Output: Function B from Module 2
    ```
  - **Import Specific Functions:**
    ```python
    from mypackage import function_a, function_b
    
    print(function_a())  # Output: Function A from Module 1
    print(function_b())  # Output: Function B from Module 2
    ```
  - **Import with Aliases:**
    ```python
    import mypackage.module1 as mod1
    import mypackage.module2 as mod2
    
    print(mod1.function_a())  # Output: Function A from Module 1
    print(mod2.function_b())  # Output: Function B from Module 2
    ```
- **Nested Packages:**
  ```
  mypackage/
  ├── __init__.py
  ├── module1.py
  └── subpackage/
      ├── __init__.py
      └── module2.py
  ```
  - **Importing from Nested Packages:**
    ```python
    from mypackage.subpackage import module2
    
    print(module2.function_c())  # Output: Function C from Subpackage Module 2
    ```
- **Third-Party Packages:**
  - **Installation:**
    ```bash
    pip install requests
    ```
  - **Usage:**
    ```python
    import requests
    
    response = requests.get('https://api.github.com')
    print(response.status_code)  # Output: 200
    ```

### Best Practices for Modules and Packages

1. **Descriptive Naming:** Use clear and descriptive names for modules and packages.
2. **Avoid Circular Imports:** Ensure modules do not import each other in a circular manner.
3. **Use `__init__.py` Wisely:** Control the package's public interface and initialize package-level variables if needed.
4. **Documentation:** Include docstrings in modules and functions, and consider adding a `README.md` for packages.
5. **Version Control:** Use version control systems (e.g., Git) to manage changes.
6. **Testing:** Write tests for your modules to ensure they function as expected.

---

## Exception Handling

### Basic `try...except` Blocks

- **Syntax:**
  ```python
  try:
      # Code that may raise an exception
  except SomeException as e:
      # Handle exception
  ```
- **Example:**
  ```python
  try:
      result = 10 / 0
  except ZeroDivisionError as e:
      print("Error: Division by zero is not allowed.")
  ```
- **Multiple Exceptions:**
  ```python
  try:
      # Code that may raise multiple exceptions
  except (ValueError, TypeError) as e:
      print(f"Error: {e}")
  ```
- **Using `else` and `finally`:**
  ```python
  try:
      result = 10 / 2
  except ZeroDivisionError:
      print("Error: Division by zero.")
  else:
      print(f"Result is {result}")  # Executes if no exception
  finally:
      print("Execution completed.")  # Always executes
  ```
- **Raising Exceptions:**
  ```python
  def check_positive(number):
      if number < 0:
          raise ValueError("Negative number provided.")
      return True
  
  try:
      check_positive(-5)
  except ValueError as e:
      print(e)
  # Output: Negative number provided.
  ```

---
# Python File Input/Output (File I/O) Cheat Sheet

## Basic File Operations

### Opening Files

To perform file operations, use the `open()` function which returns a file object.

```python
file = open('filename', 'mode')
```

**Common Modes:**
- `'r'`: Read mode (default)
- `'w'`: Write mode (creates/truncates the file)
- `'a'`: Append mode (adds to the end of the file)
- `'rb'`: Read binary
- `'wb'`: Write binary

### Reading from Files

**Methods:**
- `read(size=-1)`: Reads the entire file or specified number of characters.
- `readline()`: Reads the next line from the file.
- `readlines()`: Reads all lines into a list.

```python
content = file.read()
line = file.readline()
lines = file.readlines()
```

### Writing to Files

**Methods:**
- `write(string)`: Writes a string to the file.
- `writelines(list)`: Writes a list of strings to the file.

```python
file.write("Hello, World!\n")
file.writelines(["Line 1\n", "Line 2\n"])
```

### Closing Files

Always close files to free up system resources.

```python
file.close()
```

## Using Context Managers (`with` Statement)

The `with` statement ensures that files are properly closed after their suite finishes, even if an error occurs.

```python
with open('filename', 'mode') as file:
    # Perform file operations
```

## Working with Different File Formats

### Text Files

Store data in a readable format. Use standard file methods to read and write.

### CSV Files

Use the `csv` module to handle CSV (Comma-Separated Values) files.

**Reading CSV Files:**
```python
import csv

with open('data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        print(row)
```

**Writing CSV Files:**
```python
import csv

data = [
    ['Name', 'Age', 'Grade'],
    ['Alice', '23', 'A'],
    ['Bob', '22', 'B']
]

with open('data.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(data)
```

### JSON Files

Use the `json` module to handle JSON (JavaScript Object Notation) files.

**Reading JSON Files:**
```python
import json

with open('data.json', 'r') as jsonfile:
    data = json.load(jsonfile)
    print(data)
```

**Writing JSON Files:**
```python
import json

data = {
    "name": "Alice",
    "age": 23,
    "grade": "A"
}

with open('data.json', 'w') as jsonfile:
    json.dump(data, jsonfile, indent=4)
```

### Binary Files

Handle non-text data like images, audio, and executable files using binary modes.

**Reading Binary Files:**
```python
with open('image.png', 'rb') as file:
    binary_data = file.read()
```

**Writing Binary Files:**
```python
binary_data = b'\x89PNG\r\n\x1a\n...'

with open('new_image.png', 'wb') as file:
    file.write(binary_data)
```

## Handling File Exceptions

File operations can raise various exceptions. It's essential to handle them to make your programs robust.

**Common Exceptions:**
- `FileNotFoundError`: Raised when a file or directory is requested but doesn't exist.
- `PermissionError`: Raised when the program lacks the required permissions.
- `IOError`: Raised for input/output operations errors.
- `IsADirectoryError`: Raised when a directory is expected but found a file.

**Example:**
```python
try:
    with open('nonexistent.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("Error: The file does not exist.")
except PermissionError:
    print("Error: You do not have permission to access this file.")
except IOError as e:
    print(f"Error: An I/O error occurred. {e}")
```

## Best Practices

1. **Use Context Managers:**
   - Ensures files are properly closed.
   ```python
   with open('file.txt', 'r') as file:
       content = file.read()
   ```

2. **Handle Specific Exceptions:**
   - Provide meaningful error messages.
   ```python
   try:
       with open('file.txt', 'r') as file:
           content = file.read()
   except FileNotFoundError:
       print("File not found.")
   ```

3. **Use Proper File Modes:**
   - Choose appropriate mode based on operation.

4. **Close Files Properly:**
   - If not using `with`, ensure `file.close()` is called.

5. **Validate File Paths:**
   - Ensure correct and accessible file paths.

6. **Use `csv` and `json` Modules for Structured Data:**
   - Simplifies handling CSV and JSON data.

7. **Avoid Hardcoding File Paths:**
   - Use variables or configuration files to manage paths.

8. **Optimize Performance for Large Files:**
   - Read or write in chunks instead of loading the entire file into memory.
   ```python
   with open('large_file.txt', 'r') as file:
       while True:
           chunk = file.read(1024)  # Read in 1KB chunks
           if not chunk:
               break
           process(chunk)
   ```

9. **Secure File Handling:**
   - Validate and sanitize file names and paths to prevent security vulnerabilities like path traversal attacks.

---