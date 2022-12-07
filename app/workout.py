import datetime
from load_save import Load_Save

class Workout():
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

    def exercise(self):
        self.ex_name = input("Exercise Name: ")

        self.type = '1 - Superset', '2 - Dropset', '3 - Regular'
        print(self.type)
        self.type = input('1,2,3:')
        while self.type != '1' and self.type != '2' and self.type != '3':
            self.type = input('1,2,3:')

        self.reps = input("Number of reps: ")

        self.sets = input("Number of sets: ")
        while not self.sets.isdigit():
            while not self.sets.isdigit():
                self.sets = input("Number of sets: ")

        print(self.sets + " = Sets")
        for i in range(0, int(self.sets)):
            self.work = self.weight_tempo()

        self.conclusion = {'Name': self.ex_name, 'Type': self.type, 'Reps': self.reps, 'Sets': self.sets, 'Workout': self.work}
        print("This is your conlusive workout: \n")
        print(self.conclusion)
        return self.conclusion

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