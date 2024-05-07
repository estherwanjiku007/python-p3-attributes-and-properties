class Human:
    def __init__(self,name):
        self.name=name
    
    def get_age(self):
        print("Retreiving age")
        return self._age
    
    def set_age(self,age):
        if isinstance(age,float) and 0<len(age)<=120:
            print(f"Setting age to { age }.")
            self._age = age    
        else:
            print("Age must be a number between 0 and 120.")

    age=property(get_age,set_age)