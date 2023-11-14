class SMS_Store:
    def __init__(self) -> None:
        self.messages = []
    
    def add_new_arrival(self, from_number: str, time_arrived: str, text: str) -> None:
        self.messages.append((False, from_number, time_arrived, text))
    
    def message_count(self) -> int:
        return len(self.messages)
    
    def get_unread_indexes(self) -> list[int]:
        unread_indexes = [x for x, message in enumerate(self.messages) if not message[0]]
        return unread_indexes
    
    def get_message(self, index: int) -> tuple:
        _, from_number, time, text = self.messages[index]
        self.messages[index] = (True, from_number, time, text)
        return (from_number, time, text)
    def delete(self, index: int) -> None:
        del self.messages[index]
    
    def clear(self) -> None:
        self.messages = []
    
my_inbox = SMS_Store()
my_inbox.add_new_arrival("3", "te", "Bonjour!")
print(my_inbox.get_unread_indexes())
print(my_inbox.get_message(0))
