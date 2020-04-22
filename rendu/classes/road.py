import unittest


class Road:
    def __init__(self, intersection1, intersection2, distance):
        self.intersection1 = intersection1
        self.intersection2 = intersection2
        self.distance = distance


class RoadNetwork:
    def __init__(self, road_list):
        self.road_list = road_list
        self.nb_intersection = len(road_list)

    def get_neighbours(self, intersection):
        neighbours = []

        for item in self.road_list:
            if item.intersection1 == intersection:
                neighbours.append(item.intersection2)

        return neighbours

    def get_distance(self, intersection1, intersection2):
        distance = 0

        for item in self.road_list:
            if (item.intersection1 == intersection1 and item.intersection2 == intersection2) or (
                    item.intersection2 == intersection1 and item.intersection1 == intersection2):
                distance = item.distance

        if distance == 0:
            print('Les 2 intersections ne sont pas valide (non voisines ou inexistantes)')
        else:
            return distance

    def shortest_path(self, origin, destination):
        print('chemin le plus court')


Network = RoadNetwork([
    Road(0, 1, 4),
    Road(0, 7, 8),
    Road(1, 7, 11),
    Road(1, 2, 8),
    Road(7, 8, 7),
    Road(7, 6, 1),
    Road(2, 8, 2),
    Road(8, 6, 6),
    Road(2, 3, 7),
    Road(2, 5, 4),
    Road(5, 6, 2),
    Road(3, 5, 14),
    Road(3, 4, 9),
    Road(4, 5, 10)
])

intersection0_neighbours = Network.get_neighbours(0)
intersection07_distance = Network.get_distance(1, 7)
