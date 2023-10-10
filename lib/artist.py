class Artist:
    # We initialise with all of our attributes
    # Each column in the table should have an attribute here
    def __init__(self, id, name, genre):
        self.id = id
        self.name = name
        self.genre = genre

    # This method allows our tests to assert that the objects it expects
    # are the objects we made based on the database records.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print an Artist
    def __repr__(self):
        return f"Artist({self.id}, {self.name}, {self.genre})"
    
    def is_valid(self):
        if self.name == None or self.name == '':
            return False
        if self.genre == None or self.genre == '':
            return False
        return True
    
    def generate_errors(self):
        errors = []
        if self.name == None or self.name == '':
            errors.append("Name can't be blank")
        if self.genre == None or self.genre == '':
            errors.append("Release year can't be blank")

        if len(errors) == 0:
            return None
        else:
            return ', '.join(errors)