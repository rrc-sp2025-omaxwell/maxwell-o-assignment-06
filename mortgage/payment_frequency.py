__author__ = "Owen Maxwell"
__version__ = "1.0.0"


from enum import Enum

class PaymentFrequency(Enum):
    """Representing the options available for payment frequency."""

    MONTHLY = 12
    BI_WEEKLY = 26
    WEEKLY = 52