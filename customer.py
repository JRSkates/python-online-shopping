class Customer:
  def __init__(self, customer_id, name, email):
    self.customer_id = customer_id
    self.name = name
    self.email = email
    self.cart = []

  def add_to_cart(self, product):
    self.cart.append(product)

  def view_cart(self):
    return [product.get_details() for product in self.cart]
  
  def checkout(self):
    total_price = sum(product.price for product in self.cart)
    return total_price