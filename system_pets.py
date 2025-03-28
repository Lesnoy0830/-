"""Система учета домашних животных."""


class Pet:
    """Описываем класс Pet."""

    def __init__(self, name, animal_type, age, breed):
        """Инициализирует базовые атрибуты игрового объекта."""
        self.name = name
        self.animal_type = animal_type
        self.age = age
        self.breed = breed

    def __str__(self):
        """Вывод информации о животном."""
        return f"""Имя: {self.name},
Животное: {self.animal_type},
Возраст: {self.age},
Порода: {self.breed}

"""


class PetRegistry:
    """Класс для системной работы программы."""

    def __init__(self):
        """Инициализирует пустой список."""
        self.pets = []

    def add_pet(self, pet):
        """Добавляет объект Pet в список pets."""
        self.pets.append(pet)

    def display_pet_info(self, name):
        """Ищет питомца по имени в списке."""
        found = False
        for pet in self.pets:
            if pet.name == name:
                print(pet)
                found = True
                break
        if not found:
            print(f"Питомец с именем {name} не найден.")

    def display_all_pets(self):
        """Выводит информацию о каждом питомце в списке."""
        if not self.pets:
            print("В реестре нет питомцев.")
        else:
            for pet in self.pets:
                print(pet)


# Создание реестра питомцев
registry = PetRegistry()

# Создание питомцев
pet1 = Pet("Барон", "собака", 5, "лабрадор")
pet2 = Pet("Мурка", "кошка", 3, "сиамская")

registry.add_pet(pet1)
registry.add_pet(pet2)


registry.display_pet_info("Барон")


registry.display_all_pets()


registry.display_pet_info("Рексик")
