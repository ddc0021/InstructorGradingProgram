class Assignment: 
    #Initializes fields
    title = ""
    description = ""
    weight = ""
    max_score = ""

    #Initializes a new Assignment object
    def __init__ (self, title, description, weight, max_score):
        #An Assignment has a title, a description, a grade weight, a maximum grade score
        self.title = title
        self.description = description
        self.weight = weight
        self.max_score = max_score