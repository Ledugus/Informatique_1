class C1:
    def __init__(self) -> None:
        self.value = 1

    def move(self):
        pass

    def move_right(self):
        self.move()
    
class C2(C1):
    def __init__(self) -> None:
        self.value = 10

    def move(self):
        print("Cette méthode doit être appelée")

c = C2()
c.move_right()