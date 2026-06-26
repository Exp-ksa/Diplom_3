import random
from data import INGREDIENT_NAMES


def generate_random_burger_ingredients():
    bun = random.choice(INGREDIENT_NAMES["buns"])
    sauce = random.choice(INGREDIENT_NAMES["sauces"])
    filling = random.choice(INGREDIENT_NAMES["fillings"])
    
    return [bun, sauce, filling]

def generate_random_ingredients_other():
    ingredients = INGREDIENT_NAMES["sauces"] + INGREDIENT_NAMES["fillings"]
    return random.choice(ingredients)

def generate_random_ingredients_bun():
    return random.choice(INGREDIENT_NAMES["buns"])

def generate_random_ingredient():
    ingredients = INGREDIENT_NAMES["sauces"] + INGREDIENT_NAMES["fillings"] + INGREDIENT_NAMES["buns"]
    return random.choice(ingredients)