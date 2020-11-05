# creating dictionary

# method #1
cat = {"name": "blue", "age": 3.5, "is_cute": True}

# methiod #2
cat = dict(name="blue", age=3.5, is_cute=True)

username = "balls"
password = "1234"

balls = dict(username=username, password=password)


# Acessing date in a dictionary
cat[name]


artist = {
    "first": "Neil",
    "last": "Young",
}

full_name = f'{artist["first"]} {artist["last"]}'
full_name = "{} {}".format(artist["first"], artist["last"])

print(full_name)
