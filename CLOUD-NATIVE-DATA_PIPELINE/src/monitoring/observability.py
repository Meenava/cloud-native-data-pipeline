class Observability:
    def __init__(self):
        self.alerts = []
        self.metrics = {}

    def define_alert(self, rule):
        self.alerts.append(rule)

    def generate_metrics(self, data):
        for key, value in data.items():
            if key in self.metrics:
                self.metrics[key].append(value)
            else:
                self.metrics[key] = [value]