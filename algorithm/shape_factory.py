"""
Factory is a design pattern in common usage.
Implement a ShapeFactory that can generate correct shape.

You can assume that we have only three different shapes:
Triangle, Square and Rectangle.

Example
Example 1:

Input:
ShapeFactory sf = new ShapeFactory();
Shape shape = sf.getShape("Square");
shape.draw();
Output:
  ----
 |    |
 |    |
  ----
Example 2:

Input:
ShapeFactory sf = new ShapeFactory();
shape = sf.getShape("Triangle");
shape.draw();
Output:
   /\
  /  \
 /____\
Example 3:


Input:
ShapeFactory sf = new ShapeFactory();
shape = sf.getShape("Rectangle");
shape.draw();
Output:
  ----
 |    |
  ----
"""


class Shape:
    def draw(self):
        raise NotImplementedError('This method should have inplemented !')


class Triangle(Shape):
    def draw(self):
        print("  /\\")
        print(" /   \\")
        print("/_____\\")


class Rectangle(Shape):
    def draw(self):
        print(" ----")
        print("|    |")
        print("|    |")
        print(" ----")


class Square(Shape):
    def draw(self):
        print(" -----")
        print("|     |")
        print(" -----")


class ShapeFactpry:
    # @param {string} shapeType a string
    # @return {Shape} Get object of type Shape
    def get_shape(self,shape_type):
        if shape_type == "Triangle":
            return Triangle()
        if shape_type == "Rectangle":
            return Rectangle()
        if shape_type == "Square":
            return Square()
        else:
            return None
