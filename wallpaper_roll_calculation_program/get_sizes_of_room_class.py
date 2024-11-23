class WinDoor:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def square_wd(self):
        return self.width * self.length


class Wallpaper:
    def __init__(self, width, length, room):
        self.width = width
        self.length = length
        self.square = width * length
        self.room = room

    def number_of_rolls(self):
        return self.room.work_surface() / self.square

    def __str__(self):
        return f"\nНеобходимое количество рулонов обоев для вашей комнаты {self.number_of_rolls()} рулонов.\n"


class Room:
    def __init__(self, width, length, height):
        self.width = width
        self.length = length
        self.height = height
        self.wd = []

    def square_room(self):
        return 2 * self.height * (self.width + self.length)

    def add_wd(self, w, h):
        self.wd.append(WinDoor(w, h))

    def work_surface(self):
        total_wd_square = sum(wd.square_wd() for wd in self.wd)
        return self.square_room() - total_wd_square

    def __str__(self):
        return f"Площадь всей комнаты равна {self.square_room()} кв.м.\nПлощадь для обклеивания равна {self.work_surface()}кв.м.\n"
