#!/usr/bin/env python3
"""
N-Queens Problem Solver using SAT
This program determines the number of possible solutions to the N-Queens problem
using an incremental SAT solver.
"""

from pysat.solvers import Glucose3, Minisat22, Cadical103
from pysat.formula import CNF
import sys


def queens(N, solver_name="glucose3"):
    """
    Solve the N-Queens problem using an incremental SAT solver.
    
    Args:
        N (int): Size of the chessboard (N x N) and number of queens
        solver_name (str): SAT solver to use ("glucose3", "minisat", or "cadical")
        
    Returns:
        int: Number of satisfying assignments (solutions)
    """
    if N <= 3:
        return 0
    
    # Variable encoding: var(i, j) represents a queen at position (i, j)
    # We'll use 1-based indexing for variables as required by SAT solvers
    def var(i, j):
        return i * N + j + 1
    
    # Create CNF formula
    cnf = CNF()
    
    # Constraint 1: Exactly one queen per row
    for i in range(N):
        # At least one queen per row
        row_clause = [var(i, j) for j in range(N)]
        cnf.append(row_clause)
        
        # At most one queen per row
        for j1 in range(N):
            for j2 in range(j1 + 1, N):
                cnf.append([-var(i, j1), -var(i, j2)])
    
    # Constraint 2: At most one queen per column
    for j in range(N):
        for i1 in range(N):
            for i2 in range(i1 + 1, N):
                cnf.append([-var(i1, j), -var(i2, j)])
    
    # Constraint 3: At most one queen per main diagonal (top-left to bottom-right)
    # Diagonals are characterized by i - j = constant
    for d in range(-(N-1), N):
        diagonal_vars = []
        for i in range(N):
            j = i - d
            if 0 <= j < N:
                diagonal_vars.append(var(i, j))
        
        # Add pairwise constraints for this diagonal
        for k1 in range(len(diagonal_vars)):
            for k2 in range(k1 + 1, len(diagonal_vars)):
                cnf.append([-diagonal_vars[k1], -diagonal_vars[k2]])
    
    # Constraint 4: At most one queen per anti-diagonal (top-right to bottom-left)
    # Anti-diagonals are characterized by i + j = constant
    for d in range(2 * N - 1):
        anti_diagonal_vars = []
        for i in range(N):
            j = d - i
            if 0 <= j < N:
                anti_diagonal_vars.append(var(i, j))
        
        # Add pairwise constraints for this anti-diagonal
        for k1 in range(len(anti_diagonal_vars)):
            for k2 in range(k1 + 1, len(anti_diagonal_vars)):
                cnf.append([-anti_diagonal_vars[k1], -anti_diagonal_vars[k2]])
    
    # Initialize incremental SAT solver based on choice
    solver_map = {
        "glucose3": Glucose3,
        "minisat": Minisat22,
        "cadical": Cadical103
    }
    
    if solver_name.lower() not in solver_map:
        solver_name = "glucose3"  # default fallback
    
    solver = solver_map[solver_name.lower()]()
    
    # Add all initial clauses to the incremental solver
    for clause in cnf.clauses:
        solver.add_clause(clause)
    
    solution_count = 0
    
    # Incrementally enumerate all solutions using blocking clauses
    while solver.solve():
        solution_count += 1
        model = solver.get_model()
        
        # Create blocking clause: negate all positive literals in current model
        # This incrementally adds constraints to exclude found solutions
        blocking_clause = []
        for lit in model:
            if lit > 0:
                blocking_clause.append(-lit)
            else:
                blocking_clause.append(-lit)
        
        # Incrementally add the blocking clause to exclude this solution
        solver.add_clause(blocking_clause)
    
    solver.delete()
    return solution_count


def print_solution(N, model):
    """
    Print a visual representation of a solution.
    
    Args:
        N (int): Board size
        model (list): SAT model (variable assignments)
    """
    def var(i, j):
        return i * N + j + 1
    
    print(f"Solution for {N}x{N} board:")
    board = [['.' for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if var(i, j) in model:
                board[i][j] = 'Q'
    
    for row in board:
        print(' '.join(row))
    print()


def main():
    """Main function to test the N-Queens solver."""
    if len(sys.argv) < 2:
        print("Usage: python queens.py N [solver]")
        print("Where N > 3 is the size of the chessboard")
        print("Optional solver: glucose3 (default), minisat, or cadical")
        sys.exit(1)
    
    try:
        N = int(sys.argv[1])
        if N <= 3:
            print(f"N must be greater than 3. Got N = {N}")
            sys.exit(1)
        
        # Get solver choice from command line (optional)
        solver_name = "glucose3"  # default
        if len(sys.argv) > 2:
            solver_name = sys.argv[2].lower()
            if solver_name not in ["glucose3", "minisat", "cadical"]:
                print(f"Unknown solver '{solver_name}'. Using glucose3.")
                solver_name = "glucose3"
        
        print(f"Solving {N}-Queens problem using incremental {solver_name.upper()} SAT solver...")
        result = queens(N, solver_name)
        print(f"Number of solutions for {N}-Queens: {result}")
        
        # For verification, print known results for small N
        known_results = {4: 2, 5: 10, 6: 4, 7: 40, 8: 92}
        if N in known_results:
            expected = known_results[N]
            if result == expected:
                print(f"✓ Result matches known value: {expected}")
            else:
                print(f"✗ Result {result} doesn't match known value: {expected}")
        
    except ValueError:
        print("Please provide a valid integer for N")
        sys.exit(1)


if __name__ == "__main__":
    main()
    