class Contact:

    def __init__(self, firstname=None, lastname=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.firstname)

    def __eq__(self, other):
        return self.id == other.id and self.firstname == other.firstname