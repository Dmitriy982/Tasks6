class Road:

    def __init__(self):
        self._length = 5000
        self._width = 20

    def solve(self, w, s):
        m = self._length * self._width * w * s
        return m

    def tons(self, n):
        return int(n / 1000)


r = Road()
n = r.solve(25, 5)
print(r.tons(n))
