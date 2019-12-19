# Python program to create Bankaccount class 
# with both a deposit() and a withdraw() function 
class Bank_Account(): 
    def __init__(self, pin): 
        self.balance = 0
        self.pin = pin
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine") 

    def _verify_pin(func):
        """
        A decorator that verify pin.
        """
        def wrapper(*args,**kwargs):
            if pin == args[1]:
                print("Verified pin")
                return func(*args,**kwargs)
            else:
                raise Exception("Incorrect pin. Not allowed")
        return wrapper

    @_verify_pin
    def deposit(self, pin, amount): 
        self.balance += amount 
        print("\n Amount Deposited:",amount) 

    @_verify_pin
    def withdraw(self, pin, amount): 
        if self.balance>=amount: 
            self.balance-=amount 
            print("\n You Withdrew:", amount) 
        else: 
            print("\n Insufficient balance ") 

    @_verify_pin
    def get_balance(self, pin): 
        print("\n Net Available Balance=",self.balance) 
    
    @_verify_pin
    def change_pin(self, oldpin, newpin):
        oldpin = newpin
        return newpin


class Savings_Account(Bank_Account):
    def __init__(self,pin):
        Bank_Account.__init__(self,pin)

    def add_interest(self, rate):
        # add interest in balance
        interest = (rate/100) * self.balance
        self.balance += interest
    
# Driver code 

# creating an object of class 
if __name__ == "__main__":
    
    pin = "1234"
    s = Savings_Account(pin) 

    amount = 500
    # Calling functions with that class object 
    s.deposit(pin, amount) 
    amount = 300
    s.withdraw(pin, amount)

    pin = s.change_pin(pin, "5674")
    s.get_balance(pin) 
    s.add_interest(10)
    s.get_balance(pin) 
