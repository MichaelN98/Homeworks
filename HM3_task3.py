friends = ["John", "Marta", "James"]
enemies = ["John", "Johnatan", "Artur"]

for friend in friends:
    if friend != 'James':
        if friend not in enemies:
            print(f'{friend} we are the best friends')
        else:
            print(f'{friend} we are not friends anymore')

