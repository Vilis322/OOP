from pathlib import Path
from time import sleep
import logging

logging.basicConfig(
    filename='errors.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class FoodPrices:
    def __init__(self, file: str):
        self.file: str = file
        self.restaurants: set = set()
        self.restaurants_dishes_and_prices: dict = {}
        self.lists_of_restaurants_and_dishes()

    def lists_of_restaurants_and_dishes(self):
        try:
            file_path = Path(self.file)
        except FileNotFoundError as e:
            logging.error(f"File not found: {e}")
            return

        with file_path.open(encoding="utf-8") as f:
            for line_number, line in enumerate(f, 1):
                line = line.strip()
                try:
                    restaurant, dish_and_price = line.split(' - ')
                    dish, price = dish_and_price.split(', ')
                    dish_price_cortege = (dish, float(price))
                    self.restaurants.add(restaurant)

                    if restaurant not in self.restaurants_dishes_and_prices:
                        self.restaurants_dishes_and_prices[restaurant] = []

                    self.restaurants_dishes_and_prices[restaurant].append(dish_price_cortege)
                except ValueError as e:
                    logging.error(f"Incorrect format in string line number {line_number}: {str(e)}")

    def get_display_restaurants(self):
        for restaurant in self.restaurants:
            print(f"\nMenu from restaurant {restaurant}:")
            sleep(2)
            for dish, price in self.restaurants_dishes_and_prices[restaurant]:
                print(f"for dish '{dish}' price is: {price} EUR")
                sleep(5)

    def get_available_dish(self, user_input):
        available_restaurants = []
        dish_requested = user_input.lower().strip()

        for restaurant, dishes in self.restaurants_dishes_and_prices.items():
            for dish, price in dishes:
                if dish_requested == dish.lower():
                    available_restaurants.append((restaurant, price))

        if available_restaurants:
            dish_prices = [price for _, price in available_restaurants]
            restaurant_with_min_price, min_price = min(available_restaurants, key=lambda x: x[1])
            average_price = sum(dish_prices) / len(dish_prices)
            different_price_range = round(average_price - min_price, 2)

            for restaurant, price in available_restaurants:
                print(f"You can order '{dish_requested}' in restaurant {restaurant} for {price} EUR.")
                sleep(2)

            print(f"\nDifferent between minimal and average price is {different_price_range} EUR.")
            sleep(2)
            print(f"Minimal price is {min_price} EUR in restaurant {restaurant_with_min_price}.")
            sleep(2)
            print(f"Average price is {average_price} EUR.")
            sleep(2)
            print("\nTo select and pay for your order go to the payment page or enter 'exit' to complete the session")

        else:
            print(f"Unfortunately '{dish_requested}' don't have in Narva restaurants.")

    def get_restaurant_name(self):
        for restaurant in self.restaurants:
            print(f"Restaurant {restaurant}")
            sleep(2)

    def get_menu_from_restaurant(self, user_input):
        matching_restaurant = next(
            (restaurant for restaurant in self.restaurants_dishes_and_prices if restaurant.lower() == user_input), None)

        if matching_restaurant:
            print(f"\nMenu from restaurant {matching_restaurant}:")
            sleep(2)
            for dish, price in self.restaurants_dishes_and_prices[matching_restaurant]:
                print(f"for dish '{dish}' price is: {price} ")
                sleep(2)

    @staticmethod
    def exit_from_program():
        print("\nUnfortunately you didn't find any suitable restaurant or dish for you.")
        sleep(2)
        print("We hope that in the future we will can give you more choices. Goodbye!")
        exit()

    @staticmethod
    def printing_welcome_message():
        print("Welcome to the catalog of restaurants.")
        sleep(2)
        print("For watching info about available restaurants enter '1'.")
        sleep(2)
        print("For watching menu from all restaurants enter '2'.")
        sleep(2)
        print("For watching menu from the restaurant you are interested in, enter the restaurant name.")
        sleep(2)
        print("If you would like to order some dish enter the name of dish for pricing information.")
        sleep(2)
        print("If you don't like to order dish from available dishes enter 'exit'.")
        sleep(2)
