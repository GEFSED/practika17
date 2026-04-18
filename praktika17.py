class Cleaner:
    def clean(self):
        print("Уборщик делает уборку.")
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating
        self.cleaner = Cleaner()
    def describe_restaurant(self):
        print("Название ресторана:", self.restaurant_name)
        print("Тип кухни:", self.cuisine_type)
        print("Рейтинг:", self.rating)
    def open_restaurant(self):
        print("Ресторан открыт.")
    def update_rating(self, new_rating):
        self.rating = new_rating
    def clean_restaurant(self):
        self.cleaner.clean()
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, rating=0, flavors=None, location="", work_time=""):
        super().__init__(restaurant_name, cuisine_type, rating)
        if flavors is None:
            self.flavors = []
        else:
            self.flavors = flavors
        self.location = location
        self.work_time = work_time

    def show_flavors(self):
        print("Сорта мороженого:")
        for flavor in self.flavors:
            print("-", flavor)

    def add_flavor(self, flavor):
        self.flavors.append(flavor)
        print(flavor, "добавлен в список.")

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)
            print(flavor, "удален из списка.")
        else:
            print(flavor, "не найден в списке.")

    def check_flavor(self, flavor):
        if flavor in self.flavors:
            print(flavor, "есть в наличии.")
        else:
            print(flavor, "нет в наличии.")

    def stick_ice_cream(self, flavor):
        print("Мороженое на палочке:", flavor)

    def soft_ice_cream(self, flavor):
        print("Мягкое мороженое:", flavor)

    def cone_ice_cream(self, flavor):
        print("Мороженое в рожке:", flavor)
# 11.1
ice_cream_shop = IceCreamStand(
    "Снежок",
    "Десерты",
    5,
    ["Ванильное", "Шоколадное", "Клубничное"],
    "Невский проспект",
    "10:00 - 22:00"
)
ice_cream_shop.show_flavors()
# 11.2
print("Локация:", ice_cream_shop.location)
print("Время работы:", ice_cream_shop.work_time)
ice_cream_shop.add_flavor("Фисташковое")
ice_cream_shop.show_flavors()
ice_cream_shop.remove_flavor("Шоколадное")
ice_cream_shop.show_flavors()
ice_cream_shop.check_flavor("Ванильное")
ice_cream_shop.check_flavor("Банановое")
ice_cream_shop.stick_ice_cream("Клубничное")
ice_cream_shop.soft_ice_cream("Ванильное")
ice_cream_shop.cone_ice_cream("Фисташковое")