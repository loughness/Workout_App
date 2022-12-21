import json

workout_json_obj = '''
{
    "workout":
    [
        {"date": "shite"},
        {"start_note": ""},
        {"exercises":
            [
                {
                     "exercise name": "",
                     "initial sets": 0,
                     "initial reps": 0,
                     "sets": [],
                     "exercise note": ""
                 }
            ]
        },
        {"end note": ""},
        {"workout rating": 0}
    ]
}
'''

workout_json_template = '''
{
    "workout":
        {
        "date": "",
        "title": "",
        "start_note": "",
        "exercises": [],
        "end_note": "",
        "workout_rating": 0
        }
}
'''

exercise_json_template = '''
{   
    "exercise_name": "", 
    "initial_sets": 0,
    "initial_reps": 0,
    "sets": [],
    "exercise_note": ""
}
'''

class json_obj:

    def __init__(self):
        self.data = json.loads(workout_json_template)
        self.workout_data = self.data["workout"]

    def set_date(self, date):
        self.workout_data["date"] = date

    def get_date(self):
        return self.workout_data["date"]

    def set_title(self, title):
        self.workout_data["title"] = title

    def get_title(self):
        return self.workout_data["title"]

    def set_start_note(self, start_note):
        self.workout_data["start_note"] = start_note

    def get_start_note(self):
        return self.workout_data["start_note"]

    def set_end_note(self, end_note):
        self.workout_data["end_note"] = end_note

    def set_workout_score(self, score):
        self.workout_data["workout_rating"] = score

    def set_ex_name(self, exercise_temp, ex_name):
        exercise_temp["exercise_name"] = ex_name
        return exercise_temp

    def set_initial_sets(self, exercise_temp, sets):
        exercise_temp["initial_sets"] = sets
        return exercise_temp

    def set_initial_reps(self, exercise_temp, reps):
        exercise_temp["initial_reps"] = reps
        return exercise_temp

    def create_exercise(self, name, initial_sets, initial_reps):
        new_ex_file = json.loads(exercise_json_template)
        # created a new exercise file here so that it will not reference one that was made once
        # at the beginning of the class
        exercise = self.set_ex_name(new_ex_file, name)
        # self.workout_data["exercises"].append(ex_name)
        exercise = self.set_initial_sets(new_ex_file, initial_sets)
        exercise = self.set_initial_reps(new_ex_file, initial_reps)

        self.workout_data["exercises"].append(exercise)

    def add_set(self, weight, reps, difficulty, tempo = None):
        set = [weight, reps, tempo, difficulty]
        exercise = self.workout_data["exercises"]
        exercise[-1]["sets"].append(set)

    def add_exercise_note(self, ex_note):
        exercise = self.workout_data["exercises"]
        exercise[-1]["exercise_note"]  = ex_note


    def overview(self):
        print("OVERVIEW")
        print("WORKOUT_DATA")
        print(self.workout_data)
        print("***")



new_file = json_obj()
new_file.set_date(23)
new_file.set_title("December the fifteenth")
new_file.set_start_note("Working all over today")
new_file.overview()
new_file.create_exercise("Curls", 3, 12)
new_file.add_set(14,12,1,"paced")
new_file.add_set(16,12,1,"paced")
new_file.add_set(20,8,3,"slow")
new_file.overview()
new_file.create_exercise("Bench", 4, 10)
new_file.add_set(60,12,2,"paced")
new_file.overview()
new_file.create_exercise("Pull-ups", 5, 10)
new_file.add_set(0,12,1,"paced")
new_file.add_exercise_note("Tough on the back")
new_file.set_end_note("Fun day pushing hard!")
new_file.set_workout_score(2)
new_file.overview()




#
# data = json.loads(workout_json_template)
# # GET ()
# workout_dict = data["workout"]
# workout_date = workout_dict["date"]
# workout_title = workout_dict["title"]
# workout_start_note = workout_dict["start_note"]
# workout_exercises_list = workout_dict["exercises"]
# workout_end_note = workout_dict["end_note"]
# workout_rating = workout_dict["workout_rating"]
# # SET ()
#
# workout_dict["workout_rating"] = 3
#
#
#
# j_sonify = json.dumps(workout_dict)
#
# print(j_sonify)


# "sets":
#                          [
#                             {"weight": 12, "reps": 12, "tempo": "paced", "difficulty": 1},
#                             {"weight": 14, "reps": 12, "tempo": "paced", "difficulty": 2},
#                             {"weight": 16, "reps": 12, "tempo": "slow", "difficulty": 2}
#                          ],



