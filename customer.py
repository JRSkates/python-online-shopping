from shopping_cart import ShoppingCart
from order import Order

class Customer:
  def __init__(self, customer_id, name, email):
    self.customer_id = customer_id
    self.name = name
    self.email = email
    self.shopping_cart = ShoppingCart()
    self.orders = []

  def add_to_cart(self, product, quantity=1):
    self.shopping_cart.add_item(product, quantity)

  def view_cart(self):
    return self.shopping_cart.view_cart()
  
  def checkout(self):
    total_price = self.shopping_cart.get_total_price()
    new_order = Order(len(self.orders) + 1, self, self.shopping_cart.items, total_price)
    self.orders.append(new_order)
    self.shopping_cart = ShoppingCart()
    return new_order