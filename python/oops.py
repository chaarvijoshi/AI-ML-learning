# class student:
#     pass

# student1 = student()

# student1.name = "chaarvi"
# student1.age =21
# student1.course = "python"

# class student:
#     def __init__(self,name,age):
#        self.name=name
#        self.age=age
       
#     def show(self):
#         print(self.name)
#         print(self.age)   
        
# student1 = student("chaarvi",21)
# student2 = student("manas",22)        

# student1.show()
# student2.show()

# class student:
#     school = "ABC"
    
# s1 = student()
# s2 = student()

# student.school = "MMPS"

# s2.school = "DPS"

# print(s1.school)
# print(s2.school)    

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
class teacher(person):
    pass

t1=teacher("chaarvi",21)
t2=teacher("riya",23)

print(t1.name)
print(t2.name)       







