class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")

# pylint: disable=attribute-defined-outside-init

# this part is proposital, to show how python can change classes
point1 = Point()
point1.x = 10
point1.y = 100
point1.draw()

print(point1.x)


point2 = Point()
point2.draw()

# this gives an error
# print(point2.x)
