import task_11


class JellyBean(task_11.Dessert):
    def __init__(self, flavor='', name ='', calories=0):
        super(JellyBean, self).__init__(name, calories)
        self.flavor = flavor

    @property
    def flavol(self):
        return self._flavor

    @flavol.setter
    def flavor(self, flavor):
        self._flavor = flavor

    def is_delicious(self):
        if self.flavol == "black licorice":
            return False
        return True


y = JellyBean()
y.__init__("black licorice")

print(y.is_delicious())
y.name = "cake"
print(y.is_healthy())
