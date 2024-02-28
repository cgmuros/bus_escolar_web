from enum import Enum


class Route(Enum):
    INDEX = "/"
    PARENTS = "/parents"
    PARENTS_MAIN = "/parents_main"
    DRIVERS = "/drivers"
    SCHOOLS = "/schools"
    SOLUTIOINS = "/solutions"
    ABOUT = "/about"
    REGISTER = "/register"
    PARENTS_KIDS = "/parents_kids"
    PARENTS_ADD_STUDENT = "/parents_kids/add_student"


