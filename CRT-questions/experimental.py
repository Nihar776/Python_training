class shape:
    side='Must have at least 3 sides to be called shape'
    def __init__(self,side):
        self.side=side

triangle = shape()
print(triangle.side)
__