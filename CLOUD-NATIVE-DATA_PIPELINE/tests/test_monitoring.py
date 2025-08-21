import unittest
from src.monitoring.observability import Observability

class TestObservability(unittest.TestCase):

    def setUp(self):
        self.observability = Observability()

    def test_define_alert(self):
        rule = {"condition": "cpu_usage > 80", "action": "send_alert"}
        self.observability.define_alert(rule)
        # Assuming there's a way to check if the alert was defined
        self.assertIn(rule, self.observability.alerts)

    def test_generate_metrics(self):
        data = {"cpu_usage": 75, "memory_usage": 60}
        metrics = self.observability.generate_metrics(data)
        self.assertEqual(metrics["cpu_usage"], 75)
        self.assertEqual(metrics["memory_usage"], 60)

if __name__ == '__main__':
    unittest.main()