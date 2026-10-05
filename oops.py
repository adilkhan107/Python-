# create a class
class collage :
    student = 'Btech '
    year = "2025"
    course = "CSE"
Adil  = collage()  # create an object of class
dev   =    collage()    
print(dev)
print(dev.student, dev.year, dev.course) # call the class variable using object 

print(Adil.student, Adil.year, Adil.course) 



# constructor in python
class collage:
    def __init__(self , student , year , course ):
        self.student = student
        self.year = year
        self.course = course

stud1 = collage("adil","2024","BBA")   # create an object of class
stud2 = collage("dev","2023" ,"EEC")   # create an object of class
stud3 = collage("amit","2025","CSE")   # create an object of class
print(stud1.student)
print(stud2.year)
print(stud3.course)
 # call the class variable using object 

'''

 Attribute 
there are two types of attributes in python
1. Instance attribute   
2. Class attribute'

'''

class collage:
    collage_name  = "Mind power University"  # class attribute
    def __init__(self , student , year , course ) :
        self.student = student  # instance attribute
        self.year = year      # instance attribute
        self.course = course  # instance attribute  
student1 = collage("adil","2024","BBA")   # create an object of class        
print(collage.collage_name)  # call the class attribute using class name    
print(student1.student, student1.year, student1.course)  # call the instance attribute using object name
