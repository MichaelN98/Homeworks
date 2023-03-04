import re

camel_list = ["FirstItem", "FriendsList", "MyTuple"]
snake_list = []


for name in camel_list:
    some = re.sub(r"([A-Z][a-z]+)([A-Z][a-z]+)", r"\1_\2", name).lower()
    snake_list.append(some)
print(snake_list)

