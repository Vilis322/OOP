from food_price_comparator import FoodPrices


def main():
    food = FoodPrices("food.txt")
    user_input: str = ""

    food.printing_welcome_message()

    while user_input != "exit":
        user_input = input("\nWhat is your choice?\n").strip().lower()

        if user_input == "1":
            food.get_restaurant_name()

        elif user_input == "2":
            food.get_display_restaurants()

        elif user_input == "exit":
            food.exit_from_program()

        elif user_input in map(lambda x: x.lower(), food.restaurants):
            food.get_menu_from_restaurant(user_input)

        else:
            food.get_available_dish(user_input)


if __name__ == '__main__':
    main()
