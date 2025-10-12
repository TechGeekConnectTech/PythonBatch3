class Payment:
    def pay(self,amount):
        raise NotImplementedError("Subclasses must implement this method")

class CreditCardPayment(Payment):
    def pay(self,amount):
        return f"Paid {amount} using Credit Card"

class DebitCardPayment(Payment):
    def pay(self,amount):
        return f"Paid {amount} using Debit Card"    

class UPIpayment(Payment):
    def pay(self,amount):
        return f"Paid {amount} using UPI"

def process_payment(payment_method,amount):
    print(payment_method.pay(amount))


# User selected credit card payment method
credit_card=CreditCardPayment()
debit_card=DebitCardPayment()
upi=UPIpayment()

process_payment(credit_card,1000) 
process_payment(debit_card,500)
process_payment(upi,200)