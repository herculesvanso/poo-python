import datetime

class Historic():
    def __init__(self) -> None:
        self.opening_date = datetime.datetime.today()
        self.transactions = []

    def print(self,):
        print(f"Opening date {self.opening_date}")
        print("Transactions")
        for transaction in self.transactions:
            print("-", transaction)