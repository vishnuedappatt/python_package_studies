import random


class Customer:
    def __init__(self, quantity, price):
        words = ['1', 'a', 'a', 'j']

        self.id = str(random.randint(999, 100000))+random.choice(words)
        self.quantity = quantity
        self.price = price
        self.discount = 0

    def total_price(self):
        if self.discount > 0:
            without_discount = self.price*self.quantity
            dis_price = without_discount*self.discount
            rate = without_discount-dis_price
        else:
            rate = self.price * self.quantity
        print(f'your price is {rate} for the ID {self.id}')


class GoldenEmployee(Customer):
    def __init__(self, quantity, price):
        super().__init__(quantity, price)
        self.discount = .2
        self.total_price()


emp1 = GoldenEmployee(12, 10)
