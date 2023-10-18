class Category:
  def __init__(self, category_id, name):
    self.category_id = category_id
    self.name = name
    self.products = []

  def add_product(self, product):
    self.products.append(product)