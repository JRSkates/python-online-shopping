from inventory import Inventory

class EcommerceSystem:
  def __init__(self):
    self.catagories = []
    self.inventory = Inventory()

  def add_catagory(self, category):
    self.catagories.append(category)