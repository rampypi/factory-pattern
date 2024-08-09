# Implemente a pizzstore where we can orderPizza, three types are there Veggie, CLAM, Cheese
#Pizzastore shoould able to prepare the bake, add cut(), add ingredients,  box it and sent it
# There are 3 regionns we can support
# Plannig to have different ingredients for this different region


import unittest

from app.exception import NotAvailbalePizza
from app.pizza_store import NYPizzastore, PizzaType, CHPizzastore


class TestPizzaStore(unittest.TestCase):
    def test_order_one_NY_pizza(self):
        pizzstore = NYPizzastore()
        pizzstore.order_pizza(PizzaType.CHEESE)
        self.assertEqual(pizzstore.prepare_order(), "Ordered delivered")
        
    def test_order_one_Chicago_pizza(self):
        pizzstore = CHPizzastore()
        pizzstore.order_pizza(PizzaType.CHEESE)
        self.assertEqual(pizzstore.prepare_order(), "Ordered delivered")
        
    def test_order_one_Chicago_clam_pizza(self):
        pizzstore = CHPizzastore()
        pizzstore.order_pizza(PizzaType.CLAM)
        self.assertEqual(pizzstore.prepare_order(), "Ordered delivered")
        
    def test_order_one_Chicago_veggie_pizza(self):
        pizzstore = CHPizzastore()
        pizzstore.order_pizza(PizzaType.VEGGIE)
        self.assertEqual(pizzstore.prepare_order(), "Ordered delivered")
        
    def test_order_not_valid_pizza_tpe(self):
        pizzstore = CHPizzastore()
        with self.assertRaises(NotAvailbalePizza) as context:

            pizzstore.order_pizza("INVALID")
        
        self.assertEqual(context.exception.message, "This Pizza is not available in our store")
        
    