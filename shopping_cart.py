class ShoppingCart:
  def __init__(self):
    self.items = []

  def add_item(self, product, quantity=1):
    self.items.append({"product": product, "quantity": quantity})

  def remove_item(self, product):
    self.items = [item for item in self.items if item["product"] != product]

  def view_cart(self):
    return [f"{item['product'].name} - ${item['product'].price} x {item['quantity']}"
      for item in self.items]
  
  def get_total_price(self):
    return sum(item["product"].price * item["quantity"] for item in self.items)