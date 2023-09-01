from wizcoin import WizCoin

class WizardCustomer(WizCoin):
    def __init__(self, name):
        self.name = name
        super().__init__(0, 0, 0)

wizard = WizardCustomer('Alice')
print(f'{wizard.name} has {wizard.value()} knuts worth of money.')
print(f'{wizard.name}\s coins weigh {wizard.weightInGrams()} grams.')