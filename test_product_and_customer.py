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

def test_customer_operation():
  customer = Customer(1, "Jack", "jack@email.com")
  product1 = Product(1, "Tablet", 200)
  product2 = Product(2, "Headphones", 50)

  customer.add_to_cart(product1, 3)
  customer.add_to_cart(product2)

  cart_items = customer.view_cart()
  assert len(cart_items) == 2
  assert "Tablet - £200 x 3" in cart_items
  assert "Headphones - £50 x 1" in cart_items

  order = customer.checkout()
  assert len(customer.orders) == 1
  assert order.total_price == 650
  assert order.customer.name == "Jack"