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
