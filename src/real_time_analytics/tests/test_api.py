import unittest
from src.real_time_analytics.api import analytics_data, log_interaction

class TestAnalyticsAPI(unittest.TestCase):
    def test_log_interaction(self):
        initial_count = len(analytics_data)
        log_interaction({"query": "Order status", "response_time": 1.5, "outcome": "resolved"})
        self.assertEqual(len(analytics_data), initial_count + 1)

if __name__ == "__main__":
    unittest.main() 