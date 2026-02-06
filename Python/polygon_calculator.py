from math import sqrt

class Rectangle :
    def __init__(self, width, height) -> None :
        self.width = width
        self.height = height 

    def set_width (self, value) :
        self.width = value
    
    def set_height(self, value) :
        self.height = value
    
    def get_area(self) :
        return self.width * self.height
    
    def get_perimeter(self) :
        return 2*(self.width+self.height)
    
    def get_diagonal(self) -> float :
        return sqrt(self.width**2 + self.height**2)
    
    def get_picture(self) :
        if self.width > 50 or self.height > 50 :
            return "Too big for picture."
        res = ''
        for i in range(self.height) :
            for j in range(self.width) :
                res += '*'
            res += '\n'
        return res
    
    def get_amount_inside(self, other) -> int :
        fits_width = self.width // other.width 
        fits_height = self.height // other.height
        return fits_width * fits_height
    
    def __str__(self) :
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle) :
    def __init__(self, side_length) :
        self.side_length = side_length
        self.width = side_length
        self.height = side_length
    
    def set_width(self, value) :
        self.width = value
        self.height = value
        self.side_length = value
    
    def set_height(self, value) :
        self.width = value
        self.height = value
        self.side_length = value

    def set_side(self, value) :
        self.width = value
        self.height = value
        self.side_length = value
    
    def __str__(self) :
        return f"Square(side={self.side_length})"

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

sq2 = Square(5)
print(sq2)

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
