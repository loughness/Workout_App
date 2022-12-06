from start_menu import StartMenu
from workout import Workout
from load_save import Load_Save
from setup import Setup


class StartingProcedure():
    def __init__(self):
        self.start_menu = StartMenu("Start Menu", ["Start Workout", "Load", "Exit"])
        self.workout = Workout()
        self.ls = Load_Save()
        self.setup = Setup()


    def run(self):
        while True:
            choice = self.start_menu.run()
            if choice == "1":
                self.setup.run()
                self.workout.exercise()
                self.setup.end()
                self.ls.save()
            elif choice == "2":
                self.ls.load()
            elif choice == "3":
                break


if __name__ == "__main__":
    start = StartingProcedure()
    start.run()