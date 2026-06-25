import random
from data import INGREDIENT_NAMES


def generate_random_burger_ingredients():
    bun = random.choice(INGREDIENT_NAMES["buns"])
    sauce = random.choice(INGREDIENT_NAMES["sauces"])
    filling = random.choice(INGREDIENT_NAMES["fillings"])
    
    return [bun, sauce, filling]