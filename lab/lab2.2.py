import random

class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} получил {damage} урона. Осталось здоровья: {self.health}")

    def attack_enemy(self, enemy):
        damage = random.randint(1, self.attack)
        print(f"{self.name} атакует {enemy.name} и наносит {damage} урона!")
        enemy.take_damage(damage)

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, 100, 20)

    def special_attack(self, enemy, action_name):
        damage = random.randint(10, 30)
        print(f"{self.name} использует {action_name} и наносит {damage} урона!")
        enemy.take_damage(damage)

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, 80, 25)

    def cast_spell(self, enemy):
        damage = random.randint(15, 35)
        print(f"{self.name} использует Магический разряд и наносит {damage} урона!")
        enemy.take_damage(damage)

player, enemy = Warrior("Дариус"), Mage("Зерат")

print(f"{player.name}: {player.health} HP")
print(f"{enemy.name}: {enemy.health} HP")

attack_names = {"Q": "Истребление", "R": "Ноксианская гильотина"}

while player.is_alive() and enemy.is_alive():
    action = input("(Q) Истребление, (R) Ноксианская гильотина: ").upper()
    if action in attack_names:
        player.special_attack(enemy, attack_names[action])
    else:
        print("Некорректный ввод!")
    if enemy.is_alive():
        enemy.cast_spell(player)

print("Поздравляем! Вы победили!" if player.is_alive() else "Вы проиграли. Попробуйте еще раз!")