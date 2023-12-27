class Command:
    total_price = 0
    number_commands = 0

    def __init__(self, id_buyer: int, id_item: int, quantity: int, price: float) -> None:
        self.id_buyer = id_buyer
        self.id_item = id_item
        self.quantity = quantity
        self.price = price
        Command.number_commands += 1
        Command.total_price += self.get_price()

    def get_price(self):
        return self.quantity * self.price

    def __str__(self) -> str:
        return f"{self.id_buyer}, {self.id_item} : {self.price} * {self.quantity} = {self.get_price()}"

    @classmethod
    def get_total_price(cls):
        return cls.total_price

    @classmethod
    def get_number_total_command(cls):
        return cls.number_commands


command = Command(1, 2, 3, 9.5)
print(command)
print(command.get_number_total_command())
print(Command.get_total_price())
