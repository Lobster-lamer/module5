from consoleTextStyle import ConsoleTextStyle as CoTeSt


class House:
    def __init__(self, name: str, number_of_floors: int):
        self.name = name
        self.number_of_floors = number_of_floors
        try:
            if "сентябрь" in self.name.lower() and number_of_floors == 3:
                print(f"{CoTeSt.Color.YELLOW}3-ье сентября - день прощанья,\n"
                      f"День, когда горят костры рябин.{CoTeSt.Color.WHITE}\n")
        except:
            pass

    def go_to(self, destination_floor: int):
        if destination_floor < 1 or destination_floor > self.number_of_floors:
            print("\nТакого этажа не существует")
        else:
            print("\n".join(list(map(str, list(range(1, destination_floor+1))))))

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return (f"Название: {CoTeSt.Color.PURPLE}{self.name}{CoTeSt.Color.WHITE}, "
                f"кол-во этажей: {CoTeSt.Color.PURPLE}{self.number_of_floors}{CoTeSt.Color.WHITE}")

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
    def __iadd__(self, value):
        self.__add__(value)
        return self
    def __radd__(self, value):
        return self.__add__(value)

    def __sub__(self, value):
        if isinstance(value, int):
            self.number_of_floors -= value
    def __isub__(self, value):
        self.__sub__(value)
        return self
    def __rsub__(self, value):
        return value - self.number_of_floors

    def __mul__(self, value):
        if isinstance(value, int):
            self.number_of_floors *= value
    def __imul__(self, value):
        self.__mul__(value)
        return self
    def __rmul__(self, value):
        return self.__mul__(value)

    def __truediv__(self, value):
        if isinstance(value, int):
            self.number_of_floors //= value
    def __itruediv__(self, value):
        self.__truediv__(value)
        return self
    def __rtruediv__(self, value):
        return value // self.number_of_floors


if __name__ == "__main__":
    print()
    house1 = House("ЖК Сентябрь", 3)
    house2 = House("Гномик в деревне", 1)
    print(house1)
    print(house2)

    print(f"\nРавны? {CoTeSt.Color.PURPLE}{house1 == house2}{CoTeSt.Color.WHITE}")
    print(f"house1 > house2? {CoTeSt.Color.PURPLE}{house1 > house2}{CoTeSt.Color.WHITE}")
    print(f"house1 >= house2? {CoTeSt.Color.PURPLE}{house1 >= house2}{CoTeSt.Color.WHITE}")
    print(f"house1 < house2? {CoTeSt.Color.PURPLE}{house1 < house2}{CoTeSt.Color.WHITE}")
    print(f"house1 <= house2? {CoTeSt.Color.PURPLE}{house1 <= house2}{CoTeSt.Color.WHITE}")
    print(f"house1 != house2? {CoTeSt.Color.PURPLE}{house1 != house2}{CoTeSt.Color.WHITE}\n")

    print("Сложение:")
    house1 + 1
    print(house1)
    1 + house1
    print(house1)
    house1 += 1
    print(house1)

    print("\nВычитание:")
    house1 - 1
    print(house1)
    1 - house1
    print(house1)
    house1 -= 1
    print(house1)

    print("\nУмножение:")
    house1 * 2
    print(house1)
    2 * house1
    print(house1)
    house1 *= 2
    print(house1)

    print("\nДеление:")
    house1 / 2
    print(house1)
    2 / house1
    print(house1)
    house1 /= 2
    print(house1)

