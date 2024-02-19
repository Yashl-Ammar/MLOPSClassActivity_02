
class StudentsInMLOps:

    def __init__(self):
        self.numberOfStudents = 0

    def enrollStudents(self, num):
        self.numberOfStudents += num

    def dropStudents(self, num):
        if(num < self.numberOfStudents):
            self.numberOfStudents -= num
            return
        
        print('Invalid number!')


    def getTotalStrength(self):
        return self.numberOfStudents

    def getClassName(self):
        print('StudentsInMLOps')
