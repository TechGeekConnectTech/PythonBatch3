class BankAccount:
    def __init__(self,account_number, initial_balance=0,account_name="Default Name"):
        self.account_number = account_number  # Public attribute 
        self.__balance = initial_balance      # Private attribute 
        self._account_name= account_name  # Protected attribute

    def deposit(self, amount):
        self.__balance = self.__balance + amount 

    def withdraw(self, amount):
        self.__balance = self.__balance - amount

    def get_account_info(self):
        return f"Account Holder: {self._account_name} is having Account Number: {self.account_number}, Balance: ${self.__balance}"    

class BranchDetails(BankAccount):
    def __init__(self, account_number, initial_balance=0, account_name="Default Name", branch_name="Default Branch"):
        super().__init__(account_number, initial_balance, account_name)
        self.branch_name = branch_name

    def get_branch_info(self):
        return f"Branch Name: {self.branch_name}, {self.get_account_info()}"

    def set_branch_name(self, branch_name):
        self.branch_name = branch_name
        