# 🐍 Python Lecture 3 — Lists & Tuples (Simple Notes)

---

## 1️⃣ Lists in Python

### 📖 Definition
A **list** is a data type in Python that can hold **many values together** in one place. It is like a box that can hold many items.

### 💡 Best Example (Why we need a list)
❌ **Bad way** — storing marks of 5 students one by one:
```python
marks1 = 94.4
marks2 = 87.0
marks3 = 95.0
marks4 = 66.0
marks5 = 45.1
```
This becomes hard if we have 100 students — too many names to remember!

✅ **Good way (using a list):**
```python
marks = [94.4, 87.0, 95.0, 66.0, 45.1]
print(marks)          # [94.4, 87.0, 95.0, 66.0, 45.1]
print(type(marks))    # <class 'list'>
```

### 🔑 Key Points
- Made using **square brackets `[ ]`**. Values are separated by **commas**.
- A list can hold **as many values as we want**.
- `type(list_name)` tells us it is a `list`.
- Lists work almost like strings (same index and slicing rules) but with some big differences.

---

## 2️⃣ A List Can Hold Different Types of Data

### 📖 Definition
In other languages, an array can only hold **one type** of data. But in Python, a list can hold **many different types together** — like text, numbers, all in one list.

### 💡 Best Example
```python
student = ["Karan", 94, "Delhi", 21]
# name (text), marks (number), city (text), age (number) — all in one list!
print(student)
print(type(student))   # <class 'list'>
```

### 🔑 Key Points
- No rule that all values must be the same type.
- We can mix text, numbers, decimals — even other lists — inside one list.

---

## 3️⃣ Index Number in a List

### 📖 Definition
Every value in a list has a **position number**, called an **index**. It starts from **0**. We use the index to get any value from the list.

### 💡 Best Example
```python
marks = [94.4, 87.0, 95.0, 66.0, 45.1]
print(marks[0])     # 94.4  (first value)
print(marks[1])     # 87.0
print(len(marks))   # 5     (total number of values)
```

### 🔑 Key Points
- Index always starts from **0**, not 1.
- `len(list_name)` tells us how many values are in the list.
- If we try to use an index that does not exist, we get an error:
  ```python
  marks[5]   # ❌ Error: list index out of range
  ```

---

## 4️⃣ Strings vs Lists — Can Change vs Cannot Change (⭐ Very Important)

### 📖 Definition
- **Strings cannot be changed** after we make them.
- **Lists CAN be changed** after we make them.

> 🧠 Simple way to remember: List = changeable box. String = fixed/locked box.

### 💡 Best Example (Comparing both)
```python
# STRING — cannot change
text = "Hello"
text[0] = "Y"        # ❌ Error: we cannot change a string like this

# LIST — can change
student = ["Karan", 94, "Delhi"]
student[0] = "Arjun"     # ✅ This works fine!
print(student)            # ['Arjun', 94, 'Delhi']
```

### 🔑 Key Points
- This is the **biggest difference** between a string and a list.
- Changing values inside a list is called **"changing the list."**
- We can update list values directly, but we can never update string values directly.

---

## 5️⃣ List Slicing (Taking a Part of a List)

### 📖 Definition
**Slicing** means taking out a **part** of a list using a start point and an end point. It works the same way as string slicing.

### 💡 Easy Example
```python
marks = [85, 94, 76, 63, 48]
print(marks[1:4])     # [94, 76, 63]  → index 1,2,3 (4 not included)
print(marks[:3])      # [85, 94, 76]  → no start = starts from 0
print(marks[2:])      # [76, 63, 48]  → no end = goes till last value
```

### 💡 Harder Example (Negative Index)
```python
marks = [85, 94, 76, 63, 48]
print(marks[-3:-1])    # [76, 63]   → -3 is 76, -2 is 63, -1(48) not included
```

### 🔑 Key Points
- We write it like: `list[start:end]`
- **Start point is included, end point is NOT included** — same rule as strings.
- If we don't give a start, it begins from 0.
- If we don't give an end, it goes till the last value.
- Negative index also works: `-1` = last value, `-2` = second-last value, etc.
- The small part we take out is called a **sub-list**.

---

## 6️⃣ List Methods — Full List

### 📖 Definition
**Methods** are ready-made actions we can use on a data type. List methods only work on lists (unlike `len()` or `print()`, which work on many things).

---

### ➕ `.append(value)` — Add a value at the END

**Definition:** Adds one value to the **end** of the list. This is called **changing the list.**

**Easy Example:**
```python
nums = [2, 1, 3]
nums.append(4)
print(nums)     # [2, 1, 3, 4]
```

**🔑 Key Points:**
- We can only add **ONE** value at a time.
- The list changes directly — no need to save it in a new variable.
- It does not give back anything useful (it gives `None`).

---

### 🔽 `.sort()` — Put the list in order

**Definition:** Arranges the values in the list in the correct order — small to big, by default.

**Easy Example (Numbers):**
```python
nums = [3, 1, 2]
nums.sort()
print(nums)              # [1, 2, 3]  (small to big — default)

nums.sort(reverse=True)  
print(nums)              # [3, 2, 1]  (big to small)
```

**Harder Example (Words — also get sorted A to Z):**
```python
fruits = ["banana", "apple", "litchi"]
fruits.sort()
print(fruits)     # ['apple', 'banana', 'litchi']   (A comes before B before L)

fruits.sort(reverse=True)
print(fruits)     # ['litchi', 'banana', 'apple']
```

**🔑 Key Points:**
- `list.sort()` **does NOT give back** the sorted list — it gives `None`.
  ```python
  print(nums.sort())   # None ❌ (a common mistake beginners make!)
  ```
- The list changes directly. So print the list **after** using sort:
  ```python
  nums.sort()
  print(nums)   # ✅ correct way
  ```
- To sort big to small, use `reverse=True` (capital **T** — small `true` gives an error).
- Sorting works on numbers as well as words (A to Z order for words).

---

### 🔄 `.reverse()` — Flip the whole list

**Definition:** Flips the order of all values in the list. It changes the original list directly.

**Easy Example:**
```python
letters = ["d", "e", "a", "c", "b"]
letters.reverse()
print(letters)      # ['b', 'c', 'a', 'e', 'd']
```

**🔑 Key Points:**
- It only flips the order — it does NOT put the list in sorted order.
- It changes the original list directly.

---

### 📍 `.insert(index, value)` — Add a value at a chosen spot

**Definition:** Adds a value at the index we choose. All values at that spot (and after) move one step to the right.

**Easy Example:**
```python
nums = [2, 1, 3]
nums.insert(1, 5)
print(nums)     # [2, 5, 1, 3]   → 5 added at index 1
```

**🔑 Key Points:**
- Takes **two things**: `insert(index, value)`.
- Like `.append()`, but we can choose **where** to add — not just the end.
- All values after that spot move one step right.

---

### ❌ `.remove(value)` — Remove first matching value

**Definition:** Finds the **first time** a value appears in the list and removes it.

**Easy Example:**
```python
nums = [2, 1, 3, 1]
nums.remove(1)
print(nums)     # [2, 3, 1]   → only the FIRST "1" is removed
```

**🔑 Key Points:**
- Removes by **value**, not by index.
- Removes only the **first match** — any other same values stay.
- If the value is not found, we get an error.

---

### 📤 `.pop(index)` — Remove a value at a chosen spot

**Definition:** Removes the value that is present at a chosen index.

**Easy Example:**
```python
nums = [2, 1, 3, 1]
nums.pop(2)
print(nums)     # [2, 1, 1]   → value at index 2 (which was 3) is removed
```

**🔑 Key Points:**
- Removes by **index**, not by value (opposite of `.remove()`).
- It also **gives back** the removed value, so we can save it if we want.

---

### 📋 `.copy()` — Make a copy of the list

**Definition:** Gives back a copy of the list, which we can save in another variable — useful when we don't want to touch the original list.

**Easy Example:**
```python
list1 = [1, 2, 3]
list2 = list1.copy()
print(list2)     # [1, 2, 3]  → same values, but a separate copy
```

### 🔢 `.count(value)` — Count how many times a value appears

**Definition:** Tells us how many times one value appears in the list.

**Easy Example:**
```python
nums = [1, 2, 2, 3, 2]
print(nums.count(2))    # 3
```

---

### 📊 Quick Table — List Methods

| Method | What it does | Example | Result |
|---|---|---|---|
| `.append(x)` | Add at the end | `[1,2].append(3)` | `[1,2,3]` |
| `.sort()` | Small to big order | `[3,1,2].sort()` | `[1,2,3]` |
| `.sort(reverse=True)` | Big to small order | `[1,2,3].sort(reverse=True)` | `[3,2,1]` |
| `.reverse()` | Flip the order | `[1,2,3].reverse()` | `[3,2,1]` |
| `.insert(i,x)` | Add at chosen spot | `[2,1,3].insert(1,5)` | `[2,5,1,3]` |
| `.remove(x)` | Remove first matching value | `[2,1,3,1].remove(1)` | `[2,3,1]` |
| `.pop(i)` | Remove value at index | `[2,1,3,1].pop(2)` | `[2,1,1]` |
| `.copy()` | Make a copy | `[1,2].copy()` | `[1,2]` |
| `.count(x)` | Count same values | `[1,2,2].count(2)` | `2` |

---

## 7️⃣ Tuples in Python

### 📖 Definition
A **tuple** is a data type like a list, but the big difference is: a **tuple cannot be changed** once we make it.

### 💡 Best Example
```python
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)      # made using ROUND brackets ( ) instead of [ ]
print(type(my_tuple))     # <class 'tuple'>
```

### 🔑 Key Points
- Made using **round brackets `( )`** instead of square brackets.
- Just like a list, a tuple can hold many types of data together.
- **Tuples cannot be changed** after we make them — no adding, removing, or updating values.
  ```python
  my_tuple[0] = 5   # ❌ Error: we cannot change a tuple
  ```

---

## 8️⃣ Different Ways to Make a Tuple

### 📖 Definition
We can make a tuple with no values, with one value, or with many values — each has its own small rule.

### 💡 Best Examples

**Empty tuple:**
```python
empty_tup = ()
print(type(empty_tup))    # <class 'tuple'>
```

**One-value tuple (⭐ tricky — comma is a MUST):**
```python
single = (1,)              # ✅ correct — the comma makes it a tuple
print(type(single))        # <class 'tuple'>

wrong = (1)                # ❌ no comma
print(type(wrong))         # <class 'int'>  → Python just sees it as a plain number!
```

**Many-value tuple:**
```python
multi = (1, 2, 3)          # comma at the end is not needed here
print(type(multi))         # <class 'tuple'>
```

### 🔑 Key Points
- A **one-value tuple must have a comma** after it, or Python will just see it as a normal value (number, decimal, text) — **not** a tuple.
- For many values, adding a comma at the end is **not compulsory**.
- This is one of the most common mistakes beginners make in Python!

---

## 9️⃣ Tuple Slicing

### 📖 Definition
Slicing on tuples works in the **same way** as it does for lists and strings.

### 💡 Best Example
```python
tup = (1, 2, 3, 4)
print(tup[1:3])     # (2, 3)   → index 1,2 (3 not included)
```

### 🔑 Key Points
- Same rule: `start` is included, `end` is not included.
- Gives back a **new tuple** — not a list.

---

## 🔟 Tuple Methods (Only 2 — since a tuple cannot change)

### 🔍 `.index(value)` — Find where a value first appears

**Definition:** Gives back the index where a value is **found first** in the tuple.

**Easy Example:**
```python
tup = (5, 1, 2, 1)
print(tup.index(1))    # 1   → value "1" is first found at index 1
print(tup.index(2))    # 2   → value "2" is found at index 2
```

### 🔢 `.count(value)` — Count how many times a value appears

**Definition:** Tells us how many times a value appears in the tuple.

**Easy Example:**
```python
tup = (5, 1, 2, 1)
print(tup.count(1))    # 2   → "1" appears two times
```

### 🔑 Key Points
- A tuple only has **2 methods** (`.index()` and `.count()`) because it cannot be changed — so there is no add, remove, or sort method.
- Both methods work in the same way as they do for lists.

---

## 1️⃣1️⃣ Practice Question 1 — Store 3 Favourite Movies in a List

### 📖 Problem
Ask the user for their 3 favourite movie names and save them in a list.

### 💡 Easy Solution (using separate variables)
```python
movie1 = input("Enter first movie: ")
movie2 = input("Enter second movie: ")
movie3 = input("Enter third movie: ")

movies = []                # empty list
movies.append(movie1)
movies.append(movie2)
movies.append(movie3)

print(movies)   # ['Shutter Island', 'Lucy', 'Primer']
```

### 💡 Shorter Solution (add directly, no extra variable)
```python
movies = []
movies.append(input("Enter first movie: "))
movies.append(input("Enter second movie: "))
movies.append(input("Enter third movie: "))

print(movies)
```

### 🔑 Key Points
- Start with an **empty list** `[]`, then use `.append()` to add values one by one.
- Adding values directly (`movies.append(input(...))`) saves us from making extra variables.

---

## 1️⃣2️⃣ Practice Question 2 — Check if a List is a Palindrome

### 📖 Problem
Write a program to check if a list reads the **same from front and back** (this is called a palindrome) or not.

**What is a Palindrome?**
Something that reads the **same forwards and backwards**.
- `"MAAM"` → Palindrome ✅
- `"RACECAR"` → Palindrome ✅
- `[1, 2, 3, 2, 1]` → Palindrome ✅
- `[1, 2, 3, 1, 2, 3]` → NOT a Palindrome ❌

### 💡 Steps (Hint: use `.copy()` + `.reverse()`)
1. Make a **copy** of the list.
2. **Flip (reverse)** the copy.
3. Check if the copy is same as the original — if yes, it's a Palindrome. If no, it's not.

### 💡 Easy Example (Palindrome list)
```python
list1 = [1, 2, 1]              # this is a palindrome list

copy_of_list1 = list1.copy()
copy_of_list1.reverse()

if copy_of_list1 == list1:
    print("Palindrome")
else:
    print("Not Palindrome")

# Output: Palindrome
```

### 💡 Harder Example (Not a Palindrome list)
```python
list2 = [1, 2, 3, 1, 2, 3]     # NOT a palindrome

copy_of_list2 = list2.copy()
copy_of_list2.reverse()

if copy_of_list2 == list2:
    print("Palindrome")
else:
    print("Not Palindrome")

# Output: Not Palindrome
```

### 🔑 Key Points
- We use `.copy()` so the **original list stays safe** while we test with the flipped one.
- `.reverse()` flips the copy directly — this is perfect for checking.
- Comparing the flipped copy with the original (`==`) tells us if it's a palindrome.
- This method (copy → flip → compare) is a common and easy way to check palindromes.

---

## 1️⃣3️⃣ Practice Question 3 — Count Students with Grade 'A' in a Tuple

### 📖 Problem
Given a tuple of grades, count how many students got Grade **'A'**. Then also change this into a list and put it in order from A to D.

### 💡 Easy Solution — Counting Grade A using tuple
```python
grades = ("C", "D", "A", "B", "A", "B", "A")

count_A = grades.count("A")
print(count_A)     # 3
```

### 💡 Harder Solution — Change Tuple → List → Sort (A to D)
```python
grades = ("C", "D", "A", "B", "A", "B", "A")

grade_list = list(grades)     # change tuple into a list (needed because we cannot sort a tuple directly)
grade_list.sort()             # small to big order = A to D (like A,B,C order)

print(grade_list)   # ['A', 'A', 'A', 'B', 'B', 'C', 'D']
```

### 🔑 Key Points
- `.count()` works directly on a tuple — no need to change it into a list.
- **We cannot sort a tuple directly** (because it cannot be changed) — first change it into a list using `list(tuple_name)`, then use `.sort()`.
- "A to D" order means **A, B, C, D order** (like small to big, but for letters).

---

## 📊 Simple Comparison Table — String vs List vs Tuple

| Feature | String | List | Tuple |
|---|---|---|---|
| Brackets used | `" "` / `' '` | `[ ]` | `( )` |
| Can change values? | ❌ No | ✅ Yes | ❌ No |
| Has index number | ✅ | ✅ | ✅ |
| Can be sliced | ✅ | ✅ | ✅ |
| Can hold mixed data types | ❌ (only letters) | ✅ | ✅ |
| Has `.sort()`, `.append()` etc. | ❌ | ✅ | ❌ (only `.index()`, `.count()`) |
| Negative index works | ✅ | ✅ | ✅ |
