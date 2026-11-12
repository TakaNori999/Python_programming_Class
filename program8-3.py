class ShoppingCart:
    def __init__(self):
        self.cart = []
    def add_item(self, item):
        self.cart.append(item)
    def remove_item(self, item):
        if item in self.cart:
            self.cart.remove(item)
            print(f"deleted {item}")
        else:
            print(f"There is no {item}.")
    def view_cart(self):
        if self.cart:
            for i, box in enumerate(self.cart):
                print(f"{i+1}.{box}")
        else:
            print("Empty..")
cart = ShoppingCart()
cart.view_cart()
cart.add_item("apple")
cart.add_item("banana")
cart.remove_item("apple")
cart.view_cart()