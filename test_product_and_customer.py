from customer import Customer
from product import Product

def test_product_details():
  product = Product(1, "Laptop", 800)
  assert product.get_details() == "Laptop - £800"

