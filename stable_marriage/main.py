import networkx as nx
import matplotlib.pyplot as plt


def get_matrix(rows):
    prefer = []
    for i in range(rows):
        tmp = list(
            map(int, input().split(' ')))
        prefer.append(tmp)
    return prefer


def find_next_girl(Bprefer, boy):
    K = 1
    if boy["last_Req"] != -1:
        K = Bprefer[boy["key"]][boy["last_Req"]]+1

    if K > len(Bprefer):
        return -1
    for x in Bprefer[boy["key"]]:
        if x == K:
            return Bprefer[boy["key"]].index(x)


def get_stable_marriage(Bprefer, Gprefer, BNumber, GNumber):
    flag = True
    B = [{"key": x, "last_Req": -1, "isEngaged": False}
         for x in range(BNumber)]
    Gpartner = list(-1 for x in range(GNumber))
    while flag:
        flag = False
        for boy in B:
            if not boy["isEngaged"]:
                current_girl = find_next_girl(Bprefer, boy)
                if current_girl == -1:
                    continue
                boy["last_Req"] = current_girl
                if Gpartner[current_girl] == -1:
                    Gpartner[current_girl] = boy["key"]
                    boy["isEngaged"] = True
                else:
                    flag = True
                    if(Gprefer[current_girl][boy["key"]] < Gprefer[current_girl][Gpartner[current_girl]]):
                        rejected = Gpartner[current_girl]
                        Gpartner[current_girl] = boy["key"]
                        boy["isEngaged"] = True
                        B[rejected]["isEngaged"] = False

    return Gpartner


def print_matching(SM):
    for x in range(len(SM)):
        print(f'{x+1}<--------->{SM[x]+1}')


def print_graph(SM, BNumber, GNumber, code):
    edges = [(SM[x]+GNumber, x) for x in range(len(SM))]
    G = nx.DiGraph(edges)
    left_nodes = list(range(GNumber, BNumber+GNumber))
    right_nodes = list(range(0, GNumber))

    color_list = []
    label_list = {}
    for node in G:
        if node >= GNumber:
            label_list[node] = node-GNumber+1
            color_list.append("#1919ff" if code == 0 else "#ff0044")
        else:
            label_list[node] = node+1
            color_list.append("#ff0044" if code == 0 else "#1919ff")

    options = {
        "node_size": 3000,
        "node_color": color_list,
        "edgecolors": "black",
        "linewidths": 5,
        "width": 5,
    }
    pos = {n: (0, i) for i, n in enumerate(right_nodes)}
    pos.update({n: (2, i) for i, n in enumerate(left_nodes)})

    nx.draw_networkx(G, pos, **options, with_labels=False)
    nx.draw_networkx_labels(G, pos, label_list, font_size=36)

    ax = plt.gca()
    ax.margins(0.20)
    plt.axis("off")
    plt.title('Boy optimal' if code == 0 else 'Girl optimal')
    plt.show()


print("number of girls:")
GNumber = int(input())
print("number of boys:")
BNumber = int(input())

Bprefer = get_matrix(BNumber)
Gprefer = get_matrix(GNumber)

print("Boy optimal:")
BO = get_stable_marriage(Bprefer, Gprefer, BNumber, GNumber)
print_matching(BO)
print_graph(BO, BNumber, GNumber, 0)

print("Girl optimal:")
GO = get_stable_marriage(Gprefer, Bprefer, GNumber, BNumber)
print_matching(GO)
print_graph(GO, GNumber, BNumber, 1)
