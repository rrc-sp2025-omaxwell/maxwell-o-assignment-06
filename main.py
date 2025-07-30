"""This module demonstrates your understanding of object-oriented
programming.

Below each of the comments, code the statement or statements to satisfy
the requirement specified in the comment.
"""

from mortgage.mortgage import Mortgage
from mortgage.payment_frequency import PaymentFrequency

__author__ = "Owen Maxwell"
__version__ = "1.0.0"
__credits__ = "COMP-1327 Faculty"


def main():

# 1. Create an instance of the Mortgage class. Initialize the object
#    using values of your choosing. NOTE: This object will be used for 
#    the following 4 questions.
    print("1st Instance")
    mortgage = Mortgage(123456.78, 0.03219, 10, PaymentFrequency.WEEKLY)

# 2. Print the official string representation of the object.
    print(mortgage)

# 3. Print the payment amount for the mortgage. Format the payment 
#    amount as currency.
    #payment_amount = mortgage.get_payment()
    print (f"${(mortgage.get_payment()):,.2f}")

# 4. Update the state of the object such that all attributes values are 
#    different than what they were initialized to.

    mortgage.loan_amount = 87654.32
    mortgage.annual_interest_rate = 0.1234
    mortgage.amortization = 15
    mortgage.frequency = PaymentFrequency.MONTHLY

# 5. Choose any attribute of the object and print it's current state.
    print (f"Amortization: {mortgage.amortization}")

# 6. Attempt to create another instance of the Mortgage class. The 
#    statement must use one value that will cause the initialization
#    to fail. Prevent the script from abnormally ending and print the
#    error message to the console.
    print("--------------------------------------------------")
    print("2nd Instance")

    # Attempting to initialize with an annual interest rate
    # greater than 1.

    try:
        mortgage2 = Mortgage(123456.78, 100, 10, PaymentFrequency.WEEKLY)
    except Exception as e:

        # prints out the specific error message, and also prints the name
        # of the Exception striped to only display the name.
        print(f"Error Message: {e}\nException Type: {str(type(e)).split("'")[1]}")

    print("--------------------------------------------------")    
    print("3rd Instance")

    # Attempting to initialize with a loan amount that is a 
    # string type value, "Money".

    try:
        mortgage3 = Mortgage("Money", 0.1234, 10, PaymentFrequency.WEEKLY)
    except Exception as e:
        print(f"Error Message: {e}\nException Type: {str(type(e)).split("'")[1]}")
    

if __name__ == "__main__":
    main()