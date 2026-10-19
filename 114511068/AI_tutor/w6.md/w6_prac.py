class Pet(object):
    def __init__(self, age, name="Unnamed"):
        self.age = age
        self.name = name

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def __str__(self):
        return f"Pet: {self.name}, Age: {self.age}"


class Dragon(Pet):
    tag = 1  # 類別變數：記錄全域 Dragon 的流水號

    def __init__(self, age, name="Unnamed", parent1=None, parent2=None):
        super().__init__(age, name)  # 使用 super() 初始化父類別 Pet
        self.parent1 = parent1
        self.parent2 = parent2
        self.dragon_id = str(Dragon.tag).zfill(3)
        Dragon.tag += 1

    def get_id(self):
        return self.dragon_id

    def __add__(self, other):
        # 覆寫 + 運算子：兩隻 Dragon 繁殖出一隻 age=0 的新 Dragon
        return Dragon(0, "Unnamed", parent1=self, parent2=other)

    def __eq__(self, other):
        if not isinstance(other, Dragon):
            return False

        # 安全取得父母的 ID（若 parent 為 None 則回傳 None，避免 AttributeError）
        p1_self = self.parent1.dragon_id if self.parent1 else None
        p2_self = self.parent2.dragon_id if self.parent2 else None
        p1_other = other.parent1.dragon_id if other.parent1 else None
        p2_other = other.parent2.dragon_id if other.parent2 else None

        # 檢查父母是否相同（不限順序）
        same_order = (p1_self == p1_other) and (p2_self == p2_other)
        reverse_order = (p1_self == p2_other) and (p2_self == p1_other)

        return same_order or reverse_order

    def __str__(self):
        return f"Dragon #{self.dragon_id} (Name: {self.name}, Age: {self.age})"


# ==========================================
# 測試範例 (可直接執行)
# ==========================================
if __name__ == "__main__":
    # 創建第一代龍
    d1 = Dragon(100, "Ignis")
    d2 = Dragon(80, "Astra")

    print(d1)  # Dragon #001 (Name: Ignis, Age: 100)
    print(d2)  # Dragon #002 (Name: Astra, Age: 80)

    # 繁殖第二代龍
    d3 = d1 + d2
    d4 = d2 + d1

    print(d3)  # Dragon #003 (Name: Unnamed, Age: 0)
    print(d4)  # Dragon #004 (Name: Unnamed, Age: 0)

    # 測試父母比較 (__eq__)
    print(f"d3 == d4: {d3 == d4}")  # True (父母相同，順序相反)
    print(f"d1 == d2: {d1 == d2}")  # True (第一代龍父母皆為 None)
    print(f"d1 == d3: {d1 == d3}")  # False
