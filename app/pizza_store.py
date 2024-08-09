from enum import Enum
from abc import ABC, abstractmethod
from app.exception import NotAvailbalePizza


class PizzaType(Enum):
    CHEESE  =1
    VEGGIE = 2
    CLAM = 3


class Pizzastore(ABC):
    def __init__(self) -> None:
        self.pizza = None
   
    @abstractmethod
    def create_pizza(self, type: PizzaType):
        pass
     
    def order_pizza(self, type: PizzaType):
        self.pizza = self.create_pizza(type)
        if not isinstance(type, PizzaType):
            raise NotAvailbalePizza("This Pizza is not available in our store")
        if self.pizza:
            return self.prepare_order()
        
    
    def prepare_order(self):
        self.pizza.bake()
        self.pizza.cut()
        self.pizza.box()
        return "Ordered delivered"
   
        
class NYPizzastore(Pizzastore):
    def __init__(self):
        self.ingredients = NYIngredients()
        
    def create_pizza(self, type: PizzaType):
        if type == PizzaType.CHEESE:
           return CheesePizza(self.ingredients)
        elif type == PizzaType.CLAM:
            return ClamPizza(self.ingredients)
        else:
            return VeggiePizza(self.ingredients)
        
        return None
     
    
    
class CHPizzastore(Pizzastore):
    def __init__(self):
        self.ingredients = CHIngredients()
        
    def create_pizza(self, type: PizzaType):
        if type == PizzaType.CHEESE:
            return CheesePizza(self.ingredients)
        elif type == PizzaType.CLAM:
            return ClamPizza(self.ingredients)
        else:
            return VeggiePizza(self.ingredients)  
        return None

class Pizza(ABC):
    def __init__(self, ingredients):
        self.ingredients = ingredients
    
    @abstractmethod
    def bake(self):
        pass
    
    @abstractmethod
    def cut(self):
        pass
    
    @abstractmethod
    def box(self):
        pass
    
class Ingredient(ABC):
    
    @abstractmethod
    def prepare(self):
        pass

class CheesePizza(Pizza):
    
    
    def bake(self):
        self.ingredients.prepare()
        return "Baking Cheese Pizza"
    
    def cut(self):
        return "Cutting Cheese Pizza"
    
    def box(self):
        return "boxing Cheese Pizza"
    
class VeggiePizza(Pizza):
    
    def bake(self):
        self.ingredients.prepare()
        return "Preparin Veggie Pizza"
    
    def cut(self):
        return "Cutting Veggie Pizza"
    
    def box(self):
        return "boxing Veggie Pizza"


class ClamPizza(Pizza):
    
    def bake(self):
        self.ingredients.prepare()
        return "Preparin Cheese Pizza"
    
    def cut(self):
        return "Cutting Cheese Pizza"
    
    def box(self):
        return "boxing Cheese Pizza"


class NYIngredients(Ingredient):
    def prepare(self):
        return "Use NY Ingredients"
    

class CHIngredients(Ingredient):
    def prepare(self):
        return "Use CH Ingredients"