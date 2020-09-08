import products
import store

def print_all(list):
    print("*"*50)
    for i in list:
        i.print_info()

sears = store.Store("Sears")

blender = products.Product('Blender', 65, 'kitchen')
toaster = products.Product('Toaster', 35, 'kitchen')
microwave = products.Product('microwave', 120, 'kitchen')
futon = products.Product('Futon', 98, 'living room')
print(toaster.prod_name, blender.price, microwave.category)
microwave.update_price(0.1, False).print_info()
print("-"*50)
sears.add_product(blender).add_product(toaster).add_product(microwave).add_product(futon)
sears.inflation(0.005)
sears.set_clearance('kitchen', 0.2)
print_all(sears.products)

