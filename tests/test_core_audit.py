# tests/test_core_audit.py

import unittest
from malcom.core_audit import AuditBase

# A simple subclass of AuditBase for testing purposes
class TestAudit(AuditBase):
    def __init__(self):
        super().__init__(
            name="Test Audit",
            importance="Test Importance",
            measurement_criteria="Test Criteria",
            fix_methods="Test Fix Methods",
            use_cases="Test Use Cases"
        )

    def run(self, website):
        # Simple test logic
        if "test_condition" in website:
            self.passed = True
        else:
            self.passed = False
            self.issues.append("Test condition not met.")

class TestAuditBase(unittest.TestCase):
    def test_initialization(self):
        audit = TestAudit()
        self.assertEqual(audit.name, "Test Audit")
        self.assertEqual(audit.importance, "Test Importance")
        self.assertEqual(audit.measurement_criteria, "Test Criteria")
        self.assertEqual(audit.fix_methods, "Test Fix Methods")
        self.assertEqual(audit.use_cases, "Test Use Cases")
        self.assertFalse(audit.passed)
        self.assertEqual(audit.issues, [])

    def test_run_pass(self):
        audit = TestAudit()
        website_data = {"test_condition": True}
        audit.run(website_data)
        self.assertTrue(audit.get_result())
        self.assertEqual(audit.get_issues(), [])

    def test_run_fail(self):
        audit = TestAudit()
        website_data = {"other_condition": True}
        audit.run(website_data)
        self.assertFalse(audit.get_result())
        self.assertIn("Test condition not met.", audit.get_issues())

    def test_get_metadata(self):
        audit = TestAudit()
        metadata = audit.get_metadata()
        self.assertEqual(metadata["name"], "Test Audit")
        self.assertEqual(metadata["importance"], "Test Importance")
        self.assertEqual(metadata["measurement_criteria"], "Test Criteria")
        self.assertEqual(metadata["fix_methods"], "Test Fix Methods")
        self.assertEqual(metadata["use_cases"], "Test Use Cases")

if __name__ == '__main__':
    unittest.main()
