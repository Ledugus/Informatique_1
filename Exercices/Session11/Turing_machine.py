class Node:
    def __init__(self, s):
        self.__value = s
        self.previous = None
        self.next = None

    def get_text(self):
        return self.__value

    def set_text(self, s):
        self.__value = s


class Tape:
    def __init__(self):
        self.__first = None
        self.current = None
        self.__last = None
        self.__length = 0

    def next(self):
        if self.current and self.current.next:
            self.current = self.current.next
            return self.current.get_text()
        return None

    def previous(self):
        if self.current and self.current.previous:
            self.current = self.current.previous
            return self.current.get_text()
        return None

    def get_length(self):
        return self.__length

    def add(self, s):
        to_add = Node(s)
        self.__length += 1
        if self.__last:
            self.__last.next = to_add
            to_add.previous = self.__last
            self.__last = to_add
        else:
            self.__first = to_add
            self.__last = to_add
            self.current = to_add

    def write(self, s):
        if self.current:
            self.current.set_text(s)

    def read(self):
        if self.current:
            return self.current.get_text()
        return None

    def __str__(self) -> str:

        s = "[ "
        tail = self.__first
        while tail:
            s += str(tail.get_text()) + " "
            tail = tail.next
        s += "]"
        return s


if __name__ == "__main__":
    tape = Tape()
    for x in range(3):
        tape.add(x)
    print(tape)
    print(tape.next())
    print(tape.previous())
