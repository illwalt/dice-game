# creating dictionary

# method #1
cat = {"name": "blue", "age": 3.5, "is_cute": True}

# methiod #2
cat = dict(name="blue", age=3.5, is_cute=True)

username = "balls"
pword2 = "1234"

balls = dict(username=username, password=pword2)

users = []
users.append(dict(username=username, password=pword2))

# Acessing date in a dictionary
cat[name]


artist = {
    "first": "Neil",
    "last": "Young",
}

full_name = f'{artist["first"]} {artist["last"]}'
full_name = "{} {}".format(artist["first"], artist["last"])

print(full_name)
