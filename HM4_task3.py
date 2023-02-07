cv = "name=Amanda=sssss&age=32&&salary=1500&currency=euro"
filter_str = cv.split('&')
pairs = {}
for my_str in filter_str:
    if my_str:
        key, value = my_str.split('=', maxsplit=1)
        if '=' in value:
            value = value.split('=')[0]
        pairs[key] = value

print(pairs)


