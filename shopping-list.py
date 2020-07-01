shopping_lists = ["bread" ,"milk","eggs","rice","pasta"]

item_to_find = "pasta"
found_at = False

for index in range(len(shopping_lists)):
    if shopping_lists[index] == item_to_find:
        found_at = index

print("item found at position {}".format(found_at))