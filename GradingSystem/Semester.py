class Semester:
    #Initializes fields
    title = ""

    #Initializes a new Semester object
    def __init__(self, title):
        #A Semester has a title and list of courses
        self.title = title
        global course_list
        course_list = []

    #Creates a new Course object  
    def create_courses(self, title):
        from Course import Course
        temp = Course(title)

        #Adds this new Course to the parent Semester's list of courses
        course_list.append(temp)