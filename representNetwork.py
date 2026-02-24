
import graphviz as gv
from bus import *

# Utiliser graphviz pour un meilleur layout avec moins de croisements
dot = gv.Graph(engine='dot')  # 'dot' minimise les croisements
for node in bice_network.nodes():
    dot.node(str(node))
for edge in bice_network.edges(data=True):
    color = edge[2]['color']
    dot.edge(str(edge[0]), str(edge[1]), color=color)

# Sauvegarder en PNG
dot.render('bice_network', format='png', cleanup=True)
