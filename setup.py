import datetime
class Setup:

    def __init__(self):
        self.fname = ""


    def start_note(self):

        print("Start Note:\n")
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
        # print(title)
        return title

    def end(self):
        print("End Note:\n")
        self.end_note = input()
        self.end_score = input("Score: 1,2,3,4 \n")
        return self

    def show(self):
        print("\n")
        print(self.name())
        print("=========")
        self.start_note()


    def run(self):
        self.show()


setup = Setup()
setup.name()
