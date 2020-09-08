
class Product:
    def __init__(self, name, price, category):
        self.prod_name = name
        self.price = price
        self.category = category

    def update_price(self, percent_change, is_increased = True):
        if is_increased == True:
            print(f"{self.prod_name}'s price has been increased by {percent_change * 100}%")
            self.price += (self.price * percent_change)
        else:
            print(f"{self.prod_name}'s price has been decreased by {percent_change * 100}%")
            self.price -= (self.price * percent_change)
        return self

    def print_info(self):
        print(f"{self.prod_name}:\n\tCategory: {self.category}\t||\tPrice: ${format(self.price, '.2f')}")
        return self
