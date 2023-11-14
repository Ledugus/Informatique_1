class Weapon:
    def __init__(self, attack: int) -> None:
        self.attack = attack


class Cratos:
    def __init__(self, weapon) -> None:
        self.weapon = weapon

    def set_weapon(self, weapon: Weapon):
        self.weapon = weapon

    def hit(self, enemy):
        enemy.get_hit(self.weapon.attack)

class Drauf:
    def __init__(self, life: int) -> None:
        self.life = life

    def get_hit(self, damage: int):
        self.life -= damage


me = Cratos(Weapon(50))
enemy = Drauf(100)

for x in range(2):
    me.hit(enemy)
    print(enemy.life)
    me.set_weapon(Weapon(30))
        