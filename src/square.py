
class Square(object):

    def __init__(self, length: int):
        self.length = length

    def calculate_area(self) -> int:
        return self.length ** 2