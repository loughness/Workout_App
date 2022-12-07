from setup import Setup

class Load_Save:
    def __init__(self):
        self.date = Setup.name
        self.start_note =  "1"
        self.conclusion = "2"
        self.end_note = "3"
        self.end_score = "4"


    def save(self,name, workout):
        with open(f'workouts/{name}.txt', 'a') as file:
            file.write(
                str(name) + " \n###\n" + workout + "\n###\n")
        print(f"FILE SAVED AS {self.date}")


    def load(self, title):
        with open(f'workouts/{title}.txt', 'r') as file:
            for line in file:
                print(line)