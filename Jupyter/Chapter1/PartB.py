import re


def grades():
    with open("assets/grades.txt", "r") as file:
        listOfStudents = file.read()
    pattern = r'^([A-Za-z\s]+): B\b' # Regex pattern to match lines ending with ", B"
    b_students = re.findall(pattern, listOfStudents, re.MULTILINE)

    return b_students

def findBGrades():
    with open("assets/grades.txt", "r") as file:
        listOfStudents = file.read()
    pattern = r'^(.+): B\b' # Regex pattern to match lines ending with ", B"

    b_students = re.findall(pattern, listOfStudents, re.MULTILINE)

    return b_students


assert len(findBGrades()) == 16
print(findBGrades())