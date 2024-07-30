spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    # takes a list of spicy_foods and returns a list of strings with the names of each spicy food.
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    # takes a list of spicy_foods and returns a list of dictionaries where the heat level of the food is greater than 5.
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    # takes a list of spicy_foods and outputs to the terminal each spicy food in the following format using print(): Buffalo Wings (American) | Heat Level: 🌶🌶🌶
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    # takes a list of spicy_foods and a string representing a cuisine, and returns a single dictionary for the spicy food whose cuisine matches the cuisine being passed to the method.
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None

def print_spiciest_foods(spicy_foods):
    # takes a list of spicy_foods and outputs to the terminal ONLY the spicy foods that have a heat level greater than 5
    for food in get_spiciest_foods(spicy_foods):
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")
    

def get_average_heat_level(spicy_foods):
    # takes a list of spicy_foods and returns the average heat level of all the foods in the list.
    # Recall that to derive the average of a collection, you need to calculate the total and divide number of elements in the collection.
    return sum([food["heat_level"] for food in spicy_foods]) / len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    # takes a list of spicy_foods and a dictionary representing a new spicy food, and returns the updated list with the new spicy food added.
    spicy_foods.append(spicy_food)
    return spicy_foods

    
