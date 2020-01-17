from collections import namedtuple, deque
import sys
import argparse
import csv

inf = float('inf')
Edge = namedtuple('Edge', ['start', 'end', 'time'])

class Graph():
    def __init__(self, edges):
        self.edges = [Edge(*edge) for edge in edges]
        self.vertices = {e.start for e in self.edges} | {e.end for e in self.edges}
 
    def dijkstra(self, source, dest):
        """return shortest path"""
        try:
            assert source in self.vertices
            assert dest in self.vertices
        except AssertionError:
            return("Please provide valid stations")
        dist = {vertex: inf for vertex in self.vertices} # assign inf to start with
        previous = {vertex: None for vertex in self.vertices}
        dist[source] = 0
        vertices_copy = self.vertices.copy()
        neighbours = {vertex: set() for vertex in self.vertices}
        for start, end, time in self.edges:
            neighbours[start].add((end, time))
 
        while vertices_copy:
            min_vert = min(vertices_copy, key=lambda vertex: dist[vertex]) # choose starting vertex
            vertices_copy.remove(min_vert)
            if dist[min_vert] == inf:
                return(f"No routes from {source} to {dest}")
            if min_vert == dest:
                break
            for vert, time in neighbours[min_vert]:
                alt = dist[min_vert] + time
                if alt < dist[vert]:
                    dist[vert] = alt
                    previous[vert] = min_vert
        path, min_vert = deque(), dest
        while previous[min_vert]:
            path.appendleft(min_vert)
            min_vert = previous[min_vert]
        path.appendleft(min_vert)
        # return(path, dist[dest])
        return(f"Result: {len(path)} stops, {dist[dest]} minutes")

def parse_csv(input_csv):
    """store csv data in memory"""
    data = []
    with open(input_csv, newline='') as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(1024))
        csvfile.seek(0)
        reader = csv.reader(csvfile, dialect)
        for row in reader:
            row[2] = int(row[2])
            try:
                assert row[2] >= 0
            except AssertionError:
                print("Cannot have negative time between stations. Please check data.")
                # sys.exit()
            row = tuple(row)
            data.append(row)
    return data

def main():
    argument = sys.argv
    argument_length = len(argument) - 1

    if(argument_length != 1):
        print("please provide the correct number of arguments")
        sys.exit()
    else:
        parser = argparse.ArgumentParser()
        parser.add_argument('--file', '-f', help='provide file name')
        args = parser.parse_args()
        csvfile = args.file
        edges = parse_csv(csvfile)
        graph = Graph(edges)
        from_station = input("What station are you getting on the train?:")
        to_station = input("What station are you getting off the train?:")
        print(graph.dijkstra(from_station, to_station))

if __name__ == "__main__":
    main()
