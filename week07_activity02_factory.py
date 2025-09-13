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

# This function does not know about any specific payment class, it only communicates with the PaymentFactory.    
def checkout(payment_method: str, amount: int):
    # Request a suitable payment processor instance from the factory
    processor = PaymentFactory.create_processor(payment_method)
    # Use the processor instance returned by the factory to complete the payment and return the result
    return processor.process_payment(amount)
    
if __name__ == "__main__":
    # Call different classes for demonstration
    print(checkout("paypal", 100))
    print(checkout("stripe", 50))
    print(checkout("credit_card", 200))
