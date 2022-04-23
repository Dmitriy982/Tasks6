class Worker:

    def __init__(self, name, surname, pos, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = pos
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return sum(self._income.values())


m = Position("Dmitriy", "Alexeev", "employee", 1000, 2000)
print(m.get_full_name())
print(m.position)
print(m.get_total_income())

