class Album:
    GENRES = ["Hip-Hop", "Pop", "Jazz"]
    album_count=0
    def __init__(self,date) :
        self.increase_count()
        self.release_date=date
    
    def increase_count(cls,increase=1):
        cls.album_count+=increase

Shusho=Album("08/03/24")
print(Shusho.album_count)
class Song:
    
     
    all=[]
    def __init__(self,name):
         self.name=name
         Song.add_all_songs(self)

    @classmethod
    def add_all_songs(cls,song):
        cls.all.append(song)
        print([my_song.name for my_song in cls.all])
Oceans=Song("Oceans")
#print(Oceans.all)
class Grocrery_item:
    def __init__(self,name,price):
        self.name=name
        self.price=price

class Shopper:
    def __init__(self,name) :
        self.name=name
        self.grocery_list=[]

shopper=Shopper("oranges")
item1=Grocrery_item("apples",20)
item2=Grocrery_item("pineapples",30)
#Shopper.grocery_list.append(item1)
#Shopper.grocery_list.append(item2)
print(Shopper.__name__)

class Student:
    all=[]
    def __init__(self,name,age) :
        self.name=name
        self.age=age
        self.teacher=None
        Student.all.append(self)
    @property
    def teacher(self):
        return self.teacher
    @teacher.setter
    def teacher(self,value):
        if isinstance(value,Teacher):
            raise TypeError("Teacher must be an instance of Teacher class")
        self.teacher=value

class Teacher:
    def __init__(self,name):
        self.name=name
    def student(self):
        return [student for student in Student.all if Student.teacher==self ]
    def add_student(self,student):
        if not isinstance(student,Student):
            raise TypeError("Student must be an instance of Student class")
        student.teacher=student
       

    
        

        
       

    
        


        
     


        
