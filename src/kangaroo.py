class Kangaroo:

    def __init__(self, name, pouch_contents=None):
        # __init__ runs, it checks the value of contents and,
        # if necessary, creates a new empty list.  That way,
        # every Kangaroo that gets the default value gets a
        # reference to a different list.

        self.name = name

        if pouch_contents is None:
            pouch_contents = []
        self.pouch_contents = pouch_contents

    def put_in_pouch(self, obj):
        self.pouch_contents.append(obj)

    def __str__(self):
        t = [self.name + ' has pouch contents:']
        for thing in self.pouch_contents:
            s = '    ' + object.__str__(thing)
            t.append(s)
        return '\n'.join(t)
