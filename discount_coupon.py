class DiscountCoupon:
  def __init__(self, code, discount_percentage):
    self.code = code
    self.discount_percentage = discount_percentage

  def apply_discount(self, price):
    return price * (1 - self.discount_percentage / 100)