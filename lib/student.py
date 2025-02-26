from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        """Initialize a student with first and last name and an empty knowledge list."""
        super().__init__(first_name, last_name)
        self.knowledge = []

    def learn(self, knowledge_string):
        """Add a knowledge string to the student's knowledge list."""
        self.knowledge.append(knowledge_string)
