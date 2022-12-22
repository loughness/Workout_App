import datetime
from load_save import Load_Save
from exercise import Exercise
from save_json import Json_obj

class Workout:
    def __init__(self):
        self.date = datetime.datetime.now()
        self.start_note = ""
        self.end_note = ""
        self.end_score = 0
        self.ex_name = ""
        self.weight = []
        self.tempo = []
        self.workouts = {}

        self.date = datetime.datetime.now()
        self.workout_title = ""
        self.entry_note = ""
        self.ex_move = {}
        self.exercises = []

        self.save_file = Json_obj()

    def new_exercise(self):

        workout_exercise = Exercise()
        workout_exercise = workout_exercise.run()

        # print(f"Start_EX -> {type(workout_exercise)}") # -> class.exercise
        self.exercises.append(workout_exercise)
        # print("The latest exercise is: \n")
        # print(f"{self.exercises[0]}") # gets first exercise name

        self.another_exercise()

        return workout_exercise

    def another_exercise(self):
        print("##################")
        answer = input("Would you like to add another exercise?\n")
        if answer == "Y":
            another_ex = self.new_exercise()
            self.exercises.append(another_ex)
        else:
            self.summary_of_workout()

    def summary_of_workout(self):
        print("This is a summary of all the exercises you did:\n")
        print(f"Number of exercises : {len(self.exercises)}")
        # names
        print("Details of exercises:")
        for i in range(0, len(self.exercises)):
            print(f"\n\t * Name: {self.exercises[i].name}")

            for j in range(0,len(self.exercises[i].sets)):
                print(f"\t\t ** Set {j+1} : {self.exercises[i].sets[j].weight} kg")
                print(f"\t\t\t ** Tempo : {self.exercises[i].sets[j].tempo}")
                print(f"\t\t\t ** Diff  : {self.exercises[i].sets[j].diff}")

    def save_workout(self, name):
        num_workouts = len(self.workouts)
        pass

    def set_start_note(self):
        print("########################################")
        print("##        ##         ##       ##      ##")
        print("########################################")
        print("^ ^ ** ** ** ** ** ** ** ** ** ** ** ^ ^")
        print("\t\tStart Note:\n")
        self.start_note = input()
        return self.start_note

    def create_workout_file(self):
        # needs to WRITE the new JSON file
        # todo

        title = ""
        full_date = datetime.date.today()

        year = full_date.year

        month_num = full_date.month
        month_word = ""
        if str(month_num) == '12':
            month_word = "December"

        day = full_date.day

        title = f"{day} {month_word} {year}"
        self.workout_title = str(title)

        self.save_file.create_file(self.workout_title)


        return self.workout_title

    def end(self):
        print("End Note:\n")
        self.end_note = input()
        self.end_score = input("Score: 1,2,3,4 \n")
        print("THIS IS SELF.start_note")
        print("**********************\n")
        print(self.start_note)
        return self

    def run(self):
        self.create_workout_file()
        print("\n")
        print(self.workout_title)
        print("=========")
        self.set_start_note()
        self.new_exercise()
        self.end()
        return self

    def save_workout(self):


        pass


class Setup:

    def __init__(self):
        self.start_note = ""

    def set_start_note(self):
        print("########################################")
        print("##        ##         ##       ##      ##")
        print("########################################")
        print("^ ^ ** ** ** ** ** ** ** ** ** ** ** ^ ^")
        print("\t\tStart Note:\n")
        self.start_note = input()
        return self.start_note

    def name(self):
        title = ""
        full_date = datetime.date.today()

        year = full_date.year

        month_num = full_date.month
        month_word = ""
        if str(month_num) == '12':
            month_word = "December"

        day = full_date.day

        title = f"{day} {month_word} {year}"
        title = str(title)

        return title

    def end(self):
        print("End Note:\n")
        self.end_note = input()
        self.end_score = input("Score: 1,2,3,4 \n")
        return self

    def show(self):
        # self.create_save_file(self.name())
        print("\n")
        print(self.name())
        print("=========")
        self.set_start_note()

    def run(self):
        print("\n")
        print(self.name())
        print("=========")
        self.set_start_note()
        return self



# test_workout = Workout()
# test_workout.new_exercise()
#
# print(f"#$#$#$#$#$##$#$#$#$$#$##$")
# print(f"exercises ->>>  {test_workout.exercises}")
# for i in range(0, len(test_workout.exercises)):
#     print(f"this is i -> {i}")
#     print(test_workout.exercises[i].name)