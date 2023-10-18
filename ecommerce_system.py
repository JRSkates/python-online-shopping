from inventory import Inventory

class EcommerceSystem:
  def __init__(self):
    self.categories = []
    self.inventory = Inventory()

  def add_category(self, category):
    self.categories.append(category)