class Inventory:
  def __init__(self):
    self.proudcts = {}

  def add_product(self, product, quantity):
    if product in self.proudcts:
      self.proudcts[product] += quantity
    else:
      self.proudcts[product] = quantity

  def update_stock(self, product, quantity):
    if product in self.proudcts and self.proudcts[product] >= quantity:
      self.products[product] -= quantity
      return True
    return False
  