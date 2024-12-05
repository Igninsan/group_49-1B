class Figure:
    unit = 'cm'

    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def info(self):
        pass

class Square(Figure):
    def __init__(self, side_length):
        self.__side_length = side_length

    def calculate_area(self):
        return self.__side_length ** 2

    def info(self):
        print(f'Square side length: {self.__side_length}{Figure.unit}, area: {self.calculate_area()}{Figure.unit}')

class Rectangle(Figure):
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calculate_area(self):
        return self.__width * self.__length

    def info(self):
        print(f'Rectangle length: {self.__length}{Figure.unit}, width: {self.__width}{Figure.unit},'
              f' area: {self.calculate_area()}{Figure.unit}')


first_square = Square(5)
second_square = Square(15)
first_rectangle = Rectangle(3, 4)
second_rectangle = Rectangle(6, 10)
third_rectangle = Rectangle(12, 20)

figures_list = [first_square, second_square, first_rectangle, second_rectangle, third_rectangle]

for figure in figures_list:
    figure.info()