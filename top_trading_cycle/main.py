class Directed_Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.edges = dict([(v, []) for v in range(1, num_vertices + 1)])

    def add_edge(self, from_v, to_v):
        self.edges[from_v].append(to_v)


num_agents = int(input('Enter the number of agents: '))
preference_matrix = []

for index in range(num_agents):
    agent_preferences = list(
        map(int, input(f'Enter the preferences of agent {index + 1}: ').split()))
    preference_matrix.append(agent_preferences)

dg = Directed_Graph(num_agents)
for i in range(num_agents):
    dg.add_edge(i + 1, preference_matrix[i][0])
print(dg.edges)
