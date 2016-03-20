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

# Преобразуем G в словарь словарей
G_dict = nx.to_dict_of_dicts(G)


# Преобразование в список смежности
def adj(G, Adj = {}):
    for key in G:
        if key not in Adj:
            Adj[key] = G[key]
        else:
            Adj[key] = {G[key]}
    return Adj

G_adj = adj(G_dict)
print(G_adj)
