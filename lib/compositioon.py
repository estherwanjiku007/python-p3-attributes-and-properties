#Is a strong form of associtaion
#It rep a owns_a_rel

class Engine:
    def __init__(self,horse_power) :
        self.horse_power=horse_power
class Car:
        def __init__(self,model,horse_power) :
            self.model=model
            self.horse_power=Engine(horse_power)
engine1=Engine(203)
car1=Car("toyota",engine1)
print(car1.horse_power)

