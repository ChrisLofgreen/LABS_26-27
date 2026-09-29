



stream_squares = [
    (3, 1),
    (3, 2),
    (3, 3),
    (3, 4), 
    (3, 5),
    (3, 6),
    (3, 7),
    (3, 8),
    (3, 9)]

class Wall:
    def __init__(self, health):
        self.health = health


class PerimeterWall(Wall):
    def __init__(self, health):
        super().__init__(health)


class DividingWall(Wall):
    def __init__(self, health):
        super().__init__(health)


