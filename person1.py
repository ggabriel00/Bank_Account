class Person:
    def _init_(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)

p = Person('Shwetanshu')
p.say_hi()
