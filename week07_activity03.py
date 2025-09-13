# ABC (Abstract Base Class) is used to create an abstract base class.
# abstractmethod is a decorator used to declare an abstract method that subclasses must implement.
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    # Defines an abstract payment method.
    # Subclasses must override this method to provide specific payment logic.
    @abstractmethod
    def process_payment(self, amount: int):
        pass

class PayPalPayment(PaymentProcessor):
    # The PayPal payment processor inherits PaymentProcessor and implements the specific process_payment method.
    def process_payment(self, amount: int):
        return f"Processing ${amount} via PayPal"

class StripePayment(PaymentProcessor):
    # Stripe payment processor
    def process_payment(self, amount: int):
        return f"Processing ${amount} via Stripe"

class CreditCardPayment(PaymentProcessor):
    #  Credit card payment processor
    def process_payment(self, amount: int):
        return f"Processing ${amount} via Credit Card"

class PaymentFactory:
    # Use a private dictionary `_processors` to register all available payment processors.
    # When adding new payment methods, simply modify this dictionary.
    _processors = {
        "paypal": PayPalPayment,
        "stripe": StripePayment,
        "credit_card": CreditCardPayment
    }

    # Class methods can be called directly via `PaymentFactory.create_processor()`, 
    # without first creating a factory instance `factory = PaymentFactory()`.
    #`cls` here represents the PaymentFactory class itself.
    @classmethod
    def create_processor(cls, payment_method: str) -> PaymentProcessor:

        # Convert the input string to lowercase, then safely look up the corresponding class in the handler dictionary and store the resulting class in a variable.
        processor_class = cls._processors.get(payment_method.lower())

        # No corresponding processor class was found, indicating that the payment method is not supported.
        if not processor_class:
            raise ValueError(f"Unknown payment method: {payment_method}")
        # Create an instance of it and return
        return processor_class()

class PaymentGateway:
    # Using singleton 
    _instance = None  # Used to store unique instance

    def __new__(cls, *args, **kwargs):
        # Using '__new__' to create new instance, early than '__init__'
        # If no instance currently
        if cls._instance is None:
            print("Create PaymentGateway new instance...")
            # create instance
            cls._instance = super().__new__(cls)
        else:
            print("Instance exists，return...")
        # return instance
        return cls._instance
    
    def __init__(self):
        pass
    
    def checkout(self, payment_method: str, amount: int):
        processor = PaymentFactory.create_processor(payment_method)
        return processor.process_payment(amount)
    
if __name__ == "__main__":
    # Call different classes for demonstration
    gw1 = PaymentGateway()
    print(gw1.checkout("paypal", 100))
    print(gw1.checkout("stripe", 50))
    print(gw1.checkout("credit_card", 200))
