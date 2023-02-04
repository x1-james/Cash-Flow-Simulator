# SCENARIOS CLASS
# Project Class that keeps track of the project's identifier, description, cost, and status

class Scenarios:
    def __init__(self, name, probability):
        self.name = name
        self.probability = probability

    def __str__(self):
        return f"{self.name} - {self.probability}"
