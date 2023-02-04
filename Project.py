# PROJECT CLASS
# Project Class that keeps track of the project's identifier, description, cost, and status

# Import packages
import datetime as dt


class Project:
    def __init__(self, identifier, description, value, status, estimated_completion):
        self.identifier = identifier
        self.description = description
        self.value = value
        self.status = status
        self.estimated_completion = estimated_completion

    def is_completed(self):
        if dt.today() >= self.estimated_completion and self.status != "Completed":
            return True
        else:
            return False

    def __str__(self):
        return f"{self.identifier} {self.description} {self.value} {self.status}"

    def __eq__(self, other):
        return self.identifier == other.identifier
