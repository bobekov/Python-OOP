class Account:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def handle_transaction(self, transaction_amount):
        if self.amount + transaction_amount <= 0:
            raise ValueError("sorry cannot go in debt!")
        self.amount += transaction_amount
        self._transactions.append(transaction_amount)
        return f"New balance: {self.amount}"

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError("Please use int for amount")
        return self.handle_transaction(amount)

    @property
    def balance(self):
        return self.amount

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    def __iter__(self):
        return iter(self._transactions)

    def __getitem__(self, index):
        return self._transactions[index]

    def __reversed__(self):
        return reversed(self._transactions)

    def __eq__(self, other):
        return self.amount == other.amount

    def __gt__(self, other):
        return self.amount > other.amount

    def __ge__(self, other):
        return self.amount >= other.amount

    def __add__(self, other):
        new_owner = f"{self.owner}&{other.owner}"
        new_balance = self.amount + other.amount
        new_account = Account(new_owner, new_balance)
        new_account._transactions = self._transactions + other._transactions
        return new_account