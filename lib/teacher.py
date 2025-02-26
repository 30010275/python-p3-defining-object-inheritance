import random
from user import User

class Teacher(User):
    def __init__(self, first_name, last_name):
        """Initialize a teacher with first and last name and knowledge."""
        super().__init__(first_name, last_name)
        self.knowledge = [
            "str is a data type in Python",
            "programming is hard, but it's worth it",
            "JavaScript async web request",
            "Python function call definition",
            "object-oriented teacher instance",
            "programming computers hacking learning terminal",
            "pipenv install pipenv shell",
            "pytest -x flag to fail fast",
        ]

    def teach(self):
        """Return a random knowledge string."""
        return self.knowledge[random.randint(0, len(self.knowledge) - 1)]
