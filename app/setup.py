
# CURRENTLY NOT NEEDED
# - TRANSFERED TO WORKOUT.PY

import datetime
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
        self.show()
        return self


# setup = Setup()
# setup.name()
