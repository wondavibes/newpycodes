class Acct:
    def __init__(self):
        self._balance:int = 0
    
    def __str__(self) :
        return f"Your current account balance is: ${self._balance}"

        
    def __add__(self,other):
        if isinstance(other, Acct):
            return f"${self._balance + other._balance}"
        else:
            raise TypeError("Both operands must be Acct instances")


#    @property
#    def balance(self):
#        return self._balance


    def deposit(self, n:int):
        self._balance += n


    def withdraw(self, n):
        self._balance -= n

    def transfer(self, other, n):
        self._balance -= n
        other._balance += n

        
def main():
    account = Acct()
    demo = Acct()
    print(account)
    account.deposit(180)
    account.withdraw(60)
    account.transfer(demo,70)
    print(account)
    print(f"In demo {demo}")
    print("The total balance is",demo+account, sep=None)


if __name__ == "__main__":
    main()