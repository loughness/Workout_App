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
        workout_exercise.run()

        print(f"Start_EX -> {type(workout_exercise)}")
        self.exercises.append(workout_exercise.name)
        print("The latest exercise is: \n")
        print(f"{self.exercises[0]}")

    def weight_tempo(self):

        # self.weight = []
        # self.tempo = []

        weight = input("Weight: ")
        self.weight.append(weight)
        # weight.append(self.weight)
        # while not check.isdigit():
        #     self.weight = input("Weight: ")
        #     weight.append(self.weight)

        tempo_info = 'Paced (standard), Explosive (Quick Shit), Slow'
        print(tempo_info)

        tempo = input('1,2,3:')
        self.tempo.append(tempo)
        # tempo.append(self.tempo)
        # while self.tempo != '1' and self.tempo != '2' and self.tempo != '3':
        #     self.tempo = input('1,2,3:')
        #     tempo.append(self.tempo)

        return {'Weight': self.weight, 'Tempo': self.tempo}

    def save_workout(self, name):
        num_workouts = len(self.workouts)

        pass

    def __str__(self):
        return self.name + " " + str(self.reps) + " " + str(self.weight)

# test_workout = Workout()
# test_workout.new_exercise()