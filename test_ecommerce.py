from category import Category
from product import Product
from inventory import Inventory
from ecommerce_system import EcommerceSystem

def test_add_category_and_product():
  category = Category(1, "Electronics")
  product = Product(1, "Laptop", 800, category)
  inventory = Inventory()
  inventory.add_product(product, 5)
  ecommerce_system = EcommerceSystem()
  ecommerce_system.add_category(category)
  assert len(ecommerce_system.categories) == 1
  assert len(inventory.products) == 1