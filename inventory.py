class Inventory:
  def __init__(self):
    self.products = {}

  def add_product(self, product, quantity):
    if product in self.products:
      self.products[product] += quantity
    else:
      self.products[product] = quantity

  def update_stock(self, product, quantity):
    if product in self.products and self.products[product] >= quantity:
      self.products[product] -= quantity
      return True
    return False
  