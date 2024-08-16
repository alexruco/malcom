# malcom/core_audit.py

from abc import ABC, abstractmethod

class AuditBase(ABC):
    def __init__(self, name, importance, measurement_criteria, fix_methods, use_cases):
        self.name = name
        self.importance = importance
        self.measurement_criteria = measurement_criteria
        self.fix_methods = fix_methods
        self.use_cases = use_cases
        self.passed = False
        self.issues = []

    @abstractmethod
    def run(self, website):
        pass

    def get_result(self):
        return self.passed

    def get_issues(self):
        return self.issues

    def get_metadata(self):
        return {
            "name": self.name,
            "importance": self.importance,
            "measurement_criteria": self.measurement_criteria,
            "fix_methods": self.fix_methods,
            "use_cases": self.use_cases,
        }
