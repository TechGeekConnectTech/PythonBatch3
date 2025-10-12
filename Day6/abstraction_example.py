from abc import ABC, abstractmethod 

class Payment(ABC):
    @abstractmethod
    def make_payment(self, amount):
        pass

    def payment_status(self):
        return "Payment processed successfully."
    
class CreditCardPayment(Payment):
    def make_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")

class UPIpayment(Payment):
    def make_payment(self, amount):
        print(f"Processing UPI payment of ${amount}")

    def payment_status(self):
        return "UPI payment processed successfully."        


payment=CreditCardPayment()

payment.make_payment(150)

payment1=UPIpayment()
payment1.make_payment(200) 
print(payment1.payment_status())