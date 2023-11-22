class Character:
    def __init__(self, life: float, attack_point: float) -> None:
        self.life = life
        self.attack_point = attack_point
    def attack(self, target: 'Character'):
        target.get_hit(self.attack_point)
    def get_hit(self, damage: float):
        self.life -= damage
    def __str__(self) -> str:
        return f"Vie : {self.life}, Attaque : {self.attack_point}"

class Cratos(Character):
    def __init__(self) -> None:
        super().__init__(100, 10)
        self.xp = 0
    
    def gain_XP(self, amount: float):
        self.xp += amount
        self.attack_point += (self.xp // 10)
        self.xp = self.xp % 10
    def __str__(self) -> str:
        return super().__str__() + f" XP : {self.xp}"

class Drauf(Character):
    def __init__(self, life: float, attack_point: float) -> None:
        super().__init__(life, attack_point)
