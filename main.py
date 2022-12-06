from start_menu import StartMenu
from workout import Workout

class StartingProcedure():
    def __init__(self):
        self.start_menu = StartMenu("Start Menu", ["Start Workout", "Exit"])
        self.workout = Workout()

    def run(self):
        while True:
            choice = self.start_menu.run()
            if choice == "1":
                self.workout.start_note()
                self.workout.exercise()
            elif choice == "2":
                break


if __name__ == "__main__":
    start = StartingProcedure()
    start.run()