# Tower of Hanoi

###### Technologies:
<p align="center">
<img src="https://img.icons8.com/color/75/000000/python.png" width="75" height="75" alt="Python" style="margin: 10px 15px 0 15px;" />
</p>

### Try it!

To run the Tower of Hanoi application, follow the instructions in the Setup section below.

## Project Structure

- `recursive_solution.py`: Contains the recursive implementation of the Tower of Hanoi solution.
- `iterative_solution.py`: Contains the iterative implementation of the Tower of Hanoi solution.

## Setup

### Prerequisites

- Python 3 installed

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/creinis/tower-of-hanoi-fcc-scicomp-py-cert.git
   cd tower-of-hanoi-fcc-scicomp-py-cert
   ```

2. Run the Tower of Hanoi script:
   - For the recursive solution:
     ```bash
     python3 recursive_solution.py
     ```
   - For the iterative solution:
     ```bash
     python3 iterative_solution.py
     ```

## Tower of Hanoi

### Functionality

The Tower of Hanoi project solves the classic Tower of Hanoi problem using both recursive and iterative approaches. The goal is to move a stack of disks from one rod to another, following specific rules.

### Practical Use Case

The Tower of Hanoi problem is a classic example used in computer science to teach recursion and algorithmic thinking. It can be applied in understanding recursive problem-solving techniques and in optimizing algorithms for various computational problems.

### Benefits

- **Two Approaches:** Demonstrates both recursive and iterative solutions to the Tower of Hanoi problem.
- **Educational:** Provides a clear understanding of recursion and iterative algorithm design.
- **Python Standard Library:** Utilizes Python’s built-in data structures for implementation.

## How to Use

1. Run the `recursive_solution.py` script:
   ```bash
   python3 recursive_solution.py
   ```
2. Run the `iterative_solution.py` script:
   ```bash
   python3 iterative_solution.py
   ```

### Example Usage (Recursive)

```python
from recursive_solution import move

NUMBER_OF_DISKS = 5
A = list(range(NUMBER_OF_DISKS, 0, -1))
B = []
C = []

move(NUMBER_OF_DISKS, A, B, C)
```

### Example Usage (Iterative)

```python
from iterative_solution import move

NUMBER_OF_DISKS = 4
move(NUMBER_OF_DISKS, 'A', 'B', 'C')
```

### Example Output

```plaintext
Recursive Solution:
[A] [B] [C]
[2, 1] [3] [5, 4]
...

Iterative Solution:
Moving disk 1 from A to C
Moving disk 2 from A to B
Moving disk 1 from C to B
...
```

## Function Parameters

- `move` (Recursive):
  - `n`: Number of disks to move.
  - `source`: The source rod.
  - `auxiliary`: The auxiliary rod.
  - `target`: The target rod.

- `move` (Iterative):
  - `n`: Number of disks to move.
  - `source`: The source rod.
  - `auxiliary`: The auxiliary rod.
  - `target`: The target rod.

### Constraints

- Only one disk can be moved at a time.
- A disk can only be placed on top of a larger disk or on an empty rod.

### Comparison of Approaches

- **Recursive Approach:**
  - Uses the call stack to remember previous states.
  - Elegant and concise but can be less efficient for large numbers of disks due to deep recursion.

- **Iterative Approach:**
  - Uses loops and explicit data structures to manage state.
  - More complex to implement but avoids deep recursion and stack overflow issues for large numbers of disks.

---
#### This is a FreeCodeCamp Challenge for Scientific Computing with Python Projects Certification.
<p align="center">
<img src="https://cdn.freecodecamp.org/platform/universal/fcc_primary.svg" width="250" height="75" alt="freeCodeCamp" style="margin: 0 15px; opacity: 0.6" />
</p>
