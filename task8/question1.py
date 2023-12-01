# class is circle

class Circle:
    def __init__(self, list):
        self.numbers = list

    def display_numbers(self):
        print("the list is ")
        print(self.numbers)

number = [10, 501, 22, 37, 100, 999, 87, 351]
circle = Circle(number)
circle.display_numbers()
 