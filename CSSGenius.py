class CSSGenius:

    stream = "Computer Science"

    def _init_(self, classCode):
        self.classCode = classCode

a = CSSGenius(101)
b = CSSGenius(102)

print (a.stream)
print (b.stream)
print (a.classCode)

print(CSSGenius.stream)
