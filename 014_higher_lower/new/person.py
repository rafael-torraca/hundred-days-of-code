class Person:

    def __init__(self, data):
        self.name = data["name"]
        self.followers = data["follower_count"]
        self.description = data["description"]
        self.country = data["country"]

    def __str__(self):
        return f"{self.name}, {self.description}, from {self.country}"