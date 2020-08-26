

def mean(listOfGrades):
    average = 0
    for grade in listOfGrades:
        average += grade
    average /= len(listOfGrades)
    return average


