from get_sizes_of_room_class import WinDoor, Wallpaper, Room


class WindowDoorSquareError(Exception):
    pass


def user_input(input_message="значение", error_message="значение"):
    while True:
        try:
            value = float(input(f"\nВведите {input_message}: ").strip())
            return value
        except ValueError:
            print(f"Была введена некорректная {error_message}. Пожалуйста, введите корректную {input_message}!")


def room_dimensions():
    length_wall = user_input(input_message="длину стены", error_message="длина стены")
    width_wall = user_input(input_message="ширину стены", error_message="ширина стены")
    height_wall = user_input(input_message="высоту стены", error_message="высота стены")
    room = Room(length_wall, width_wall, height_wall)
    return room


def amount_windows_and_doors():
    count_windows = user_input(input_message="количество окон", error_message="количество окон")
    count_doors = user_input(input_message="количество дверей", error_message="количество дверей")
    return count_windows, count_doors


def input_dimensions(count, object_type):
    dimensions = []
    for i in range(int(count)):
        length = user_input(input_message=f"длину {i+1}{object_type}", error_message=f"длина {i+1}{object_type}")
        width = user_input(input_message=f"ширину {i+1}{object_type}", error_message=f"ширина {i+1}{object_type}")
        dimensions.append((length, width))
    return dimensions


def get_dimensions_windows_and_doors(room):
    while True:
        count_windows, count_doors = amount_windows_and_doors()

        input_error = False

        try:
            windows_dimensions = input_dimensions(count_windows, "-го окна")
            doors_dimensions = input_dimensions(count_doors, "-ой двери")

            total_windows_square = sum(WinDoor(length, width).square_wd() for length, width in windows_dimensions)
            total_doors_square = sum(WinDoor(length, width).square_wd() for length, width in doors_dimensions)

            if total_windows_square + total_doors_square >= room.square_room():
                raise WindowDoorSquareError("\nОбщая площадь окон и дверей равна или превышает площадь комнаты!")

            for length, width in windows_dimensions + doors_dimensions:
                room.add_wd(length, width)

        except WindowDoorSquareError as e:
            print(str(e))
            print("Вам придётся ввести параметры окон и дверей заново!")
            input_error = True

        if not input_error:
            break


def dimensions_of_rolls(room):
    length_wallpaper = user_input(input_message="длину рулона", error_message="длина рулона")
    width_wallpaper = user_input(input_message="ширину рулона", error_message="ширина рулона")
    number_of_rolls = Wallpaper(length_wallpaper, width_wallpaper, room)
    return number_of_rolls


def main():
    print("Добро пожаловать в интернет-магазин 'Обои для дома'!\nСперва необходимо вычислить необходимую площадь "
          "обклейки Вашей комнаты.\nСперва введите ширину, длину и высоту стен соответственно.")

    room = room_dimensions()

    print(f"\nОтлично, у нас есть значение площади Вашей комнаты, это значение равно {room.square_room()} кв.м.\nТеперь"
          f" нам необходимо выяснить, сколько в Вашей комнате окон и дверей и вычислить их общую площадь для вычисления"
          f" необходимой площади обклейки комнаты.")

    get_dimensions_windows_and_doors(room)

    print(f"\nОтлично, теперь у нас есть все необходимые параметры.\n{room}\nОсталось выяснить количество рулонов обоев"
          f", необходимых для обклейки Вашей комнаты.\nДля этого Вам необходимо ввести длину и ширину одного рулона "
          f"выбранных Вами обоев.")

    number_of_rolls = dimensions_of_rolls(room)

    print(number_of_rolls)
    print("Для заказа перейдите на страницу оплаты. Спасибо, что выбрали 'Обои для дома'!")


if __name__ == "__main__":
    main()
