<div align="center">

# NUMERICAL SOLVER

**A desktop application for numerical methods and mathematical computation.**

Python · PySide6 · NumPy · Excel export

</div>

---

## Overview

Numerical Solver is a desktop learning application for solving selected numerical-analysis problems through a graphical interface. It combines a PySide6 interface with separate Python modules for iterative linear-system methods and nonlinear equation solving.

The application is intended to support experimentation with numerical methods and inspectable calculation steps. Numerical output should be interpreted with the method's mathematical assumptions and convergence behavior in mind.

## Supported methods

| Method | Problem class | Implementation |
| --- | --- | --- |
| Jacobi | Linear systems | Iterative method |
| Gauss-Seidel | Linear systems | Iterative method |
| Gauss-Jordan | Linear systems | Direct elimination |
| Bisection | Nonlinear equations | Bracketing root method |
| Newton-Raphson | Nonlinear equations | Iterative root approximation using a numerical derivative |
| Regula Falsi | Nonlinear equations | Bracketing root method |

The source modules maintain calculation histories for methods that expose iteration or elimination steps. The interface also includes a menu action for exporting results to Excel.

## Technology

- Python
- PySide6 for the desktop interface.
- NumPy for matrix and vector operations.
- pandas and openpyxl for spreadsheet integration.
- Qt Designer UI definitions.

## Requirements

The repository does not currently include a root requirements.txt or pyproject.toml. Install the packages used by the source in a Python environment:

    python -m pip install PySide6 numpy pandas openpyxl

A supported Python version should be selected according to the PySide6 and NumPy releases installed on the development machine.

## Getting started

    git clone https://github.com/gusti111/Numerical_Solver_App.git
    cd Numerical_Solver_App

Create a virtual environment:

    python -m venv .venv

Windows:

    .venv\Scripts\activate

macOS / Linux:

    source .venv/bin/activate

Install the application dependencies and launch:

    python -m pip install PySide6 numpy pandas openpyxl
    python main.py

## Repository structure

    Numerical_Solver_App/
    ├── Rumus/
    │   ├── jacobi.py
    │   ├── gauss_seidel.py
    │   ├── gauss_jordan.py
    │   ├── bisection.py
    │   ├── newton.py
    │   └── regulafalsi.py
    ├── Excel/             # Example workbooks and method references
    ├── Laporan/           # Project reports and supporting material
    ├── main.py            # Application entry point
    ├── mainMenu.ui        # Qt Designer interface
    └── ui_mainMenu.py     # Generated UI binding

## Mathematical considerations

- Jacobi and Gauss-Seidel convergence depends on the properties of the coefficient matrix and the initial approximation.
- Bisection and Regula Falsi require an interval that brackets a root under the method's assumptions.
- Newton-Raphson can fail when the derivative is near zero or when the initial guess is unsuitable.
- A maximum-iteration result is not automatically a valid solution; inspect the final error and method status.
- Verify important results independently, particularly when using rounded or poorly conditioned input data.

The function evaluators in the current source use Python eval to process mathematical expression strings. This is not a security sandbox; do not pass untrusted expressions to it. Replace it with a dedicated allowlisted expression parser before exposing the functionality through a public service.

## Project status

An academic numerical-computing project. The repository currently contains generated build and Python bytecode artifacts; these should be reviewed and excluded from source control where they are reproducible.

## Author

**Gusty Faqikh** · [GitHub](https://github.com/gusti111)