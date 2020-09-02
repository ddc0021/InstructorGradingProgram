class Teacher:
    #Initializes fields
    name = ""
    password = ""

    #Initializes a new Teacher object
    def __init__(self, name, password):
        #A Teacher has a name, a password, and a list of semesters.
        self.name = name
        self.password = password
        global semester_list
        semester_list = []

#Creates a new Semester object
    def create_semesters(self, input_title):
        from Semester import Semester
        temp = Semester(input_title)

        #Adds this new Semester to the parent Teacher's list of semesters
        semester_list.append(temp)