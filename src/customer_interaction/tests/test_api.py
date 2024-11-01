import unittest
from src.customer_interaction.api import generate_response

class TestCustomerInteractionAPI(unittest.TestCase):
    def test_generate_response(self):
        response = generate_response("What is the status of my order?")
        self.assertTrue(isinstance(response, str))

if __name__ == "__main__":
    unittest.main() 