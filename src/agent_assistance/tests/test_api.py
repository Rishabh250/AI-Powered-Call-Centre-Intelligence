import unittest
from src.agent_assistance.api import get_assistant_suggestion

class TestAgentAssistanceAPI(unittest.TestCase):
    def test_get_assistant_suggestion(self):
        response = get_assistant_suggestion("Customer wants a refund", "session_123")
        self.assertTrue(isinstance(response, str))

if __name__ == "__main__":
    unittest.main() 