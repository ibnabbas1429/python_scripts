class Dog():
    """A simple attempt tp model a Dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Creating the Sitting command for dogs"""
        print(self.name.title() + " is now sitting")

    def jump(self):
        """creating a jump command for dogs """

        print(self.name.title() + " is jumping")

    def go(self):
        """creating a jump command for dogs """

        print(f"Go! {self.name.title()}")

my_dog = Dog("bright", 8)


print(f"My dog's name is {my_dog.name.title()} and he is {str(my_dog.age)} years old.")
my_dog.sit()
my_dog.jump()

