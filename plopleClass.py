class Person:
    def __init__(self,firstname,lastname,age):
        self.firstname=firstname
        self.lastname=lastname
        self.age=age
    
    def __str__(self):
        return f"{self.firstname}, {self.lastname}, {self.age}"

def people_sort(ls,type):
    return sorted(ls,key=lambda x:getattr(x,type))

p1=Person("Michael","Smith",40)
p2=Person("Alice","Waters",21)
p3=Person("Zoey","Jones",29)

sortByFirstname=people_sort([p1,p2,p3],"firstname")

# Print each person in the sorted list
for person in sortByFirstname:
    print(person)
