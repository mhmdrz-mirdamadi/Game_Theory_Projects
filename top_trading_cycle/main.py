from itertools import cycle


class Directed_Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.edges = dict([(v, []) for v in range(1, num_vertices + 1)])

    def add_edge(self, from_v, to_v):
        self.edges[from_v].append(to_v)

    def find_cycle(self):
        for start_vertex in self.edges.keys():
            visited = set()
            cycle = set()
            end_vertex = self.edges[start_vertex][0]

            visited.add(start_vertex)
            visited.add(end_vertex)

            cycle.add(start_vertex)
            cycle.add(end_vertex)

            vertex_in_cycle = True
            while True:
                end_vertex = self.edges[end_vertex][0]

                if end_vertex == start_vertex:
                    return cycle

                if end_vertex in visited:
                    vertex_in_cycle = False
                    break

                visited.add(end_vertex)
                cycle.add(end_vertex)

            if not vertex_in_cycle:
                continue


num_agents = int(input('Enter the number of agents: '))
preference_matrix = []

print('Enter the preferences of each agent (separated by space)')
for index in range(num_agents):
    agent_preferences = list(
        map(int, input(f'Agent {index + 1}: ').split()))
    preference_matrix.append(agent_preferences)

dg = Directed_Graph(num_agents)
for i in range(num_agents):
    dg.add_edge(i + 1, preference_matrix[i][0])

print(dg.find_cycle())
