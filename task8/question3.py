#calculate the area and perimeter

class Circle:
    __pi = 3.141 
    
    @classmethod
    def area(cls, radius):
        return cls.__pi * (radius ** 2)
    
    @classmethod
    def perimeter(cls, radius):
        return 2 * cls.__pi * radius
    
number_list = [10, 501, 22, 37, 100, 999, 87, 351]
for radius in number_list:
    circle_area = Circle.area(radius)
    circle_perimeter = Circle.perimeter(radius)
    print(f"Radius: {radius}, Area: {circle_area}, Perimeter: {circle_perimeter}")
