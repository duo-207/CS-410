import unittest

from main import solve_quadratic_equation


class MyTestCase(unittest.TestCase):
    def test_linear_equation(self):  # 4x - 8 = 0; x = 2
        self.assertEqual(solve_quadratic_equation(0, 4, -8), (2.0,))

    def test_quadratic_positive_delta(self):  # x^2 - 5x + 6 = 0; x1 = 2, x2 = 3
        # since both of (2.0,3.0) and (3.0,2.0) is correct. using set is a better choice
        roots = set(solve_quadratic_equation(1, -5, 6))
        self.assertSetEqual(roots, {2.0, 3.0})

    def test_negative_coefficients(self):  # -x^2 - 5x - 6 = 0; x1 = -2, x2 = -3
        roots = set(solve_quadratic_equation(-1, -5, -6))
        self.assertSetEqual(roots, {-2.0, -3.0})

    def test_quadratic_zero_delta(self):  # x^2 - 6x + 9 = 0; x1 = x2 = 3
        self.assertEqual(solve_quadratic_equation(1, -6, 9), (3.0,))

    def test_quadratic_negative_delta(self):  # x^2 + 0*x + 1 = 0; no real solution
        self.assertEqual(solve_quadratic_equation(1, 0, 1), "No real solution")

    def test_all_zero_coefficients(self):  # 0*x^2 + 0*x + 0 = 0; Infinite solutions
        self.assertEqual(solve_quadratic_equation(0, 0, 0), "Infinite solutions")

    def test_quadratic_fractional_results(self):
        # 2x^2 - 3x + 1 = 0; (2x - 1) * (x - 1) = 0; x1 = 1/2, x2 = 1
        roots = solve_quadratic_equation(2, -3, 1)
        self.assertAlmostEqual(roots[0], 1.0)
        self.assertAlmostEqual(roots[1], 0.5)

    def test_large_coefficients(self):  # 1e6*x^2 - 5e6*x + 6e6 = 0; x1 ≈ 3, x2 ≈ 2
        roots = solve_quadratic_equation(1e6, -5e6, 6e6)
        if not isinstance(roots, tuple):
            self.fail("Expected tuple of floats")
        else:
            self.assertTrue(2.0 <= min(roots) <= 3.0 and 2.0 <= max(roots) <= 3.0)

    def test_small_coefficients(self):  # 1e-6*x^2 - 5e-6*x + 6e-6 = 0; x1 ≈ 3, x2 ≈ 2
        roots = solve_quadratic_equation(1e6, -5e6, 6e6)
        if not isinstance(roots, tuple):
            self.fail("Expected tuple of floats")
        else:
            self.assertTrue(2.0 <= min(roots) <= 3.0 and 2.0 <= max(roots) <= 3.0)


if __name__ == '__main__':
    unittest.main()
