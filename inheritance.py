class Parent():
    def __init__(self,last_name,eye_color):
        print("Parent constructor")
        self.last_name = last_name;
        self.eye_color = eye_color;

    def show_info(self):
        print("Last name: "+self.last_name);
        print("Eye color: "+self.eye_color);

class Child(Parent):
    def __init__(self, last_name,eye_color,no_of_toys):
        print("Child constructor");
        Parent.__init__(self,last_name,eye_color)
        self.no_of_toys = no_of_toys;

miley = Child("miley","blue",5);
#print(miley.last_name);
#print(miley.no_of_toys)
miley.show_info();
        
