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

        self.ex_data = json.loads(exercise_json_template)


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

    def set_ex_name(self, ex_name):
        self.ex_data["exercise_name"] = ex_name
        return self.ex_data

    def set_initial_sets(self, sets):
        self.ex_data["initial_sets"] = sets
        return self.ex_data

    def create_exercise(self, name):

        self.workout_data["exercises"].append(self.set_ex_name(name))
        self.workout_data["exercises"].append(self.set_initial_sets(12))

    def overview(self):
        print(self.workout_data["exercises"])
        # print(self.ex_data)



new_file = json_obj()
new_file.set_date(23)
new_file.set_title("December the fifteenth")
new_file.overview()
new_file.create_exercise("Curls")
new_file.overview()
new_file.create_exercise("Bench")

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



