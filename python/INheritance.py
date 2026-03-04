class parent:
    def __init__(self,fname,lname):
        self.fname=fname;
        self.lname=lname;
    def details(self):
        print(f"My {self.fname} and {self.lname}");
class child(parent):
    def __init__(self, fname, lname):
     parent.__init__(self, fname, lname)
a=child("firstname","lastname")
print(a.fname,a.lname);