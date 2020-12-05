article = {
    "title": "Python is charming",
}

print(article["title"])
try:
    print(article["author"])
except KeyError:
    print("Anonymous author")
