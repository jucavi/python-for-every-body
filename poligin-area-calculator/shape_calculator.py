class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    
    def get_picture(self):
        shape = ""

        if self.height > 50 or self.width > 50:
            return "Too big for picture."

        for _ in range(self.height):
            shape += "*" * self.width + "\n"

        return shape

    def get_amount_inside(self,shape):
        return self.get_area() // shape.get_area()

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

    def set_side(self, length):
        self.width = length
        self.height = length

    def __repr__(self):
        return f"Square(side={self.width})"
    

