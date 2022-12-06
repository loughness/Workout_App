def save(self):
    with open('workout.txt', 'a') as file:
        file.write(
            str(self.date) + " " + self.start_note + " " + str(self.conclusion) + " " + self.end_note + " " + str(
                self.end_score) + "")


def load(self):
    with open('workout.txt', 'r') as file:
        for line in file:
            print(line)