class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}

        for start, end in edges:
            if start not in self.graph_dict:
                self.graph_dict[start] = [end]
            else:
                self.graph_dict[start].append(end)

    def get_routes(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []

        routes = []

        for route in self.graph_dict[start]:
            if route not in path:
                new_path = self.get_routes(route, end, path)
                for rt in new_path:
                    routes.append(rt)

        return routes


routes = [
    ("Mumbai", "Paris"),
    ("Mumbai", "Dubai"),
    ("Paris", "Dubai"),
    ("Paris", "New York"),
    ("Dubai", "New York"),
    ("New York", "Toronto"),
]

gra = Graph(routes)

lst_routes = gra.get_routes("Mumbai", "New York")
print(lst_routes)
final_routes = []

for items in lst_routes:
    final_routes.append((len(items), items))

final_routes.sort(reverse=False)

print(final_routes[0][1])
