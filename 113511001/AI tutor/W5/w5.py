class Character:
    id = 1
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.id = Character.id
        Character.id += 1
    def get_power(self):
        return self.level
    def get_id(self):
        return str(self.id).zfill(3)
    def __add__(self, other):
        return Team(self, other)


class Warrior(Character):
    def __init__(self, name, level):
        Character.__init__(self, name, level)
    def get_power(self):
        return self.level * 2

class Mage(Character):
    def __init__(self, name, level):
        Character.__init__(self, name, level)
    def get_power(self):
        return self.level * 3

class Team:
    def __init__(self, member1, member2):
        self.members = [member1, member2]
    def get_total_power(self):
        total_power = 0
        for member in self.members:
            total_power += member.get_power()
        return total_power