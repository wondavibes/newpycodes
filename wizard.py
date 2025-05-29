from classes import Student

class Senior(Student):
    def __init__(self, name, course, house):
        self.course = course
        super().__init__(name, house)



class Pupil(Student):
    def __init__(self,name, house, blouse):
        self.blouse = blouse
        super().__init__(name, house)