from customer import Customer
from product import Product
from shopping_cart import ShoppingCart
from order import Order

def test_product_details():
  product = Product(1, "Laptop", 800)
  assert product.get_details() == "Laptop - £800"

def test_customer_operations():
  product1 = Product(1, "Mouse", 30)
  product2 = Product(2, "Keyboard", 50)
  customer = Customer(1, "Jack", "jack@email.com")

  customer.add_to_cart(product1)
  customer.add_to_cart(product2)

  cart_items = customer.view_cart()
  assert len(cart_items) == 2
  assert "Mouse - £30" in cart_items
  assert "Keyboard - £50" in cart_items

  total_price = customer.checkout()
  assert total_price == 80