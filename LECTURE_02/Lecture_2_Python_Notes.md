# 🐍 Python Lecture 2 — Strings & Conditional Statements

---

## 1️⃣ Strings

### 📖 Definition
A **string** is a data type in Python used to store a **sequence of characters** — it can be a single character, a word, a full sentence, or even a paragraph.

### 💡 Best Example
```python
str1 = "This is a string"        # double quotes
str2 = 'college'                 # single quotes
str3 = """This is a string"""    # triple quotes
```

### 🔑 Key Points
- Strings can be created using `' '`, `" "`, or `""" """`.
- **Double quotes are most commonly used** in professional code.
- Use **double quotes** when the string itself contains an apostrophe (`'`), and use **single quotes** when the string contains a `"`.
  ```python
  text = "This is Prisha's College Tutorial"   # correct — apostrophe inside double quotes
  ```
- Triple quotes are mainly used for multi-line strings or docstrings.

---

## 2️⃣ Escape Sequence Characters

### 📖 Definition
Special characters used inside a string to add **formatting** (like a new line or a tab) that normally can't be typed directly in code.

### 💡 Best Example
```python
print("Hello\nWelcome to Python")   # \n → new line
print("Hello\tWorld")               # \t → tab space
```
**Output:**
```
Hello
Welcome to Python

Hello    World
```

### 🔑 Key Points
| Escape Character | Meaning |
|---|---|
| `\n` | New line |
| `\t` | Tab space |
- You can't press "Enter" directly inside a string in code — escape sequences solve this problem.
- Useful when printing paragraphs or long, structured text.

---

## 3️⃣ String Concatenation

### 📖 Definition
**Concatenation** means joining two or more strings together using the `+` operator.

### 💡 Best Example
```python
string1 = "apna"
string2 = "college"
final_string = string1 + " " + string2
print(final_string)      # apna college
```

### 🔑 Key Points
- Works exactly like adding numbers (`a + b`), but here we add strings.
- Adding an empty string `""` (like a space) between two strings is completely valid.
- Result can be stored directly in a new variable.

---

## 4️⃣ Length of a String — `len()`

### 📖 Definition
The `len()` function returns the **total number of characters** present in a string.

### 💡 Best Example
```python
name = "Python"
print(len(name))          # 6

sentence = "apna college"
print(len(sentence))      # 12 (includes the space!)
```

### 🔑 Key Points
- **Spaces are counted** as characters.
- Special characters (`%`, `$`, `@`) and digits are also counted.
- Common beginner mistake: forgetting that spaces count toward length.

---

## 5️⃣ Indexing

### 📖 Definition
**Indexing** means giving every character in a string a **position number**, so we can access any character directly.

### 💡 Best Example
```python
s = "apna college"
print(s[0])     # a   (first character)
print(s[1])     # p
print(s[5])     # ' ' (space)
```

### 🔑 Key Points
- Indexing in Python **always starts from 0**, not 1.
- Syntax: `string_name[index_number]`
- We can **access** characters using index, but we **cannot modify/change** them:
  ```python
  s[4] = "-"   # ❌ Error: 'str' object does not support item assignment
  ```
- Strings are **immutable** in Python — once created, individual characters can't be changed.

---

## 6️⃣ Slicing

### 📖 Definition
**Slicing** means accessing a **part (chunk)** of a string using a start and end index — like cutting a piece from a fruit.

### 💡 Best Example
```python
s = "apna college"
print(s[1:4])     # pna   → index 1,2,3 (4 excluded)
print(s[0:4])     # apna  → first word
print(s[5:])      # college  (end omitted = till last index)
print(s[:4])      # apna     (start omitted = from index 0)
print(s[-3:-1])   # eg       (negative indexing example)
```

### 🔑 Key Points
- Syntax: `string[start:end]`
- **Start index is included, end index is NOT included.**
- If **end index is skipped** → Python automatically goes till the last character.
- If **start index is skipped** → Python automatically starts from index 0.
- `len(string)` can be used as the end index to safely reach the last character.
- **Negative indexing**: Last character = `-1`, second last = `-2`, and so on (counts backward). Mainly used in slicing, not in normal indexing.

---

## 7️⃣ Important String Functions

### 📖 Definition
Python has many built-in (in-built) functions to perform common operations on strings quickly.

| Function | What it Does | Example | Output |
|---|---|---|---|
| `.endswith("x")` | Checks if string ends with given value → returns True/False | `"apna".endswith("a")` | `True` |
| `.capitalize()` | Capitalizes only the **first letter**; returns a **new string** | `"apna".capitalize()` | `"Apna"` |
| `.replace("old","new")` | Replaces **all occurrences** of old value with new value | `"I am o".replace("o","a")` | `"I am a"` |
| `.find("x")` | Returns index of **first occurrence**; returns `-1` if not found | `"python".find("o")` | `4` |
| `.count("x")` | Counts how many times a substring appears | `"apna college".count("o")` | `2` |

### 🔑 Key Points
- `.capitalize()` does **not change the original string** — you must reassign it:
  ```python
  s = s.capitalize()   # now original variable is updated
  ```
- `.find()` returns `-1` (not an error) when the value doesn't exist — because `-1` is never a valid index in normal search.
- These functions create/return **new strings**; they don't modify the original string in place (since strings are immutable).

---

## 8️⃣ Conditional Statements (if, elif, else)

### 📖 Definition
Conditional statements let a program **make decisions** and execute different blocks of code depending on whether a condition is **True** or **False**.

### 💡 Best Example
```python
age = 21
if age >= 18:
    print("Can vote")
    print("Can apply for license")
```
**Output:**
```
Can vote
Can apply for license
```

### 🔑 Key Points
- Syntax: `if condition:` followed by an **indented block** (1 tab / 4 spaces).
- A **condition** is anything that returns `True` or `False` (comparisons, boolean variables).
- Python uses **indentation** (proper spacing) instead of curly braces `{}` (unlike C++/Java) to define code blocks.
- Multiple statements can be written under one `if` block — they all execute together when the condition is True.
- If condition is `False`, the block is simply skipped (nothing happens, unless there's an `else`).

---

## 9️⃣ if vs elif vs else

### 📖 Definition
- **`if`** → checks a condition.
- **`elif`** (else if) → checked **only if** the previous `if`/`elif` was False.
- **`else`** → runs when **all** above conditions are False (no condition needed here).

### 💡 Best Example (Traffic Light Logic)
```python
light = "green"

if light == "red":
    print("Stop")
elif light == "green":
    print("Go")
elif light == "yellow":
    print("Look")
else:
    print("Light is broken")
```
**Output:** `Go`

### 🔑 Key Points
- **You can write `if` and `elif` multiple times**, but only **ONE `else`**, always written **last**.
- **Main difference:** `if` **always checks** its own condition independently. `elif` is checked **only when** the previous condition failed.
- As soon as **one condition becomes True**, its block runs and **all remaining elif/else are skipped**.
- `else` requires no condition — it's the default/fallback case.

### 🎯 Second Best Example (Grading System using `and`)
```python
marks = 85

if marks >= 90:
    grade = "A"
elif marks >= 80 and marks < 90:
    grade = "B"
elif marks >= 70 and marks < 80:
    grade = "C"
else:
    grade = "D"

print("Grade:", grade)   # Grade: B
```
- Here `and` (logical operator) combines two conditions — **both must be True** for the block to run.
- This shows how ranges (like 80–90) are checked using `and`.

---

## 🔟 Nesting (if inside if)

### 📖 Definition
**Nesting** means writing an `if` statement **inside another `if`/`else`** block — used when you need to check an extra condition only after the first one is already True.

### 💡 Best Example
```python
age = 95

if age >= 18:
    if age >= 80:
        print("Cannot drive")
    else:
        print("Can drive")
else:
    print("Cannot drive")
```
**Output:** `Cannot drive`

### 🔑 Key Points
- The inner `if` is checked **only when the outer `if` condition is already True**.
- Requires **extra indentation** for the nested block.
- Very useful for multi-level decision-making (e.g., age category + upper limit check together).
- Nesting also works with loops (covered in later lectures).

---

## 1️⃣1️⃣ Even / Odd Check (Practice Concept)

### 📖 Definition
A number is **even** if dividing it by 2 gives remainder `0`; otherwise, it's **odd**. This is checked using the **modulo operator `%`**.

### 💡 Best Example
```python
num = int(input("Enter number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```

### 🔑 Key Points
- `%` (modulo) gives the **remainder** after division.
- `num % 2 == 0` → Even.
- `num % 2 != 0` (anything else) → Odd.
- Same logic (`num % x == 0`) is used to check if a number is a **multiple** of any value `x` (e.g., multiple of 5, 7, etc.).

---

## 1️⃣2️⃣ Finding Greatest of 3 Numbers (Practice Concept)

### 📖 Definition
Using nested/chained `if-elif-else` with comparison operators to find the largest among multiple values.

### 💡 Best Example
```python
a = int(input("First number: "))
b = int(input("Second number: "))
c = int(input("Third number: "))

if a >= b and a >= c:
    print("First number is largest:", a)
elif b >= c:
    print("Second number is largest:", b)
else:
    print("Third number is largest:", c)
```

### 🔑 Key Points
- Compare the **first value against both others** using `and`.
- If that fails, the largest must be **among the remaining two** — so only one more comparison is needed.
- This pattern (eliminate one option at a time) is a common interview logic-building trick.
