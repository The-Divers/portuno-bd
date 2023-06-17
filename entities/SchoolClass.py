class SchoolClass:
    def __init__(self, id, day_week, subject):
        self.id = id
        self.day_week = day_week
        self.subject = subject
        self.occupancies = []

    def addOccupancy(self, occupancy):
        self.occupancies.append(occupancy)

    def removeOccupancy(self, index):
        self.occupancies.remove(index)

    def getOccupancy(self, occupancy):
        self.occupancies.index(occupancy)


