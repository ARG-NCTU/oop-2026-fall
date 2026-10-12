class material:
    def __init__(self, _name, _purity):
        self.name = _name
        self.purity = _purity
    def get_name(self):
        return self.name
    def get_purity(self):
        return self.purity
    def __str__(self):
        return "Material:" + self.name + ":" + str(self.purity)
    def __add__(self, other):
        return potion(self, other)
    def set_purity(self, new_purity):
        self.purity = new_purity
    def has_ingredient(self, target_name):
        return self.name == target_name


class potion(material):
    batch_id = 1
    def __init__(self, _p1, _p2):
        self.p1 = _p1
        self.p2 = _p2
        self.purity = (self.p1.get_purity() + self.p2.get_purity()) // 2
        self.name = str(potion.batch_id)
        while len(self.name) < 3:
            self.name = "0" + self.name
        potion.batch_id += 1
        material.__init__(self, self.name, self.purity)
    def __str__(self):
        return "Potion:" + self.name + ":" + str(self.purity)
    def __eq__(self, other):
        if not isinstance(other, potion):
            return False
        return (self.p1 == other.p1 and self.p2 == other.p2) or \
               (self.p1 == other.p2 and self.p2 == other.p1)
    def has_ingredient(self, target_name):
        return self.p1.has_ingredient(target_name) or self.p2.has_ingredient(target_name)


m1 = Material("Herb", 40)
m2 = Material("Water", 20)
m3 = Material("Crystal", 100)

p1 = Potion(m1, m2) # Made of Herb and Water
p2 = Potion(p1, m3) # Made of Potion 001 and Crystal

print(p2.has_ingredient("Herb"))    # Output: True (inherited via p1)
print(p2.has_ingredient("Crystal")) # Output: True (direct component)
print(p2.has_ingredient("Fire"))    # Output: False (never used)