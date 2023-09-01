class BankAccount:
    def __init__(self, accountHolder):
        # BankAccount methods can access self._balance, but outside of this should not:
        self._balance = 0
        self._name = accountHolder
        with open(self._name + 'Ledger.txt', 'w') as ledgerFile:
            ledgerFile.write("Balance is 0\n")
    
    def deposit(self, amnt):
        if amnt <= 0:
            return # DON'T allow negative "deposits"
        self._balance = self._balance + amnt
        with open(self._name + 'Ledger.txt', 'a') as ledgerFile:
            ledgerFile.write(f'Deposit {str(amnt)} \n')
            ledgerFile.write(f'Balance is {str(self._balance)} \n')
    
    def withdraw(self, amnt):
        if self._balance < amnt or amnt < 0:
            return # Not enough in account, or withdraw is negative
        self._balance -= amnt
        with open(self._name + 'Ledger.txt', 'a') as ledgerFile:
            ledgerFile.write(f'Withdraw {str(amnt)} \n')
            ledgerFile.write(f'Balance is {str(self._balance)} \n')


acct = BankAccount('Alice') # We create an account for alice
acct.deposit(120) # _balance can be affected through depostit()
acct.withdraw(40) # _balance can be affected through withdraw()

# Changing _name or _balnce outside of BankAccount is impolite, but allowed: ERROR or bugs will be produced
acct._balance = 10000000
acct.withdraw(1000)

# Now we are modifying Bob's account ledger!
acct._name = "Bob"
acct.withdraw(1000) # This withdrawl is recorded in BobLedger.txt!