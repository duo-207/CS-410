# This is a sample Python script.
from typing import Union, Tuple


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def solve_quadratic_equation(a: float, b: float, c: float) -> Union[str, tuple]:
    """
    *************************************************************************
    Solves quadratic equations with the form ax^2 + bx + c = 0.
    Inputs:
        a (float): Coefficient of x^2
        b (float): Coefficient of x
        c (float): Constant

    Returns:
        Str include message indicating the situation of solutions
        Or tuple with the solutions of the equation.
    *************************************************************************
    """
    if a == 0:  # Reduce to linear equation when a = 0
        if b == 0:
            if c == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            return (-c / b,)

    delta = b**2 - 4 * a * c  # The discrimination D = b^2 - 4ac
    if delta > 0:  # D > 0, two real solutions
        root1 = (-b + delta ** 0.5) / (2 * a)  # x1 = (-b + D^1/2) / 2a
        root2 = (-b - delta ** 0.5) / (2 * a)  # x2 = (-b - D^1/2) / 2a
        return root1, root2
    elif delta == 0:  # D = 0, one real solution
        root3 = -b / (2 * a)  # x1 = x2 = - b / 2a
        return (root3,)
    else:  # D < 0, no real solutions, or two imaginary solution
        return "No real solution"


# Example
# print(solve_quadratic_equation(1, -3, 2))
# Equation: x^2 - 3x + 2 = 0,  Outputs: (2.0, 1.0)
