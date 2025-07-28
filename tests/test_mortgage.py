__author__ = "Owen Maxwell"
__version__ = "1.0.0"

import sys
import os
sys.path.append('maxwell-o-assignment-06')
from mortgage.mortgage import Mortgage
from mortgage.payment_frequency import PaymentFrequency

import unittest

# (self, loan_amount: float, annual_interest_rate: float,
                  #amortization: int, frequency: PaymentFrequency)
class TestMortgage(unittest.TestCase):
    
    # 1, TypeError when loan amount is not numeric
    def test_loan_amount_typeerror(self):
        # Arrange
        loan_amount = "not int or float"
        annual_interest_rate = 0.5
        amortization = 5
        frequency = PaymentFrequency.MONTHLY

        expected = "Loan amount must be a value of a numeric type."

        # act and assert
        with self.assertRaises(TypeError) as context:
            Mortgage(loan_amount, annual_interest_rate, amortization, frequency)
            
        self.assertEqual(expected, str(context.exception))

    # 2, ValueError when loan amount is 0
    def test_loan_amount_zero(self):
            # Arrange
            loan_amount = 0
            annual_interest_rate = 0.5
            amortization = 5
            frequency = PaymentFrequency.MONTHLY

            expected = "Loan Amount must be a value greater than zero."

            # act and assert
            with self.assertRaises(ValueError) as context:
                Mortgage(loan_amount, annual_interest_rate, amortization, frequency)
                
            self.assertEqual(expected, str(context.exception))

    # 3, ValueError when loan amount is less than 0
    def test_loan_amount_negative(self):
            # Arrange
            loan_amount = -5
            annual_interest_rate = 0.5
            amortization = 5
            frequency = PaymentFrequency.MONTHLY

            expected = "Loan Amount must be a value greater than zero."

            # act and assert
            with self.assertRaises(ValueError) as context:
                Mortgage(loan_amount, annual_interest_rate, amortization, frequency)
                
            self.assertEqual(expected, str(context.exception))

    # 4, TypeError when interest rate is not numeric
    def test_interest_rate_typeerror(self):
        # Arrange
        loan_amount = 10
        annual_interest_rate = "not int or float"
        amortization = 5
        frequency = PaymentFrequency.MONTHLY
        expected = "Annual Interest Rate must be a value of a numeric type."

        # act and assert
        with self.assertRaises(TypeError) as context:
            Mortgage(loan_amount, annual_interest_rate, amortization, frequency)
            
        self.assertEqual(expected, str(context.exception))

    # 5, ValueError when interest rate is less than zero
    def test_interest_rate_negative(self):
        # Arrange
        loan_amount = 10
        annual_interest_rate = -1
        amortization = 5
        frequency = PaymentFrequency.MONTHLY

        expected = "Annual interest rate must be a value" \
            " greater than zero and less than or equal to 1."

        # act and assert
        with self.assertRaises(ValueError) as context:
            Mortgage(loan_amount, annual_interest_rate, amortization, frequency)
            
        self.assertEqual(expected, str(context.exception))

    # 6, ValueError when interest rate zero
    def test_interest_rate_zero(self):
        # Arrange
        loan_amount = 10
        annual_interest_rate = 0
        amortization = 5
        frequency = PaymentFrequency.MONTHLY

        expected = "Annual interest rate must be a value" \
            " greater than zero and less than or equal to 1."

        # act and assert
        with self.assertRaises(ValueError) as context:
            Mortgage(loan_amount, annual_interest_rate, amortization, frequency)
            
        self.assertEqual(expected, str(context.exception))

    # 7, ValueError when interest rate is greater than 1
    def test_interest_rate_greater_than_one(self):
        # Arrange
        loan_amount = 10
        annual_interest_rate = 2
        amortization = 5
        frequency = PaymentFrequency.MONTHLY

        expected = "Annual interest rate cannot be a value greater than 1."

        # act and assert
        with self.assertRaises(ValueError) as context:
            Mortgage(loan_amount, annual_interest_rate, amortization, frequency)
            
        self.assertEqual(expected, str(context.exception))

    # 8, ValueError when amortization is invalid
    def test_amortization_invalid(self):
        # Arrange
        loan_amount = 10
        annual_interest_rate = 0.5
        amortization = 3
        frequency = PaymentFrequency.MONTHLY

        expected = "Amortization must be a value in [5, 10, 15, 20, 25, 30]."

        # act and assert
        with self.assertRaises(ValueError) as context:
            Mortgage(loan_amount, annual_interest_rate, amortization, frequency)
            
        self.assertEqual(expected, str(context.exception))

    # 9, ValueError when frequency is invalid
    def test_frequency_invalid(self):
        # Arrange
        loan_amount = 10
        annual_interest_rate = 0.5
        amortization = 5
        frequency = "daily"

        expected = "Frequency must be a value of PaymentFrequency type."

        # act and assert
        with self.assertRaises(ValueError) as context:
            Mortgage(loan_amount, annual_interest_rate, amortization, frequency)
            
        self.assertEqual(expected, str(context.exception))

    # 10, test to ensure __init__ initializes attributes
    def test_mortgage_init_valid(self):
        # Arrange
        loan_amount = 10
        annual_interest_rate = 0.5
        amortization = 5
        frequency = PaymentFrequency.MONTHLY

        # Act
        mortgage = Mortgage(loan_amount, annual_interest_rate, amortization, frequency)

        # Assert
        self.assertEqual(mortgage.loan_amount, loan_amount)
        self.assertEqual(mortgage.annual_interest_rate, annual_interest_rate)
        self.assertEqual(mortgage.amortization, amortization)
        self.assertEqual(mortgage.frequency, frequency)
    
    #-------------------------------------------------------
    # Accessor and Mutator testing

    # loan_amount accessor/mutator unittesting

    # non-numeric
    def test_loan_amount_mutator_not_numeric(self):
        # Arrange
        mortgage = Mortgage(5, 0.5, 5, PaymentFrequency.MONTHLY)
        expected = "Loan amount must be a value of a numeric type."
    
        # act and assert
        with self.assertRaises(TypeError) as context:
            mortgage.loan_amount = "INVALID"
        self.assertEqual(expected, str(context.exception))
    
    # amount zero
    def test_loan_amount_mutator_amount_zero(self):
        # Arrange
        mortgage = Mortgage(5, 0.5, 5, PaymentFrequency.MONTHLY)
        expected = "Loan Amount must be a value greater than zero."
    
        # act and assert
        with self.assertRaises(ValueError) as context:
            mortgage.loan_amount = 0
        self.assertEqual(expected, str(context.exception))

    # amount less than zero
    def test_loan_amount_mutator_less_than_zero(self):
        # Arrange
        mortgage = Mortgage(5, 0.5, 5, PaymentFrequency.MONTHLY)
        expected = "Loan Amount must be a value greater than zero."
    
        # act and assert
        with self.assertRaises(ValueError) as context:
            mortgage.loan_amount = -5
        self.assertEqual(expected, str(context.exception))

    # updates current state
    def test_loan_amount_mutator_update_state(self):
        # Arrange
        mortgage = Mortgage(5, 0.5, 5, PaymentFrequency.MONTHLY)
        expected = 10
    
        # Act
        mortgage.loan_amount = 10
        # Assert
        self.assertEqual(expected, mortgage.loan_amount)

    # returns current state
    def test_loan_amount_accessor_state(self):
        # Arrange and Act
        mortgage = Mortgage(10, 0.5, 5, PaymentFrequency.MONTHLY)
        
        # Assert
        self.assertEqual (mortgage.loan_amount, 10)
    
    #-------------------------------------------------------
    # annual_interest_rate accessor/mutator unittesting
    def test_interest_rate_not_numeric(self):
        # Arrange
        mortgage = Mortgage(5, 0.5, 5, PaymentFrequency.MONTHLY)
        expected = "Annual Interest Rate must be a value of a numeric type."

        # act and assert
        with self.assertRaises(TypeError) as context:
            mortgage.annual_interest_rate = "INVALID"
        self.assertEqual(expected, str(context.exception))



