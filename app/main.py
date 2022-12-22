from start_menu import StartMenu
from workout import Workout
from load_save import Load_Save
from workout import Setup


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
                # setup_start = self.setup.run() # -> setup_start IS A SETUP Class
                current_workout = self.workout.run() # -> current_workout IS A WORKOUT Class
                # setup_end = self.setup.end()
                # self.workout.save_file()
                # print(f"THIS IS WHAT SETUP_START.start_note IS -> {setup_start.start_note}")

            elif choice == "2":
                self.ls.load()
            elif choice == "3":
                break


if __name__ == "__main__":
    start = StartingProcedure()
    start.run()