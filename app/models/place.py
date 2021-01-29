class Place:
    def __init__(self, name, country, description, visited = False, id = None):
        self.name = name
        self.country = country
        self.description = description
        self.visited = visited
        self.id = id


    def mark_as_visited(self):
        self.visited = True