class species:
    def __init__(self, name,age):
        self.name=name
        self.age=age
    def sing(self,song):
        return f"{self.name} sings {song}" 
    def plays(self):
        return f"{self.name} is playing"
ob1=species("blue", 12)
ob2=species("red", 14)

print(f" {ob1.name} is {ob1.age} is yrs old")
print(f"{ob2.name} is {ob2.age}is yrs old ")
print(ob1.sing("happy"))
print(ob1.plays())