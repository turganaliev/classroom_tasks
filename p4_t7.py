class MoneyFmt():
    def __init__(self, amount):
        self.amount = amount

    def update(self, _amount):
        self.amount = _amount
        return str(round(_amount, 2)) + '$'

    def repr(self):
        return float(self.amount)

    def str(self):
        return str(round(self.amount, 2)) + '$'

cash = MoneyFmt(-123455.67888)
print(cash.repr())
print(cash.str())
print(cash.update(122.899))
