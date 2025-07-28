
__author__ = "Owen Maxwell"
__version__ = "1.0.0"


from mortgage.payment_frequency import PaymentFrequency

class Mortgage:
    """
    """

    # list containing the years a mortgage can
    #  be amortized (payed over) for.
    
    amortization_list = [5, 10, 15, 20, 25, 30]    

    def __init__(self, loan_amount: float, annual_interest_rate: float,
                  amortization: int, frequency: PaymentFrequency):
        
        # Verify if loan_amount is valid
        if not isinstance(loan_amount, (int, float)):
            raise TypeError ("Loan amount must be a value of a numeric type.")
        
        if loan_amount <= 0:
            raise ValueError("Loan Amount must be a value greater than zero.")
        

        # Verify if annual_interest_rate is valid
    
        if not isinstance(annual_interest_rate, (int, float)):
            raise TypeError("Annual Interest Rate must be a value of a numeric type.")
        
        if annual_interest_rate <= 0:
            raise ValueError("Annual interest rate must be a value" \
            " greater than zero and less than or equal to 1.")
        
        if annual_interest_rate > 1:
            raise ValueError("Annual interest rate cannot be a value greater than 1.")


        # Verify if amortization is valid
        
        if amortization not in Mortgage.amortization_list:
            raise ValueError("Amortization must be a value in [5, 10, 15, 20, 25, 30].")

        
        # Verify if frequency is valid

        if frequency not in PaymentFrequency:
            raise ValueError("Frequency must be a value of PaymentFrequency type.")
        
        self.__loan_amount = loan_amount
        self.__annual_interest_rate = annual_interest_rate
        self.__amortization = amortization
        self.__frequency = frequency

    # def accessors and mutators for loan_amount
    # accessor
    @property
    def loan_amount(self) -> float:
        """ Gets the amount for the loan.

        Returns:
            float: the value amount of the loan.
        """
        
        return self.__loan_amount

    # mutator
    @loan_amount.setter
    def loan_amount(self, loan_amount: float) -> None:
        """ mutator for loan amount.
        
        Args: 
            loan_amount (float): a float representing the amount of the loan.

        Raises:
            TypeError: Raised when type isn't numeric.
            ValueError: Raised when value is less than or equal to zero.
        """

        # Verify if loan_amount is valid
        if not isinstance(loan_amount, (int, float)):
            raise TypeError ("Loan amount must be a value of a numeric type.")

        if loan_amount <= 0:
            raise ValueError("Loan Amount must be a value greater than zero.")
        
        self.__loan_amount = loan_amount
        
    # def accessor and mutator for annual interest rate
    # accessor
    @property
    def annual_interest_rate(self) -> float:
        """Gets the amount of the annual interest rate

        Returns:
            float: amount of annual interest rate
        
        """

        return self.__annual_interest_rate
    
    # mutator
    @annual_interest_rate.setter
    def annual_interest_rate(self, annual_interest_rate: float) -> None:
        """Mutator for amount of the annual interest rate

        Args: annual_interest_rate(float): a float representing annual_interest_rate

        Raises:       
            TypeError: Raised when type is non numeric.
            ValueError: Raised whe value is less than or equal to zero,
            or when value is greater than one.
        """

        # verify if annual_interest_rate is valid
        if not isinstance(annual_interest_rate, (int, float)):
            raise TypeError("Annual Interest Rate must be a value of a numeric type.")
        
        if annual_interest_rate <= 0:
            raise ValueError("Annual interest rate must be a value" \
            " greater than zero and less than or equal to 1.")
        
        if annual_interest_rate > 1:
            raise ValueError("Annual interest rate cannot be a value greater than 1.")
    
        self.__annual_interest_rate = annual_interest_rate
   
    # def accessor and mutator for amortization
    # accessor
    @property
    def amortization(self) -> int:
        """ Gets the value of the amortization for mortgage.

        Returns:
            int: value of amortization
        """
        return self.__amortization

    # mutator
    @amortization.setter
    def amortization(self, amortization: int) -> None:
        """ Mutator for value of amortization.

        Args:
            amortization(int): an integer value representing amortization.

        Raises:
            ValueError: If value is not in amortization list.
        """

        if amortization not in Mortgage.amortization_list:
            raise ValueError("Amortization must be a value in [5, 10, 15, 20, 25, 30].")
        
        self.__amortization = amortization

    
    # def accessor and mutators for frequency
    
    # accessor
    @property
    def frequency(self) -> int:
        """Returns a value corresponding to frequency of payments.

        Returns:
            int: value in the amount of times a payment will be made.        
        """
        return self.__frequency

    @frequency.setter
    def frequency(self, frequency: int) -> None:
        """
        
        """

        if frequency not in PaymentFrequency:
            raise ValueError("Frequency must be a value of PaymentFrequency type.")

        self.__frequency = frequency


    # repr
    def __repr__(self) -> str:
        """Returns a string representation of the object.

        Returns:
            str: string representation of the object

        Example:
            >>> Mortgage()
        """

        return (f"{self.loan_amount} | "
                + f"{self.annual_interest_rate} | "
                + f"{self.amortization} | "
                + f"{self.frequency}")
