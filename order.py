class Order:
  def __init__(self, order_id, customer, items, total_price):
    self.order_id = order_id
    self.customer = customer
    self.items = items
    self.total_price = total_price

  def display_order(self):
    item_list = "\n".join([f"{item['product'].name} - ${item['product'].price} x {item['quantity']}"
      for item in self.items])
    return f"Order ID: {self.order_id}\nCustomer: {self.customer.name}\nItems:\n{item_list}\nTotal Price: ${self.total_price}"