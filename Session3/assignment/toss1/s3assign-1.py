class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    
    def introduce(self):
        print(f"나는{self.name}이고 키는 {self.height}cm이고 {self.age}살이야!")

    def yell(self):
        print("아?")
    
#a = Person('김태균', 21, 180, "123443")
#a.introduce()

class Developer(Person):
    keyboard = "기계식"
    def __init__(self, name, age, height, keyboard):
        super().__init__(name, age, height)
        self.keyboard = keyboard

    def yell(self):
        print("어?")

class Designer(Person):
    def __init__(self, name, age, height, disease):
        super().__init__(name, age, height)
        self.disease = disease
    
class  ProductManager(Person):
    def __init__(self, name, age, height):
        super().__init__(name, age, height)
    
    def  yell(self):
        print("개발자님 여기 오류있어요")

    def aging(self):
        self.age += 2
        self.height -= 5
        Developer.keyboard = "멤브레인"
        print('개발자를 새로 뽑아야하나...')

d1 = Developer('마크 주커버그', 30, 180, '기계식')
d2 = Designer('피카소', 20, 190, '근육통')
p1 = ProductManager('김태균', 21, 180)

d1.introduce()
d1.yell()
d2.introduce()
d2.yell()
p1.introduce()
p1.yell()

p1.aging()
p1.introduce()




