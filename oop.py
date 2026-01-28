class Player:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0

    def is_alive(self):
        return self.hp > 0
    
p = Player("Jan Olav", 20)
print(p.name, p.hp)
p.take_damage(5)
print(p.name, p.hp, p.is_alive())
p.take_damage(20)
print(p.name, p.hp, p.is_alive())