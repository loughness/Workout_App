


class Exercise:
    """
    *^
    This is the individual exercise storing the Name (required),
    Body_Part (Not Needed), Reps (required), Weight (required),
    Tempo (required), Difficulty (required), Exercise_Note (Not Needed)
    ^*
    """

    def __init__(self):
        self.name = ""
        # self.tempo = ""
        self.difficulty = 0
        self.sets = []
        self.initial_reps = 0
        # self.reps = 0
        # sets[] contains set_weight[INT]
        # sets[] contains set_weight[{weight: [12], difficulty: [2]}}]
        #
        # self.weight_diff_tempo = {"weight": 0, "difficulty": 0, "tempo": "Standard"}

        # { weight_1 : 12 }
        # { weight_2 : 14 }
        # { weight_3 : 16 }
        ###
        # set_1 can call weight[0]


    def set_name(self):
        print("####################")
        self.name = input("What's the name of this exercise?\n")

        return self.name


    def new_set(self):
        finished = False
        # this is the activation of creating a new set that holds the weight for that set
        print("####################")
        self.total_sets = input("How many sets would you like to do?\n") # returns input_string
        print("####################")
        self.initial_reps = input("How many repetitions would you like to do?\n")
        self.initial_reps = int(self.initial_reps)


        # creating instances of the Sets and adding them to the exercises' Sets list
        for i in range(0, int(self.total_sets)):
            added_set = Sets(i)
            self.sets.append(added_set)

        # for the amount of said sets - ask for all the information in order
        for i in range(0, len(self.sets)):
            working_set = self.sets[i]
            # working_set.reps = self.initial_reps
            working_set.add_weight()
            working_set.add_achieved_reps()
            working_set.add_tempo()
            working_set.add_difficulty()


    def summary(self):
        print("#######################")
        print(f"This is a summary from this exercise - {self.name}:\n")
        print(f"** {self.name}")
        print(f"** {len(self.sets)} x {self.initial_reps}")

        for i in range(0, len(self.sets)):
            working_set = self.sets[i]
            print(f"Set {i+1}: Weight -> {working_set.weight}\n"
                  f"        Tempo -> {working_set.tempo}\n"
                  f"       Difficulty -> {working_set.diff}\n")
            print("**")


    def run(self):
        self.set_name()
        self.new_set()
        self.summary()

        return self

class Sets:

    def __init__(self, set_number):
        self.set_num = set_number
        self.reps = 0
        self.weight = 0
        self.tempo = "---"
        self.diff = 0
        self.achieved_reps = 0

    def add_weight(self):
        # set_number will be i starting at 0 - self.total_sets
        print("####################")
        weight = input(f"Set {self.set_num + 1} weight: \n")  # returns input_string_int
        weight = int(weight)  # returns input_int

        self.weight = weight


    def add_tempo(self):
        print("####################")
        print("What was your tempo for this weight")
        print("1 -> Paced\n"
              "\t -> A typical non-emphasized movement\n"
              "2 -> Slow\n"
              "\t -> Purposefully slowed down a bit\n"
              "3 -> Explosive\n"
              "\t -> Purposefully emphasized on fast and hard")

        self.input_tempo = input("What's the tempo of the set?\n")
        self.input_tempo = int(self.input_tempo)

        if self.input_tempo == 1:
            self.tempo = "Paced"
        elif self.input_tempo == 2:
            self.tempo = "Slow"
        elif self.input_tempo == 3:
            self.tempo = "Explosive"


    def add_reps(self):
        print("####################")
        initial_reps = input(f"How many repetitions would you like to do?\n")
        initial_reps = int(initial_reps)

        self.reps = initial_reps

    def add_achieved_reps(self):
        print("####################")
        achieved = input(f"How many repetitions did you achieve?\n")
        achieved = int(achieved)  # returns input_int

        self.achieved_reps = achieved

    def add_difficulty(self):
        print("####################")
        set_diff = input("How difficult was that last set?\n")
        set_diff = int(set_diff)

        self.diff = set_diff


    def get_total_reps(self):
        return self.reps


# curls = Exercise()
# curls.run()

# # difficulty should be in the set not the exercise itself
#
# # print(curls.new_set())
# # print(f"Your set 2 weight is : {curls.get_set_weight(2)}") # getting second weight from set CHECK
#
# print(curls.set_name())