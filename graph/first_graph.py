import networkx as nx
import matplotlib.pyplot as plt

# Открываем файл со списком ребер
file = open('graph.txt', 'r')

# Создаем заготовку под граф
G = nx.Graph()

# Производим считывание ребер из файла
for line in file.readlines():
    a, b, weight = line.split()
    a, b, weight = str(a), str(b), int(weight)
    G.add_edge(a, b, weight = weight)

# закрываем файл
file.close()

# Сортируем ребра по длине
elarge = [(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] > 5]
esmall = [(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] <= 5]


pos = nx.spring_layout(G)

nx.draw_networkx_nodes(G, pos, node_size=300)                            # Рисуем вершины
nx.draw_networkx_edges(G,pos,edgelist=elarge, width=3)                   # Рисуем ребра
nx.draw_networkx_edges(G,pos,edgelist=esmall, width=3, alpha=0.5, edge_color='b', style='dashed')
nx.draw_networkx_labels(G, pos, font_size=16, font_family='sans-serif')  # Рисуем метки

plt.axis('off')
plt.savefig("labels_and_colors.png")
plt.show()
