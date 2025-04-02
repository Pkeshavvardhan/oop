class subject:
    grade=10
    name="Pinochio"
    def intro(self):

     print("hi i am student")

    def details(self):
       print("i study in grade", self.grade)
       print("my name is ", self.name)
ob=subject()
ob.intro()
ob.details()