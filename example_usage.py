"""Example demonstrating Quadratic Programming solution."""
from client import ActiveSetQP

def main():
    Q = [[4.0, 0.0], [0.0, 2.0]]
    c = [-8.0, -6.0]
    sol = ActiveSetQP.solve_unconstrained(Q, c)
    print("Optimal QP Minimizer x*:", sol)

if __name__ == "__main__":
    main()
