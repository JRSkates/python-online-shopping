class Product:
  def __init__(self, product_id, name, price, category=None):
    self.product_id = product_id
    self.name = name
    self.price = price
    self.catagory = category

  def get_details(self):
    return f"{self.name} - £{self.price}"