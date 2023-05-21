import task_11


class JellyBean(task_11.Dessert):
    def __init__(self, flavor='', name='', calories=0):
        super(JellyBean, self).__init__(name, calories)
        self.flavor = flavor

    @property
    def flavol(self):
        return self.flavor

    @flavol.setter
    def flavol(self, value):
        self.flavor = value

    def is_delicious(self):
        if self.flavol == "black licorice":
            return False
        return True



'''
y = JellyBean()
y.flavol = "black licorice"

print(y.is_delicious())
y.flavol = "black licoriceb"

print(y.is_delicious())
y.name = "cake"
y.calories = 199.9999

print(y.calories, y.is_healthy())
'''