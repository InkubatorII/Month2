class Asset:
    pass

class InsurableItem:
    pass

class BankAccount(Asset):
    pass

class RealEstate(Asset, InsurableItem):
    pass

class Security(Asset, InsurableItem):
    pass

class InterestBearingItem(Asset):
    pass


class SavingAccount(BankAccount):
    pass

class CheckingAccount(BankAccount):
    pass


class Stock(Security):
    pass

class Bond(Security):
    pass
