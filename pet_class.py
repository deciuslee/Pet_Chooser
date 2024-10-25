# Jonathan Lee
# Purpose: set up Pet Class for Pet Chooser Program

class Pet:
    def __init__(self, name, age, owner_name, animal_type):
        self.name = name
        self.age = age
        self.owner_name = owner_name
        self.animal_type = animal_type

# Getter and Setter for Name
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

# Getter and Setter for Age
    def get_age(self):
        return self.age

    def set_age(self, age):
        if isinstance(age, int) and 0 < age:
            self.age = age
        else:
            raise ValueError("Age input must be a positive integer.")

# Getter and Setter for Owner Name
    def get_owner_name(self):
        return self.owner_name

    def set_owner_name(self, owner_name):
        self.owner_name = owner_name

# Getter and Setter for Animal Type
    def get_animal_type(self):
        return self.animal_type

    def set_animal_type(self, animal_type):
        self.animal_type = animal_type

# Return string representation of pet's information
    def __str__(self):
        return (f"{self.get_name()}, the {self.get_animal_type()}. {self.get_name()} is {self.get_age()} years old. "
                f"{self.get_name()}'s owner is {self.get_owner_name()}")
