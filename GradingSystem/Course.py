class Course:
    #Initializes fields
    title = ""

    #Initializes a new Course object
    def __init__(self, title):
        #A Course has a title, a list of categories, and a list of students
        self.title = title
        global category_list
        category_list = []
        #global student_list
        #student_list = []
        
    #Creates a new Category object
    def create_categories(self, title):
        from Category import Category
        temp = Category(title)

        #Adds this new Category to the parent Course's list of categories
        category_list.append(temp)

    #Creates a new Student object
    #def create_student(self, name, number):
        #from Student import MyStudent
        #temp = Student(name, number)

        #Adds this new Student to the parent Course's list of students
        #student_list.append(temp)