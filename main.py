from DAO import SemesterDAO, SchoolClassDAO, UserDAO
from entities import User, SchoolClass, Semester, Classroom, Professor, Ocupancy, Permission

if __name__ == '__main__':
    UserDAO.deleteUser(2)
