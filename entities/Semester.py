from datetime import datetime

class Semester:
    def __init__(self, name, beginning_date, ending_date):
        self.name = name
        self.beginning_date = datetime.strptime(beginning_date, "%d/%m/%Y").strftime("%Y-%m-%d")
        self.ending_date = datetime.strptime(ending_date, "%d/%m/%Y").strftime("%Y-%m-%d")
