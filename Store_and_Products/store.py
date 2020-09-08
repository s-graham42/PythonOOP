class Store:
    def __init__(self, store_name):
        self.name = store_name
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"{product.prod_name} added to {self.name}")
        return self

    def sell_product(self, id):
        print(f"{self.products[id].prod_name} sold for ${self.products[id].price}.")
        self.products.pop(id)
        return self

    def inflation(self, percent_increase):
        print("Inflation hits:")
        for i in self.products:
            i.update_price(percent_increase, True)
        return self

    def set_clearance(self, category, percent_discount):
        print(f"Clearance Sale on {category} items!!")
        for i in self.products:
            if i.category == category:
                i.update_price(percent_discount, False)
        return self