class parent:
 def __init__(self,name,rollno) -> None:
    self.name=name
    self.rollno=rollno
    print('From the constructor :',name,' ',rollno)
 def details(self):
     print('From the parent class details function :',self.name,' ',self.rollno)

class child(parent):
    def ganesh_details(self):
        print('From ganesh team :',self.name,' ',self.rollno)

obj=child('JAFFA',420)
obj.ganesh_details()
obj.details()




