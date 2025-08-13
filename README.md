# N-Queens Problem Solver using SAT

This Python program computes the number of solutions to the **N-Queens problem** using an **incremental SAT solver**. It supports multiple SAT solvers and can enumerate all solutions for a given board size \(N > 3\).

---

## Table of Contents

- [Overview](#overview)  
- [Features](#features)  
- [Dependencies](#dependencies)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Execution Examples](#execution-examples)  
- [Source Code](#source-code)  
- [Notes](#notes)

---

## Overview

The N-Queens problem requires placing N queens on an N×N chessboard such that no two queens attack each other. This solver:

- Encodes the problem as a CNF formula.
- Uses an **incremental SAT solver** to enumerate all valid solutions.
- Supports **Glucose3**, **MiniSat**, or **CaDiCaL** as the backend SAT solver.

---

## Features

- Supports variable board sizes (\(N > 3\)).  
- Incrementally enumerates all possible solutions.  
- Optional visual representation of a solution.  
- Cross-verifies results against known small N solutions.

---

## Dependencies

- Python 3.8+  
- [PySAT](https://pysathq.github.io/) Python library

```bash
pip install python-sat[pblib,aiger]
 ```

## Supported SAT Solvers

This program supports the following SAT solvers through PySAT:

- **Glucose3** (default)
- **MiniSat**
- **CaDiCaL**

> **Note:** The source code of the SAT solvers is **not included**. PySAT provides Python bindings to the solvers.

---

## Installation

1. Clone this repository:

```bash
git clone https://github.com/<your-username>/nqueens-sat.git
cd nqueens-sat
 ```
2. Install dependencies:
```bash
pip install python-sat[pblib,aiger]
```

## Usage

Run the program via the command line:

```bash
python queens.py N [solver]
```

## Execution example
$ python queens.py 4
Solving 4-Queens problem using incremental GLUCOSE3 SAT solver...
Number of solutions for 4-Queens: 2
✓ Result matches known value: 2



$ python queens.py 8 cadical
Solving 8-Queens problem using incremental CADICAL SAT solver...
Number of solutions for 8-Queens: 92
✓ Result matches known value: 92






