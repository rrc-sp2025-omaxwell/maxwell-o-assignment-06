__author__ = "Owen Maxwell"
__version__ = "1.0.0"

from mortgage.mortgage import Mortgage
from mortgage.payment_frequency import PaymentFrequency


import unittest
# (self, loan_amount: float, annual_interest_rate: float,
                  #amortization: int, frequency: PaymentFrequency)
class TestMortgage(unittest.TestCase):
    """
    
    """
    def loan_amount_typeerror(self):
        # Arrange
        loan_amount = "not int or float"
        annual_interest_rate = 0.5
        amortization = 5
        frequency = PaymentFrequency.WEEKLY

        expected = "Loan amount must be a value of a numeric type."

        # act and assert
        with self.assertRaises(TypeError) as context:
            Mortgage(loan_amount, annual_interest_rate, amortization, frequency)
        self.assertEqual(expected, str(context.exception))