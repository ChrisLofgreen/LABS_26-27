

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


# pen structure:

# Southern wall: 0,0 - 30,0
# Northern wall: 0,10 - 30,10

# Beaver pen:

# Western vertical wall: 0,0 - 0,10
# Eastern between B and O: 10,0 - 10,10
# Stream: 3,1 to 3,9

# Orangutan pen:

# Western between B and O: 10,0 - 10,10
# Eastern between O and TR: 20,0 - 20,10

# Rex pen:

# Eastern vertical wall: 30,0 - 30,10
# Western between O and TR: 20,0 - 20,10

class Wall():
    def __init__(self, name, coordinates):
        self.coordinates = coordinates
        self.name = name

class PerimeterWall(Wall):
    def __init__(self, name, coordinates):
        super().__init__(name, coordinates)
        
        self.health = 5000

class DividingWall(Wall):
    def __init__(self, name, coordinates):
        super().__init__(name, coordinates)

        self.health = 500

class Forest():
    def __init__(self, name, coordinates):
        self.name = name
        self.coordinates = coordinates



'''
walls_old = {
    "b_south": 5000, 
    "b_north": 5000, 
    "b_west": 5000, 
    "b_o": 500, 
    "o_north": 5000, 
    "o_south": 5000, 
    "o_t": 500, 
    "t_north": 5000, 
    "t_south": 5000, 
    "t_east": 5000
    }
'''
forests = []

b_forest = Forest("Beaver forest", [(x, y) for x in range(1, 10) for y in range(1, 10)])
o_forest = Forest("Orangutan forest", [(x, y) for x in range(11, 20) for y in range(1, 10)])
t_forest = Forest("Tyrannosaur forest", [(x, y) for x in range(21, 30) for y in range(1, 10)])

forests.append(b_forest)
forests.append(o_forest)
forests.append(t_forest)

walls = []

b_west = PerimeterWall("Western Perimeter Wall", [(0,1), (0,2), (0,3), (0,4), (0,5), (0,6), (0,7), (0,8), (0,9)])
t_east = PerimeterWall("Eastern Perimeter Wall", [(30,1), (30,2), (30,3), (30,4), (30,5), (30,6), (30,7), (30,8), (30,9)])

b_south = PerimeterWall("Beaver-pen Southern Perimeter Wall", [(0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0), (8,0), (9,0), (10,0)])
b_north = PerimeterWall("Beaver-pen Northern Perimeter Wall", [(0,10), (1,10), (2,10), (3,10), (4,10), (5,10), (6,10), (7,10), (8,10), (9,10), (10,10)])

o_south = PerimeterWall("Orangutan-pen Southern Perimeter Wall", [(11,0), (12,0), (13,0), (14,0), (15,0), (16,0), (17,0), (18,0), (19,0), (20,0)])
o_north = PerimeterWall("Orangutan-pen Northern Perimeter Wall", [(11,10), (12,10), (13,10), (14,10), (15,10), (16,10), (17,10), (18,10), (19,10), (20,10)])

t_south = PerimeterWall("Tyrannosaur-pen Southern Perimeter Wall", [(21,0), (22,0), (23,0), (24,0), (25,0), (26,0), (27,0), (28,0), (29,0), (30,0)])
t_north = PerimeterWall("Tyrannosaur-pen Northern Parimeter Wall", [(21,10), (22,10), (23,10), (24,10), (25,10), (26,10), (27,10), (28,10), (29,10), (30,10)])

b_o = DividingWall("Dividing Wall between Beaver-pen and Orangutan-pen", [(10,1), (10,2), (10,3), (10,4), (10,5), (10,6), (10,7), (10,8), (10,9)])
o_t = DividingWall("Dividing Wall between Orangutan-pan and Tyrannosaur-pen", [(20,1), (20,2), (20,3), (20,4), (20,5), (20,6), (20,7), (20,8), (20,9)])

walls.append(b_west)
walls.append(t_east)
walls.append(b_south)
walls.append(b_north)
walls.append(o_south)
walls.append(o_north)
walls.append(t_south)
walls.append(t_north)
walls.append(b_o)
walls.append(o_t)
