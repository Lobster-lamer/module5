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
                f"кол-во этажей: {CoTeSt.Color.PURPLE}{self.number_of_floors}{CoTeSt.Color.WHITE}\n")


if __name__ == "__main__":
    print()
    house1 = House("ЖК Сентябрь", 3)
    house2 = House("Гномик в деревне", 1)
    print(house1)
    print(house2)
    print(len(house1))
    print(len(house2))
