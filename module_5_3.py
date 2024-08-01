class House:
    def __init__(self, x, y):
        self.name = x
        self.number_of_floors = int(y)

    def __len__(self):
       return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        self.number_of_floors = self.number_of_floors + value
        return self

    def __iadd__(self, value):
        # assert isinstance(value, int)
        # self.number_of_floors = self.number_of_floors + value
        # return self
        return self + value

    def __radd__(self, value):
        # self.number_of_floors = value + self.number_of_floors
        # return self
        return self + value


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
# print(h1)
# print(h2)
# print(h1 == h2)
# print(h1 + 10)
# # print(h1 += 10)  # не пойму, почему на это ругается. написал вместо этой следующую строку
# print(h1.__iadd__(10))
# print(10 + h2)
# print(str(h1))
# print(str(h2))
# print(h1 == h2)
print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)
print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
