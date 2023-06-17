from DAO import SemesterDAO, SchoolClassDAO, UserDAO
from entities.User import User

if __name__ == '__main__':
    user = User(509697, "João Victor Alves", "Jv1234", 85, 992136744)
    UserDAO.insertUser(user)
