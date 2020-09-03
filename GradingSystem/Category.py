class Category:
    #Initializes fields
    title = ""

    #Initializes a new Category object
    def __init__(self, title):
        #A Category has a title and a list of assignments
        self.title = title
        global assignment_list
        assignment_list = []

    #Creates a new Assignment object
    def create_assignments(self, title, description, weight, max_score):
        from Assignment import Assignment
        temp = Assignment(title, description, weight, max_score)

        #Adds this new Assignment to the parent Category's list of assignments
        assignment_list.append(temp)