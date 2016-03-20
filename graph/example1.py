import matplotlib.pyplot as plt
import networkx as nx

G=nx.path_graph(8)
nx.draw(G)
plt.savefig("simple_path.png") # save as png
plt.show() # display