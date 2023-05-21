class Dessert:
    def __init__(self, name="", calories=0):
        self.name = name
        self.calories = calories

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def calories(self):
        return self._calories

    @calories.setter
    def calories(self, calories):
        self._calories = calories

    def is_healthy(self):
        if type(self.calories) != (int or float):
            return None
        if self.calories < 200:
            return True
        else:
            return False

    def is_delicious(self):
        return True


'''x = Dessert()

x.__init__("cake", 150)
print(x.is_healthy())
print(x.is_delicious())
s = x.name
print(s)
x.name = "apple cake"
s = x.name
print(s)
x.calories = 205
print(x.calories)
print(x.is_healthy())'''

