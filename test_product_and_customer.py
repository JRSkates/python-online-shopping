from customer import Customer
from product import Product
from shopping_cart import ShoppingCart
from order import Order

def test_shopping_cart():
  cart = ShoppingCart()
  product = Product(1, "Phone", 300)
  assert product.get_details() == "Phone - £300"

  cart.add_item(product, 2)
  assert len(cart.view_cart()) == 1
  assert cart.get_total_price() == 600

  cart.remove_item(product)
  assert len(cart.view_cart()) == 0
  assert cart.get_total_price() == 0