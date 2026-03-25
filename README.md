# Polynomial Addition Using Linked Lists (Python)

## 📌 Project Overview

This project implements **Polynomial Addition using Linked Lists** in Python. Each polynomial is represented as a linked list where every node stores a term consisting of a coefficient and its corresponding power.

The program allows users to input two polynomials dynamically and performs addition by combining like terms (same powers).

---

## 🎯 Objectives

* Represent polynomials using linked lists
* Perform addition of two polynomials
* Understand dynamic data structures in Python
* Practice traversal and manipulation of linked lists

---

## 🧠 Concept

A polynomial expression looks like:

3x³ + 5x² + 2x + 7

Each term contains:

* Coefficient → numerical value
* Power → exponent of variable

Using a linked list, each node stores:
(coefficient, power)

Example:
[3,3] → [5,2] → [2,1] → [7,0]

---

## ⚙️ Features

* User input for polynomial terms
* Dynamic creation of linked lists
* Efficient polynomial addition
* Clean and readable output format
* Object-Oriented implementation

---

## 🛠️ Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
* Linked List Data Structure

---

## 🚀 How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/polynomial-addition-linkedlist.git
```

2. Navigate to the project folder:

```bash
cd polynomial-addition-linkedlist
```

3. Run the program:

```bash
python main.py
```

---

## 🧪 Sample Input

Enter number of terms in Polynomial 1: 3
Enter coefficient: 3
Enter power: 3
Enter coefficient: 5
Enter power: 2
Enter coefficient: 6
Enter power: 0

Enter number of terms in Polynomial 2: 3
Enter coefficient: 6
Enter power: 3
Enter coefficient: 8
Enter power: 1
Enter coefficient: 4
Enter power: 0

---

## 📤 Sample Output

Polynomial 1:
3x^3 + 5x^2 + 6x^0

Polynomial 2:
6x^3 + 8x^1 + 4x^0

Result Polynomial after Addition:
9x^3 + 5x^2 + 8x^1 + 10x^0

---

## 📊 Time Complexity

| Operation | Complexity |
| --------- | ---------- |
| Insertion | O(n)       |
| Addition  | O(n)       |
| Traversal | O(n)       |

---

## ✅ Advantages

* Efficient for sparse polynomials
* Dynamic memory usage
* Easy insertion and manipulation

---

## ⚠️ Limitations

* Requires proper ordering of terms (descending powers)
* Slightly complex compared to arrays
* Traversal overhead for large polynomials

---

## 📚 Applications

* Computer Algebra Systems
* Scientific computations
* Signal processing
* Mathematical modeling

---

## 📌 Future Enhancements

* Polynomial subtraction and multiplication
* GUI-based interface
* Support for multiple variables (e.g., x, y)
* Sorting terms automatically

---

## 👩‍💻 Author

Suhani Pandey

---

## ⭐ Acknowledgment

This project was developed as part of academic learning to understand linked lists and polynomial operations.

---
