class Datetime:
    def __init__(self, day: int, month: int, year: int):
        self.d = day
        self.m = month
        self.y = year

    def limitOfMonth(self):
        if self.m == 2:
            if (self.y % 4 !=0) or (self.y % 400 in [100, 200, 300]):
                return 28
            else:
                return 29
        elif self.m in [4, 6, 9, 11]:
            return 30
        else:
            return 31

    def add(self, number: int):
        for _ in range(number):
            if self.d < Datetime.limitOfMonth(self):
                self.d += 1
            elif self.m < 12:
                self.m += 1
                self.d = 1
            else:
                self.y += 1
                self.m = 1
                self.d = 1
        return self

    def equal(self, dayB):
        if (self.d, self.m, self.y) == (dayB.d, dayB.m, dayB.y):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.d:02d}/{self.m:02d}/{self.y:04d}"