import rclpy 
import sys
from rclpy.node import Node
from std_msgs.msg import Int16

class GeneratedMap: #generated  by bots, shared by all of them
    def __init__(self):
        self.grid = {}
        self.Frontier = set()




    def get(self,x, y):
        if (x, y) in self.grid:
            return self.grid[(x, y)]
        else:
            return None

    def setValue(self,x, y, value): #0 for free, 1 for obtacled, No value for unexplored
        self.grid[(x, y)] = value

    def remove(self,x, y):
        if (x, y) in self.grid:
            del self.grid[(x, y)]

    def search(self,value):
        result = []
        for coord, v in self.grid.items():
            if v == value:
                result.append(coord)
        return result


    def neighbors(x, y):
        # 4-directional neighbors
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        return [(x+dx, y+dy) for dx, dy in dirs]


    def bounds(self):
        # square map bounds
        if not self.grid:
            return None

        xs = [x for (x, y) in GeneratedMap.grid.keys()]
        ys = [y for (x, y) in GeneratedMap.grid.keys()]
        return min(xs), max(xs), min(ys), max(ys)


    def update_frontiers(self):
        for (x, y) in self.grid:
          if self.grid[(x,y)] == 0:
            for nx, ny in GeneratedMap.neighbors(x, y):
                if (nx, ny) not in GeneratedMap.grid:  # unexplored neighbor
                    GeneratedMap.Frontier.add((x, y))
                    break  # no need to check other neighbors

    def printmap(self):
        # render the known explored region __ is so python treats it as a special function and prints a string when we code print(str)
        b = GeneratedMap.bounds()
        if b is None:
            print("<empty map>")

        minx, maxx, miny, maxy = b
        rows = []
        for y in range(miny, maxy + 1):
            row = []
            for x in range(minx, maxx + 1):
                row.append(str(self.get(x, y)))
            rows.append(" ".join(row))
        print("\n".join(rows))


