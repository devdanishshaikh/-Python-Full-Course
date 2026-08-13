# Chapter 1: Introduction to Python

## Introduction
A computer only understands binary (0 and 1). Humans write code in simple languages like Python. A translator called an **interpreter** converts Python code into machine code, so the computer can run it.

## Key Concepts

### 1. Programming
**Definition:**
Programming means giving step-by-step instructions to a computer to do a task. These instructions are called a **program**.

**Why it is used:**
Computers cannot think on their own. We use programs to tell them exactly what to do.

**How it works:**
We write code in a programming language (like Python). The computer follows the code, one instruction at a time.

**Example:**
```python
print("Hello World")
# This instruction tells the computer to show text on screen
```

### Why This Matters in a Job
- **Automation:** Programs replace manual, repeated work.
- **AI/ML:** All AI models are built using programming.

---

### 2. Python (and Why We Use It)
**Definition:**
Python is a high-level, easy-to-read programming language.

**Why it is used:**
- Simple syntax, close to English.
- Free and open-source.
- Used in many fields: web development, data science, automation, AI/ML.

**How it works:**
Python code is read and run by the **Python interpreter**, line by line.

**Example:**
```python
print(5 + 3)
# Output: 8
```

### Why This Matters in a Job
- **Data Science / Data Analysis:** Python is used with tools like pandas and NumPy.
- **AI/ML:** Frameworks like TensorFlow and scikit-learn use Python.
- **Automation:** Python scripts automate repetitive tasks.

---

### 3. Setup (Python + VS Code)
**Definition:**
Before writing Python code, we need Python installed and a code editor (VS Code).

**Why it is used:**
Python runs the code. VS Code is where we write and organize the code.

**How it works:**
1. Download Python from python.org, check "Add to PATH" during install.
2. Verify install:
```bash
python --version
```
3. Install VS Code from code.visualstudio.com.
4. Save files with a `.py` extension (e.g., `app.py`) and run them in VS Code.

**Common mistake:** Forgetting to add Python to PATH, or saving a file without `.py`.

---

### 4. `print()` Function
**Definition:**
`print()` displays text or values on the screen. This is called **output**.

**Why it is used:**
To see results and check if the code works correctly.

**How it works:**
- Text inside double quotes `" "` is shown exactly as written (this is a **string**).
- A comma `,` inside `print()` joins items on the same line.
- Separate `print()` calls go to new lines.

**Example:**
```python
print("Name:", "Sarah")
print("Age:", 23)
# Output:
# Name: Sarah
# Age: 23
```

**Common mistakes:**
- Forgetting quotes around text → causes an error.
- Confusing printing a variable's **name** vs its **value**.

### Why This Matters in a Job
- **Data Analysis:** Used to display results and check outputs while exploring data.

---

# Chapter 2: Variables and Data Types

## Introduction
Variables store data in memory so we can use and change it later. Python automatically detects what type of data (text, number, etc.) each variable holds.

## Key Concepts

### 1. Variables
**Definition:**
A variable is a name for a memory location that stores a value.

**Why it is used:**
To save data and reuse it, instead of writing the same value repeatedly.

**How it works:**
We use `=` (assignment operator) to store a value into a variable name. `=` means "store the right value into the left name," not "equal to."

**Example:**
```python
name = "Sarah"
age = 23
age = 24        # value updated, old value is gone
```

**Key rules:**
- Variable names can have letters, numbers, and underscore `_`.
- Cannot start with a number.
- No special symbols (`%`, `@`, `#`, etc.).
- Case-sensitive (`Name` ≠ `name`).
- Names should be simple, short, and meaningful.

**Common mistakes:**
- Starting a name with a digit (`1age` → error).
- Using spaces instead of underscore (`my name` → error, use `my_name`).
- Confusing `=` (assignment) with `==` (comparison).

### Why This Matters in a Job
- **Data Analysis/Automation:** Variables store data values, file paths, counters, and settings used throughout a script.

---

### 2. Printing Variable Values
**Definition:**
Shows the value stored in a variable, not its name.

**Why it is used:**
To display the current data stored, which may change during the program.

**How it works:**
- `print("name")` → prints the literal word "name" (in quotes = text).
- `print(name)` → prints the value stored in the variable `name` (no quotes = variable).

**Example:**
```python
name = "Sarah"
print("name")   # Output: name
print(name)     # Output: Sarah
```

**Common mistake:** Adding quotes by mistake when trying to print a variable's value.

---

### 3. Data Types
**Definition:**
The data type tells what kind of value a variable holds (text, whole number, decimal, or true/false).

**Why it is used:**
Python needs to know the data type to handle it correctly (e.g., math operations only work on numbers).

**How it works:**
Python detects the type automatically (**dynamic typing**). Use `type()` to check it.

**Example:**
```python
name = "Sarah"       # str
age = 23              # int
price = 25.99         # float
is_active = True      # bool

print(type(age))      # <class 'int'>
```

**Main data types:**

| Type | Example | Meaning |
|---|---|---|
| `str` | `"Sarah"` | Text |
| `int` | `23`, `-5` | Whole number |
| `float` | `25.99` | Decimal number |
| `bool` | `True`, `False` | True/False only |

**Key rules:**
- Strings use quotes (`" "`, `' '`, or `''' '''`); double quotes are standard.
- Boolean values must start with a capital letter: `True`, `False`.

**Common mistakes:**
- Thinking `int` can have decimals (it cannot).
- Writing `true`/`false` in lowercase (Python needs `True`/`False`).

### Why This Matters in a Job
- **Data Science/Analysis:** Correct data types are essential for calculations and data cleaning.
- **AI/ML:** Models require input data in the correct type (numbers, text, etc.).

---

### 4. `None` Data Type
**Definition:**
`None` is a special data type used when a variable has **no value** yet.

**Why it is used:**
To show that a variable exists but is empty, or has not been given a value.

**How it works:**
We assign `None` to a variable directly, like any other value.

**Example:**
```python
a = None
print(type(a))   # Output: <class 'NoneType'>
```

**Key rule:** `None` must start with a capital `N`. Writing `none` (lowercase) causes an error.

### Why This Matters in a Job
- **Data Analysis:** `None` is often used to mark missing or empty data values.

---

### 5. Keywords (Reserved Words)
**Definition:**
Keywords are special words that already have a fixed meaning in Python (for example: `True`, `False`, `None`, `and`, `or`, `if`, `break`).

**Why it is used:**
Python reserves these words for specific tasks. This keeps the language rules clear and consistent.

**How it works:**
We cannot use a keyword as a variable name, because Python already uses that word for something else.

**Example:**
```python
# Wrong - "True" is a keyword, not allowed as a variable name
True = 5   # This causes an error
```

**Key rule:** We don't need to memorize all keywords right away. We naturally learn them as we cover more Python topics.

---

### 6. Case Sensitivity
**Definition:**
Python treats uppercase and lowercase letters as different. This is called being **case-sensitive**.

**Why it is used:**
This is a core rule of Python's syntax (unlike some languages, like SQL, which do not care about letter case).

**How it works:**
`Name`, `name`, and `NAME` are treated as three different variables in Python.

**Example:**
```python
name = "Sarah"
Name = "John"
print(name)  # Output: Sarah
print(Name)  # Output: John
```

**Common mistakes:**
- Writing `true`/`false`/`none` in lowercase instead of `True`/`False`/`None`.
- Not matching the exact letter case used earlier in the code, causing errors.

---

# Chapter 3: Operators and Expressions

## Introduction
An **expression** is a piece of code that Python calculates to produce a value (for example, `2 + 3`). Python follows fixed rules to calculate these expressions correctly.

## Key Concepts

### 1. Typed Language: Implicit vs Explicit
**Definition:**
A "typed language" means every piece of data has a data type. Python decides this type **implicitly** (automatically). Some languages, like Java or C++, need the type to be stated **explicitly** (manually).

**Why it is used:**
Implicit typing makes Python faster and easier to write, since we don't need to declare types manually.

**How it works:**
In Python, we just assign a value, and Python figures out the type on its own.

**Example:**
```python
# Python (implicit typing)
name = "Sarah"     # Python decides this is a string automatically

# Java (explicit typing) - written for comparison only, not valid Python
# String name = "Sarah";   -> type "String" must be stated manually
```

**Key rule:** Python is an **implicitly typed language** for variables — we never write the data type ourselves.

### Why This Matters in a Job
- **Automation/Scripting:** Implicit typing makes Python code shorter and quicker to write for scripts.

---

### 2. String Multiplied by a Number (Repetition)
**Definition:**
When a string is multiplied by a number, Python repeats that string the given number of times.

**Why it is used:**
This is a quick way to repeat text without writing it multiple times.

**How it works:**
`string * number` → the string is repeated `number` times.

**Example:**
```python
text = "@"
print(text * 6)
# Output: @@@@@@
```

**Common mistake:** Expecting `string * number` to do normal multiplication like numbers — it repeats text instead.

---

### 3. String + String (Concatenation)
**Definition:**
Joining two strings together using `+` is called **concatenation**.

**Why it is used:**
To combine text values, like joining a first name and last name.

**How it works:**
`string1 + string2` → the two strings join into one, in that order.

**Example:**
```python
first = "Data"
second = "Science"
print(first + second)
# Output: DataScience
```

**Key rule:** You can only use `+` between two strings, or between two numbers — not mix a string and a number directly (that causes an error, unless converted first).

### Why This Matters in a Job
- **Data Analysis:** Concatenation is used to build messages, labels, and combined text fields.

---

### 4. Arithmetic Operators and Operator Precedence
**Definition:**
Arithmetic operators perform math: `+` (add), `-` (subtract), `*` (multiply), `/` (divide), `%` (remainder), `//` (integer division), `**` (power).

**Why it is used:**
To perform calculations in code, just like in math.

**How it works:**
Python follows **operator precedence** (order of operations) — multiplication and division happen before addition and subtraction, similar to math rules (BODMAS/PEMDAS).

**Example:**
```python
a = 2
b = 3
c = 4
print(a + b * c)
# Step 1: b * c = 12
# Step 2: a + 12 = 14
# Output: 14
```

**Common mistake:** Solving left to right without checking operator precedence first.

### Why This Matters in a Job
- **Data Science:** Correct calculation order matters in formulas and statistical computations.

---

### 5. Integer + Float = Float
**Definition:**
When an expression mixes an integer and a float, the result is always a **float**.

**Why it is used:**
This keeps calculations accurate. Rounding to an integer could lose important decimal information.

**How it works:**
Python automatically converts the result to float, even if one of the original numbers was an integer.

**Example:**
```python
a = 10
b = 5.0
c = a * b
print(c)
# Output: 50.0 (not 50)
```

**Key rule:** If even one value in a calculation is a float, the final result becomes a float.

---

### 6. Division (`/`) Always Returns a Float
**Definition:**
The normal division operator `/` always gives a float result, even if both numbers are integers.

**Why it is used:**
To give an accurate, precise answer instead of losing decimal values.

**How it works:**
`a / b` → always returns a float.

**Example:**
```python
a = 1
b = 2
c = a / b
print(c)
# Output: 0.5
```

**Common mistake:** Expecting `int / int` to give an `int` result — it always gives a `float` in Python.

---

### 7. Integer Division (`//`)
**Definition:**
Integer division (`//`) divides two numbers and removes the decimal part, rounding down to the nearest whole number. The result is still shown as a float if any input is a float.

**Why it is used:**
Useful when we only need the whole number part of a division result (for example, counting full groups).

**How it works:**
- `//` divides normally, then rounds **down** to the closest smaller (or equal) whole number. This is called the **floor**.
- If the inputs include a float, the answer is displayed as a float (e.g., `0.0`), but the value itself is a whole number.

**Example:**
```python
a = 1.5
b = 3
c = a // b
print(c)
# 1.5 / 3 = 0.5 -> floor(0.5) = 0 -> shown as float
# Output: 0.0
```

**Key rule (Floor):** The floor of a number is the closest whole number that is **less than or equal to** it.
- `floor(5.2)` = 5
- `floor(-5.2)` = -6 (goes down, not up)

**Common mistake:** Confusing `/` (always precise float) with `//` (rounds down to a whole number, shown as float if inputs include a float).

### Why This Matters in a Job
- **Data Analysis/Automation:** Integer division is useful for tasks like splitting data into equal batches or pages.

---

### 8. Comments
**Definition:**
A comment is a part of the code that Python does **not run**. We write comments to explain the code in plain language.

**Why it is used:**
To make code easier to understand — for ourselves later, and for other people reading our code.

**How it works:**
- A single-line comment starts with `#`.
- A multi-line comment is written inside triple quotes `''' '''` or `""" """`.

**Example:**
```python
# This line prints a greeting
print("Hello World")

'''
This is a multi-line comment.
It can cover many lines.
It does not run as code.
'''
```

**Key rule:** Anything after `#` on that line is ignored by Python. It has no effect on the program's output.

**Common mistake:** Forgetting that comments are only for humans — they don't run, so they can't perform any action in the program.

### Why This Matters in a Job
- **Automation/Team Projects:** Clear comments help other developers (and your future self) understand and maintain the code.

---

## Key Concepts (continued): Operators

### 9. What Is an Operator?
**Definition:**
An operator is a symbol that performs an operation (a task) on values. The values it works on are called **operands**.

**Why it is used:**
Operators let us perform calculations, comparisons, and logical checks in code.

**How it works:**
In `a + b`, `+` is the operator, and `a` and `b` are the operands.

**Example:**
```python
a = 5
b = 2
print(a + b)   # Output: 7
```

---

### 10. Arithmetic Operators (Full List)
**Definition:**
Arithmetic operators perform basic math calculations.

**Why it is used:**
For all number-based calculations in a program.

**How it works:**

| Operator | Meaning | Example (`a=5, b=2`) | Result |
|---|---|---|---|
| `+` | Addition | `a + b` | `7` |
| `-` | Subtraction | `a - b` | `3` |
| `*` | Multiplication | `a * b` | `10` |
| `/` | Division (always float) | `a / b` | `2.5` |
| `%` | Modulo (remainder) | `a % b` | `1` |
| `**` | Power (exponent) | `a ** b` | `25` |
| `//` | Integer division (floor) | `a // b` | `2` |

**Example:**
```python
a = 5
b = 2
print(a + b)    # 7
print(a - b)    # 3
print(a * b)    # 10
print(a / b)    # 2.5
print(a % b)    # 1 (remainder of 5/2)
print(a ** b)   # 25 (5 to the power 2)
print(a // b)   # 2 (whole number part of 5/2)
```

**Common mistake:** Confusing `%` (remainder) with `/` (division), or `**` (power) with `*` (multiply).

### Why This Matters in a Job
- **Data Science:** Arithmetic operators are the base of every formula and calculation in data analysis.

---

### 11. Relational (Comparison) Operators
**Definition:**
Relational operators compare two values. The result is always a **boolean** (`True` or `False`).

**Why it is used:**
To check relationships between values — used heavily later in `if` conditions.

**How it works:**

| Operator | Meaning | Example (`a=50, b=20`) | Result |
|---|---|---|---|
| `==` | Equal to | `a == b` | `False` |
| `!=` | Not equal to | `a != b` | `True` |
| `>` | Greater than | `a > b` | `True` |
| `<` | Less than | `a < b` | `False` |
| `>=` | Greater than or equal to | `a >= b` | `True` |
| `<=` | Less than or equal to | `a <= b` | `False` |

**Example:**
```python
a = 50
b = 20
print(a == b)   # False
print(a != b)   # True
print(a > b)    # True
```

**Key rule:** `==` checks equality (a question). `=` assigns a value (a command). They are NOT the same.

**Common mistake:** Using `=` when we mean `==`, especially inside conditions.

### Why This Matters in a Job
- **Data Analysis/Automation:** Comparison operators are used to filter data and check conditions (e.g., "is sales > target?").

---

### 12. Assignment Operators
**Definition:**
Assignment operators store a value into a variable. `=` is the basic one; others combine an operation with assignment.

**Why it is used:**
To quickly update a variable's value using its own current value (shortcut, instead of writing it out fully).

**How it works:**

| Operator | Meaning | Same As |
|---|---|---|
| `=` | Assign value | `num = 10` |
| `+=` | Add and assign | `num = num + 10` |
| `-=` | Subtract and assign | `num = num - 10` |
| `*=` | Multiply and assign | `num = num * 10` |
| `/=` | Divide and assign | `num = num / 10` |
| `%=` | Modulo and assign | `num = num % 10` |
| `**=` | Power and assign | `num = num ** 10` |

**Example:**
```python
num = 10
num += 10   # same as: num = num + 10
print(num)  # Output: 20

num -= 5    # same as: num = num - 5
print(num)  # Output: 15
```

### Why This Matters in a Job
- **Automation:** Shortcut operators (like `+=`) are common in loops that count or add up totals.

---

### 13. Logical Operators
**Definition:**
Logical operators combine or reverse boolean values. Python has three: `and`, `or`, `not`.

**Why it is used:**
To build more complex true/false conditions from simple ones.

**How it works:**

| Operator | Meaning | Result is `True` when |
|---|---|---|
| `and` | Both must be true | Both values are `True` |
| `or` | At least one must be true | At least one value is `True` |
| `not` | Reverses the value | Flips `True` to `False`, and `False` to `True` |

**Example:**
```python
value1 = True
value2 = False

print(value1 and value2)   # False (not both true)
print(value1 or value2)    # True (at least one true)
print(not value1)          # False (opposite of True)
```

**Real example with expressions:**
```python
a = 50
b = 30
print(a == b or a > b)
# a == b -> False
# a > b  -> True
# False or True -> True
```

**Common mistake:** Mixing up `and` (needs both true) with `or` (needs only one true).

### Why This Matters in a Job
- **Data Analysis/Automation:** Logical operators combine multiple filter conditions (e.g., "age > 18 AND status == active").

---

### 14. Type Conversion (Implicit)
**Definition:**
Type conversion is when Python **automatically** changes one data type into another during a calculation.

**Why it is used:**
To safely combine different but compatible data types in one expression (e.g., `int` and `float`), without losing information.

**How it works:**
When an `int` and a `float` are used together, Python automatically converts the `int` to a `float` (since `float` can hold more detail).

**Example:**
```python
a = 2          # int
b = 4.25       # float
total = a + b
print(total)   # Output: 6.25 (a was auto-converted to 2.0)
```

**Common mistake:** Expecting automatic conversion between a `string` and a number — this does NOT work and causes an error.

```python
a = "2"        # string
b = 4.25       # float
print(a + b)   # Error: cannot combine string and float automatically
```

---

### 15. Type Casting (Explicit / Manual Conversion)
**Definition:**
Type casting is when **we manually** convert a value from one data type to another, using functions like `int()`, `float()`, `str()`.

**Why it is used:**
To fix type mismatches ourselves, when Python cannot (or should not) convert automatically.

**How it works:**
- `int(value)` → converts to integer
- `float(value)` → converts to float
- `str(value)` → converts to string

**Example:**
```python
a = "2"              # string
a = int(a)            # manually convert to int
b = 4.25
print(a + b)          # Output: 6.25 (now works, no error)

price = 3.14
price_text = str(price)
print(type(price_text))   # Output: <class 'str'>
```

**Key rule:** Type casting only works if the value actually "fits" the new type. `int("Sarah")` will cause an error, because "Sarah" is not a valid number.

**Common mistake:** Trying to convert text (like a name) into a number — this always fails.

### Why This Matters in a Job
- **Data Analysis:** Type casting is used constantly when cleaning data (e.g., converting text columns from a file into numbers for calculation).

---

### 16. Taking Input from the User
**Definition:**
The `input()` function lets the program ask the user to type something while the program is running.

**Why it is used:**
To make programs interactive — the program can react to what the user enters, instead of using fixed values.

**How it works:**
- `input("message")` shows the message, waits for the user to type, and returns what they typed.
- **Important rule:** `input()` always returns a **string**, even if the user types a number.

**Example:**
```python
name = input("Enter your name: ")
print("Welcome", name)
# If user types: Sarah
# Output: Welcome Sarah
```

**Taking a number as input (needs type casting):**
```python
age = int(input("Enter your age: "))   # convert string input to int
print("You entered:", age)
print(type(age))   # <class 'int'>
```

**Common mistake:** Forgetting to convert `input()` to `int` or `float` before doing math with it — this causes errors or wrong results (since text can't be added like numbers).

### Why This Matters in a Job
- **Automation:** Scripts often take user input to control what the program does (e.g., asking for a file name or a setting).
- **Data Analysis:** Interactive tools often ask users for parameters (like a date range) before running a report.

---

## Practice Questions (With Solutions)

### Q1: Input two numbers and print their sum.
```python
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
print("Sum =", first + second)

# Example run:
# Enter first number: 20
# Enter second number: 50
# Output: Sum = 70
```

### Q2: Input the side of a square and print its area.
```python
side = float(input("Enter square side: "))
area = side * side
print("Area of the square is:", area)

# Example run:
# Enter square side: 4
# Output: Area of the square is: 16.0
```

### Q3: Input two floating-point numbers and print their average.
```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
average = (a + b) / 2
print("Average =", average)

# Example run:
# Enter first number: 16.5
# Enter second number: 3.5
# Output: Average = 10.0
```

### Q4: Input two integers `a` and `b`. Print `True` if `a` is greater than or equal to `b`, otherwise print `False`.
```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a >= b)

# Example run 1:
# a = 15, b = 2 -> Output: True

# Example run 2:
# a = 2, b = 15 -> Output: False
```

---

## Quick Summary Table (All Operators)

| Category | Operators | Purpose |
|---|---|---|
| Arithmetic | `+ - * / % ** //` | Perform calculations |
| Relational | `== != > < >= <=` | Compare values (returns True/False) |
| Assignment | `= += -= *= /= %= **=` | Store or update values |
| Logical | `and or not` | Combine or reverse boolean values |
