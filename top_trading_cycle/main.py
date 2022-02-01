class Directed_Graph:
    def __init__(self):
        self.num_vertices = 0
        self.edges = dict()

    def add_edge(self, from_v, to_v):
        self.edges[from_v] = to_v
        self.num_vertices += 1

    def find_cycle(self):
        for start_vertex in self.edges.keys():
            visited = set()
            cycle = set()
            end_vertex = self.edges[start_vertex]

            visited.add(start_vertex)
            visited.add(end_vertex)

            cycle.add(start_vertex)
            cycle.add(end_vertex)

            vertex_in_cycle = True
            while True:
                end_vertex = self.edges[end_vertex]

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

stable_permutation = dict()
agents = list(range(1, num_agents + 1))

while len(agents) > 0:
    dg = Directed_Graph()
    for agent in agents:
        dg.add_edge(agent, preference_matrix[agent - 1][0])

    cycle = list(dg.find_cycle())
    for vertex in cycle:
        stable_permutation[vertex] = dg.edges[vertex]
        preference_matrix[vertex - 1] = []
        agents.remove(vertex)

    for agent in preference_matrix:
        for vertex in cycle:
            if vertex in agent:
                agent.remove(vertex)

stable_permutation = dict(
    sorted(stable_permutation.items(), key=lambda item: item[0]))

print('\nStable Permutation:')
for key in stable_permutation.keys():
    print(f'Agent {key} <--> House {stable_permutation[key]}')
