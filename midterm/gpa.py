"""gpa.py

Software Design Fall 2014 Midterm. Problem 1
"""


def main():
    student_gpas = {}
    recur_student_gpas = {}
    student_grades = read_grades('raw_grades.txt')
    for student, grades in student_grades.iteritems():
        currgpa = calc_gpa(grades)  # Does not match recursive funct
        recur_currgpa = recur_calc_gpa(grades)  # Does not match calc_gpa()
        student_gpas[student] = currgpa
        recur_student_gpas[student] = recur_currgpa
    graduates, superseniors = sort_students(student_gpas)
    graduates_dict, superseniors_dict = sort_students_dict(student_gpas)
    printgpas(student_gpas)
    writegpas(student_gpas, 'class-grades.txt')
    writegpas(recur_student_gpas, 'recursive-class-grades.txt')


def calc_gpa(gradelist):
    """Takes in a list of grades (either 'A', 'B', 'C', or 'D') and calculates a GPA.

    Inputs: gradelist is a list of grades. A grade is a single capital character 'A', 'B', 'C', or 'D'.
    Outputs: gpa is the calculated GPA on a four-point scale.
    """
    gradesum = 0
    # GPA dictionary for part a.
    gpadict = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}
    for grade in gradelist:
        gradesum += gpadict[grade]
    gpa = gradesum / float(len(gradelist))
    # If more than two decimal points, round to two decimal points
    return round(gpa, 2)


def read_grades(gradefile):
    """Read a text file (with formatting specified in the midterm) of students' grades.students

    Inputs: gradefile is a filepath to the desired text file. EX: 'raw_grades.txt'
    Outputs: studentgrades is a dictionary of all students' grades. Key is student name (e.g. "Kyle")
    Value is a list of grades for the key.
    """
    studentgrades = {}
    openfile = open(gradefile, 'r')
    for line in openfile.readlines():
        # sg = line.replace(('\n'), '').split(',')
        sg = line.translate(None, ' \n').split(',')
        studentgrades[sg[0]] = sg[1:]
    return studentgrades


def printgpas(studentgpas):
    """Formats and prints the gpas dictionary output from main() to console."""
    for student, gpa in studentgpas.iteritems():
        print '%s\'s grade point average is %.2f.' % (student, gpa)


def writegpas(studentgpas, textfilename):
    """Formats and writes the gpas dictionary output from main() to a text file."""
    gradefile = open(textfilename, 'w')
    for student, gpa in studentgpas.iteritems():
        if len(student) < 7:
            gradefile.write('%s:\t\t%.2f' % (student, gpa) + '\n')
        else:
            gradefile.write('%s:\t%.2f' % (student, gpa) + '\n')
    gradefile.close()


def recur_calc_gpa(gradelist):
    """Takes in a list of grades (either 'A', 'B', 'C', or 'D') and recursibely calculates a GPA.

    Inputs: gradelist is a list of grades. A grade is a single capital character 'A', 'B', 'C', or 'D'.
    Outputs: gpa is the calculated GPA on a four-point scale.
    """

    gpadict = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}
    if len(gradelist) == 1:
        return gpadict[gradelist[0]]
    else:
        return (gpadict[gradelist[0]] + recur_calc_gpa(gradelist[1:])) / 2.0


def sort_students(studentgpas):
    """Making lists. Problem 2a"""
    questiontwo_list = []
    superseniors = []
    graduates = []
    for student, gpa in studentgpas.iteritems():
        questiontwo_list.append((student, gpa))

    for item in questiontwo_list:
        if item[1] >= 2.5:
            graduates.append(item)
        else:
            superseniors.append(item)

    return graduates, superseniors


def sort_students_dict(studentgpas):
    """Making dictionaries. Problem 2b"""
    superseniors_dict = {}
    graduates_dict = {}
    for student, gpa in studentgpas.iteritems():
        if gpa >= 2.5:
            graduates_dict[student] = gpa
        else:
            superseniors_dict[student] = gpa

    return graduates_dict, superseniors_dict

if __name__ == '__main__':
    main()
