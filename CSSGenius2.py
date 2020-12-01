class CSSGenius2:

    stream = 'Computer Science'

    def _init_(self, classCode):
        self.classCode = classCode

    def setAddress(self, address):
        self,address = address

    def getAddress(self):
        return self.address

a = CSSGenius2
a.setAddress("Noida, UP")
print(a.getAddress)
