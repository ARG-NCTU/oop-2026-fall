# Week 1: arithmetic and sequential assignment only.
# Edit these two values to try another valid input.
items = 23
capacity = 5

full_boxes = items // capacity
leftover_items = items % capacity
extra_box = (leftover_items + capacity - 1) // capacity
required_boxes = full_boxes + extra_box
unused_slots = required_boxes * capacity - items

print(full_boxes, leftover_items, required_boxes, unused_slots)
