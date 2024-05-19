import heapq
import itertools
import networkx as nx


class TSP:
    def __init__(self, file_name):
        self.cities = []
        self.distances = {}
        self.load_data(file_name)

    def load_data(self, file_name):
        try:
            with open(file_name, 'r') as file:
                data = file.readlines()
                cities_set = set()
                for line in data:
                    city1, city2, distance = line.strip().split()
                    distance = int(distance)
                    cities_set.add(city1)
                    cities_set.add(city2)
                    self.distances[(city1, city2)] = distance
                    self.distances[(city2, city1)] = distance
                self.cities = list(cities_set)
                self.distance_matrix = [[self.distances.get((c1, c2), float('inf')) for c2 in self.cities] for c1 in
                                        self.cities]
        except FileNotFoundError:
            print(f"File {file_name} not found.")
            exit(1)

    def find_index(self, city):
        return self.cities.index(city)

    def dfs(self):
        self.best_path = None
        self.min_cost = float('inf')

        def dfs_recursive(path, visited, current_cost):
            if len(path) == len(self.cities):
                return_cost = current_cost + self.distance_matrix[path[-1]][path[0]]
                if return_cost < self.min_cost:
                    self.min_cost = return_cost
                    self.best_path = path[:]
                return
            for i in range(len(self.cities)):
                if not visited[i]:
                    visited[i] = True
                    path.append(i)
                    dfs_recursive(path, visited, current_cost + self.distance_matrix[path[-2]][path[-1]])
                    path.pop()
                    visited[i] = False

        for start in range(len(self.cities)):
            dfs_recursive([start], [start == i for i in range(len(self.cities))], 0)
        return self.best_path, self.min_cost

    def ucs(self):
        pq = [(0, [0])]  # (cost, path)
        best_path, min_cost = None, float('inf')

        while pq:
            current_cost, path = heapq.heappop(pq)
            if len(path) == len(self.cities):
                return_cost = current_cost + self.distance_matrix[path[-1]][path[0]]
                if return_cost < min_cost:
                    min_cost = return_cost
                    best_path = path
            else:
                last = path[-1]
                for next_city in range(len(self.cities)):
                    if next_city not in path:
                        new_cost = current_cost + self.distance_matrix[last][next_city]
                        new_path = path + [next_city]
                        heapq.heappush(pq, (new_cost, new_path))
        return best_path, min_cost

    def mst_cost(self, unvisited):
        if len(unvisited) <= 1:
            return 0
        G = nx.Graph()
        for (i, j) in itertools.combinations(unvisited, 2):
            G.add_edge(i, j, weight=self.distance_matrix[i][j])
        mst = nx.minimum_spanning_tree(G)
        return mst.size(weight='weight')

    def a_star(self):
        pq = [(0, 0, [0], set(range(1, len(self.cities))))]  # (cost + heuristic, cost, path, unvisited)
        best_path, min_cost = None, float('inf')

        while pq:
            f, current_cost, path, unvisited = heapq.heappop(pq)
            if not unvisited:
                return_cost = current_cost + self.distance_matrix[path[-1]][path[0]]
                if return_cost < min_cost:
                    min_cost = return_cost
                    best_path = path
            else:
                last = path[-1]
                for next_city in list(unvisited):
                    new_cost = current_cost + self.distance_matrix[last][next_city]
                    new_path = path + [next_city]
                    new_unvisited = unvisited - {next_city}
                    heuristic = self.mst_cost(new_unvisited)
                    heapq.heappush(pq, (new_cost + heuristic, new_cost, new_path, new_unvisited))
        return best_path, min_cost


def main():
    file_name = input("Enter the TSP data file name: ")
    tsp = TSP(file_name)

    while True:
        print("\nChoose the technique to solve TSP:")
        print("1. Depth-First Search (DFS)")
        print("2. Uniform Cost Search (UCS)")
        print("3. A* Search")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            path, cost = tsp.dfs()
            technique = "DFS"
        elif choice == '2':
            path, cost = tsp.ucs()
            technique = "UCS"
        elif choice == '3':
            path, cost = tsp.a_star()
            technique = "A* Search"
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
            continue

        path = [tsp.cities[i] for i in path]
        print(f"\nTechnique: {technique}")
        print(f"Best Path: {' -> '.join(path)} -> {path[0]}")
        print(f"Minimum Cost: {cost}")


if __name__ == "__main__":
    main()
