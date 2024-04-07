class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        self.parents = []
        self.children = []
        self.spouse = None
    
    def add_parent(self, parent):
        self.parents.append(parent)
    
    def add_child(self, child):
        self.children.append(child)
    
    def add_spouse(self, spouse):
        self.spouse = spouse
        spouse.spouse = self
    
    def is_male(self):
        return self.gender == 'male'
    
    def is_female(self):
        return self.gender == 'female'
    
    def get_parents(self):
        return self.parents
    
    def get_children(self):
        return self.children
    
    def get_spouse(self):
        return self.spouse
    
    def __str__(self):
        return self.name

# Implementation
if __name__ == '__main__':
    # Create family members
    john = Person('John', 'male', 45)
    jane = Person('Jane', 'female', 45)
    mike = Person('Mike', 'male', 25)
    susan = Person('Susan', 'female', 20)
    david = Person('David', 'male',85)
    
    # Add family relationships
    john.add_spouse(jane)
    john.add_child(mike)
    john.add_child(susan)
    john.add_parent(david)
    
    # Print family members and relationships
    print('Name:', john)
    print('Parents:', [parent.name for parent in john.get_parents()])
    print('Spouse:', john.get_spouse())
    print('Children:', [child.name for child in john.get_children()])
