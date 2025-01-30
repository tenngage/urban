class House:
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
            return
        for i in range(1, new_floor + 1):
            print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, количество этажей: {self.number_of_floors}"

    def __del__(self):
        print(f"{self.name} снесен, но он останется в истории")

    def __eq__(self, other):
        if isinstance(other, int):
            return self.number_of_floors == other
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if isinstance(other, int):
            return self.number_of_floors < other
        return self.number_of_floors < other.number_of_floors

    def __gt__(self, other):
        if isinstance(other, int):
            return self.number_of_floors > other
        return self.number_of_floors > other.number_of_floors

    def __le__(self, other):
        if isinstance(other, int):
            return self.number_of_floors <= other
        return self.number_of_floors <= other.number_of_floors

    def __ge__(self, other):
        if isinstance(other, int):
            return self.number_of_floors >= other
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if isinstance(other, int):
            return self.number_of_floors != other
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        raise TypeError

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

    def __sub__(self, value):
        if isinstance(value, int):
            self.number_of_floors -= value
            return self
        raise TypeError

    def __isub__(self, value):
        return self.__sub__(value)

    def __mul__(self, value):
        if isinstance(value, int):
            self.number_of_floors *= value
            return self
        raise TypeError

    def __rmul__(self, value):
        return self.__mul__(value)

    def __imul__(self, value):
        return self.__mul__(value)

    def __truediv__(self, value):
        if isinstance(value, int):
            self.number_of_floors = int(self.number_of_floors / value)
            return self
        raise TypeError

    def __itruediv__(self, value):
        return self.__truediv__(value)

    houses_history = []

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
