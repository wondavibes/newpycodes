class Acct:
    def __init__(self):
        self._balance = 0
    
    def __str__(self) :
        return f"Your current account balance is: {self._balance}"


#    @property
#    def balance(self):
#        return self._balance


    def deposit(self, n):
        self._balance += n


    def withdraw(self, n):
        self._balance -= n


def main():
    account = Acct()
    print(account)
    account.deposit(180)
    account.withdraw(60)
    print(account)


if __name__ == "__main__":
    main()