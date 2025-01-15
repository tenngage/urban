class House:
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

# h1 = House('ЖК Горский', 18)
# h2 = House('Домик в деревне', 2)
# h1.go_to(5)
# h2.go_to(10)

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 2)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
h1 = h1 / 5
print(h1)
h1 /= 2
print(h1)
