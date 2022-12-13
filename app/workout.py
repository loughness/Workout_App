import datetime
from load_save import Load_Save
from exercise import Exercise

class Workout:
    def __init__(self):
        self.date = datetime.datetime.now()
        # self.start_note = ""
        self.end_note = ""
        self.end_score = 0
        self.ex_name = ""
        self.weight = []
        self.tempo = []
        self.workouts = {}
        # self.save_file = Load_Save.save()

        self.date = datetime.datetime.now()
        self.workout_title = ""
        self.entry_note = ""
        self.ex_move = {}
        self.exercises = []

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

    def __str__(self):
        return self.exercises

# test_workout = Workout()
# test_workout.new_exercise()
#
# print(f"#$#$#$#$#$##$#$#$#$$#$##$")
# print(f"exercises ->>>  {test_workout.exercises}")
# for i in range(0, len(test_workout.exercises)):
#     print(f"this is i -> {i}")
#     print(test_workout.exercises[i].name)