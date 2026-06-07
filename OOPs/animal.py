class animal:
    def __init__(self,name,type_animal):
        self.name=name
        self.breed=type_animal
    def speak(self):
        return print(f'{self.breed} is my favourite animal')

class dog(animal):
    def __init__(self,name,breed):
        super().__init__(name,breed)
    def speak(self):
        return print(f'{self.breed} is my favourite dog')
    
tom=dog('tom','german')
print(tom.speak())