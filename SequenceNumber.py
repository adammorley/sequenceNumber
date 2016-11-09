import Persistence

class NumberGenerator(tag):
    number = 0

    def get(self):
        return self.increment()

    def increment(self):
        self.number = self.number + 1
        self.persist()
        return self.number

    def persist(self):
        Persistence.persist(self.number, tag)
        return None
