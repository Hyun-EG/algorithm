class Person:
    def __init__(self, name_param):
        self.name = name_param
        print("hihi i am created", self, self.name)

    def talk(self):
        print("안녕하세요. 저는 ",self.name,"입니다.")

person_1 = Person("박성현")
person_1.talk()

person_2 = Person("박셩현")
person_2.talk()
