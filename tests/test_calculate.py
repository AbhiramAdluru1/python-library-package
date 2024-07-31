import unittest
from policy_calculator import calculate_policy_price

class TestPolicyCalculator(unittest.TestCase):

    def test_calculate_policy_price(self):
        result = calculate_policy_price(
            original_policy_price=1000.0,
            age=45,
            height=160.0,
            weight=80.0,
            does_smoke=True,
            does_drink=False,
            has_diabetes=True,
            had_any_surgery=False
        )
        self.assertAlmostEqual(result, 1150.0)

if __name__ == '__main__':
    unittest.main()
