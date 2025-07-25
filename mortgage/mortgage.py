
__author__ = "Owen Maxwell"
__version__ = "1.0.0"

from payment_frequency import PaymentFrequency

class Mortgage:
    """
    """

    # list containing the years a mortgage can
    #  be amortized (payed over) for.
    
    

    def __init__(self, loan_amount: float, annual_interest_rate: float,
                  amortization: int, frequency: PaymentFrequency):
        
        amortization_list = [5, 10, 15, 20, 25, 30]
        
        # Verify if loan_amount is valid
        try:
            loan_amount = float(loan_amount) or int(loan_amount)
        except TypeError:
            raise TypeError("Loan amount must be a value of a numeric type.")
        
        if loan_amount <= 0:
            raise ValueError("Loan Amount must be a value greater than zero.")
        
            

        # Verify if annual_interest_rate is valid
        try:
            annual_interest_rate = float(annual_interest_rate) or int(annual_interest_rate)
        except TypeError:
            raise TypeError("Annual Interest Rate must be a value of a numeric type.")
        
        if annual_interest_rate <= 0 or annual_interest_rate > 1:
            raise ValueError("Annual interest rate must be a value" \
            " greater than zero and less than or equal to 1.")
        

        # Verify if amortization is valid
        
        if amortization not in amortization_list:
            raise ValueError("Amortization must be a value in [5, 10, 15, 20, 25, 30].")
        
        # Verify if frequency is valid

        if frequency not in PaymentFrequency:
            raise ValueError("Frequency must be a value of PaymentFrequency type.")
        
        self.loan_amount = loan_amount
        self.annual_interest_rate = annual_interest_rate
        self.amortization = amortization
        self.frequency = frequency

    

