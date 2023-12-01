#proper number variable

class Circle:
    def __init__(self, num_list):
        self.numbers = num_list
        self.__pi = 3.141 

    def display_numbers(self):
        print("Numbers in the list:")
        print(self.numbers)

    def calculate_area(self, radius):
        area = self.__pi * (radius ** 2)
        return area

number = [10, 501, 22, 37, 100, 999, 87, 351]
circle = Circle(number)
circle.display_numbers()

radius = 5
area = circle.calculate_area(radius)
print(f"Area of a circle with radius {radius} is: {area}")
