from module_5_3 import House as House_module_5_3


class House(House_module_5_3):
    house_history = []

    def __new__(cls, name: str, *args, **kwargs):
        cls.house_history.append(name)
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        super().__init__(name, number_of_floors)

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории и сердцах(")


if __name__ == "__main__":
    house1 = House("ЖеКа", 10)
    house2 = House("Чеченский ЖК \"Дон\"", 44)
    print(House.house_history)
    print(house1)
    del house1
    print(123)

