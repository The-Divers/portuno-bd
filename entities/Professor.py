from entities.User import User


class Professor (User):
    def __init__(self, id, name, password, ddd, number):
        super().__init__(id, name, password, ddd, number)
        self.professorPermissions = []

    def addProfessorPermission(self, permission):
        self.professorPermissions.append(permission)

    def removeProfessorPermission(self, index):
        self.professorPermissions.remove(index)

    def getProfessorPermission(self, permission):
        self.professorPermissions.index(permission)
