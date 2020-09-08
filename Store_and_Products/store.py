class Store:
    def __init__(self, store_name):
        self.name = store_name
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"{product.prod_name} added to {self.name}")
        return self

    def sell_product_by_num(self, idNumber):
        for i in self.products:
            if i.idNum == idNumber:
                print(f"{i.prod_name} sold for ${format(i.price, '.2f')}.")
                self.products.remove(i)
        return self

    def sell_product_by_index(self, ind):
        print(f"{self.products[ind].prod_name} sold for ${format(self.products[ind].price, '.2f')}.")
        self.products.pop(ind)
        return self

    def inflation(self, percent_increase):
        print("-"*50)
        print("Inflation hits:")
        for i in self.products:
            i.update_price(percent_increase, True)
        return self

    def set_clearance(self, category, percent_discount):
        print("-"*50)
        print(f"Clearance Sale on {category} items!!")
        for i in self.products:
            if i.category == category:
                i.update_price(percent_discount, False)
        return self