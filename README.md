# Active-Set Quadratic Programming Skill

Direct Karush-Kuhn-Tucker (KKT) active-set quadratic programming solver for linear quadratic regulation (LQR) and model predictive control (MPC).

```mermaid
flowchart LR
    Costs["Hessian Q & Linear Vector c"] --> KKT["Assemble KKT System"]
    Constraints["Linear Constraints Ax <= b"] --> KKT
    KKT --> Solve["Direct Inversion / Active Elimination"]
    Solve --> Optimal["Optimal Primal x* and Multipliers λ*"]
```

## Features
- **100% Python Standard Library**: Pure analytical inversion.
- **Model Predictive Control Core**: Direct compatibility with robotic tracking problems.
