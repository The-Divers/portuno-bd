class User:
    def __init__(self, id, name, password, ddd, number):
        self.id = id
        self.name = name
        self.password = password
        self.ddd = ddd
        self.number = number
        self.permissions = []
        self.occupancies = []

    def addPermission(self, permission):
        self.permissions.append(permission)

    def removePermission(self, index):
        self.permissions.remove(index)

    def getPermission(self, permission):
        self.permissions.index(permission)

    def addOccupancy(self, occupancy):
        self.occupancies.append(occupancy)

    def removeOccupancy(self, index):
        self.occupancies.remove(index)

    def getOccupancy(self, occupancy):
        self.occupancies.index(occupancy)
