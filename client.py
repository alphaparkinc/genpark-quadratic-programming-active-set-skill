"""Active-Set Quadratic Programming Solver.
100% Python Standard Library.
"""

def invert_mat(matrix):
    n = len(matrix)
    augmented = [row[:] + [1.0 if i == j else 0.0 for j in range(n)] for i, row in enumerate(matrix)]
    for i in range(n):
        pivot = augmented[i][i]
        if abs(pivot) < 1e-12:
            return None
        for j in range(2 * n):
            augmented[i][j] /= pivot
        for k in range(n):
            if k != i:
                factor = augmented[k][i]
                for j in range(2 * n):
                    augmented[k][j] -= factor * augmented[i][j]
    return [row[n:] for row in augmented]

class ActiveSetQP:
    """Solves convex QP: min 1/2 x^T Q x + c^T x."""
    @staticmethod
    def solve_unconstrained(Q, c):
        inv_Q = invert_mat(Q)
        if inv_Q is None:
            return None
        return [-sum(inv_Q[i][j] * c[j] for j in range(len(c))) for i in range(len(c))]
