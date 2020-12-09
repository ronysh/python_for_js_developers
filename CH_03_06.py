FRIENDS = [
  {"name": "Graham"}, 
  {"name": "John"}, 
  {"name": "Terry"}, 
  {"name": "Eric"}, 
  {"name": "Terry"}, 
  {"name": "Michael"}
] # Members of Monty Python comedy troupe!


for friend in FRIENDS:
    if "a" in friend["name"]:
        print(f"Hey {friend['name']}!")
