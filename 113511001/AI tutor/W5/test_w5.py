from w5 import Character, Warrior, Mage, Team


print("---- Test 1: Basic Warrior ----")
w1 = Warrior("Alex", 5)

print("ID:", w1.get_id())
print("Name:", w1.name)
print("Level:", w1.level)
print("Power:", w1.get_power())

assert w1.get_id() == "001"
assert w1.get_power() == 10

print("Test 1 passed!")


print("\n---- Test 2: Basic Mage ----")
m1 = Mage("Luna", 4)

print("ID:", m1.get_id())
print("Name:", m1.name)
print("Level:", m1.level)
print("Power:", m1.get_power())

assert m1.get_id() == "002"
assert m1.get_power() == 12

print("Test 2 passed!")


print("\n---- Test 3: Team ----")
team1 = w1 + m1

print("Total power:", team1.get_total_power())

assert team1.get_total_power() == 22

print("Test 3 passed!")


print("\n---- Test 4: Edge Case ----")
w2 = Warrior("A", 1)
w3 = Warrior("B", 100)

team2 = w2 + w3

print("w2 power:", w2.get_power())
print("w3 power:", w3.get_power())
print("Team total power:", team2.get_total_power())

assert w2.get_power() == 2
assert w3.get_power() == 200
assert team2.get_total_power() == 202

print("Test 4 passed!")


print("\n---- Test 5: Unique IDs ----")
print("w1 ID:", w1.get_id())
print("m1 ID:", m1.get_id())
print("w2 ID:", w2.get_id())
print("w3 ID:", w3.get_id())

assert w1.get_id() == "001"
assert m1.get_id() == "002"
assert w2.get_id() == "003"
assert w3.get_id() == "004"

print("Test 5 passed!")


print("\nALL TESTS PASSED!")