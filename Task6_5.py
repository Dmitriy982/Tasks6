class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки {self.title}")


class Pen(Stationery):
    def draw(self):
        print(f"Отрисовка  {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"Отрисовка  {self.title}")


class Handle(Stationery):
    def draw(self):
        print(f"Отрисовка  {self.title}")


st = Stationery("Начало")
st.draw()
pn = Pen("Ручкой")
pn.draw()
pnc = Pencil("Карандашом")
pnc.draw()
hnd = Handle("Маркером")
hnd.draw()

