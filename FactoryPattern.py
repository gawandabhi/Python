class Circle:
    def draw(self):
        print("Drawing the circle")
        
class Square:
    def draw(self):
        print("Drawing the Square")        
        
class ShapeFactory:
    def get_shape(self,shape_type):
        if shape_type == "circle":
            return Circle()
        elif shape_type == "square":
            return Square()
        else:
            return None
        
factory = ShapeFactory()

shape1 = factory.get_shape("circle")
shape1.draw()              

shape2 = factory.get_shape("square")
shape2.draw()