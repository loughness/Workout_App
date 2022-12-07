


class StartMenu():
    """The Start menu whereby we get the choice from our user"""
    def __init__(self, name, items):
        # name is a string
        # items is a List
        self.name = name
        self.items = items

    def __str__(self):
        return self.name

    def show(self):
        print(self.name)
        print("=========")
        for i in range(len(self.items)):
            print(i + 1, self.items[i])
        print("=========")

    def get_choice(self):
        choice = input("Enter your choice: \n")
        return choice

    def run(self):
        self.show()
        choice = self.get_choice()
        return choice
    # ultimately gets CHOICE
    # Which returns an integer of the users' input
