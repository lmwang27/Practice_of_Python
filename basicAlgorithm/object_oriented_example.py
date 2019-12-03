class Student(object):
    def __init__(self, name,score):
        self.name = name
        self.score = score

    # naming member function follow rules of function
    def speak(self):
        print(self.name, self.score)

# python don't support override
