class Calculation:
    def __init__(self, a, b, strategy):
        self.a = a
        self.b = b
        self.strategy = strategy
        self.result = None
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self)

    def execute(self):
        self.result = self.strategy.execute(self.a, self.b)
        self.notify()
        return self.result

    def __str__(self):
        return f"{self.a} {self.strategy.__class__.__name__} {self.b} = {self.result}"

