import networkx as nx
import tkinter as tk
from tkinter import ttk, messagebox
import tkinter as tk

ligne1 = nx.Graph()
ligne1.add_edges_from([("Valdoie Mairie", "Blumberg"), ("Blumberg", "Rubans"), ("Rubans", "Salbert"), ("Salbert", "1ere armée"), ("1ere armée", "Marché Vosges"),
                       ("Marché Vosges", "Roseraie"), ("Roseraie", "Colmar"), ("Colmar", "Strasbourg"), ("Strasbourg", "Jean Jaurès"), ("Jean Jaurès", "Clemenceau"),
                       ("Clemenceau", "République"), ("République", "Foch"), ("Foch", "Schwob"), ("Schwob", "Denfert Rochereau"), ("Denfert Rochereau", "Gare"), 
                       ("Gare", "Faubourg de Lyon"), ("Faubourg de Lyon", "Liberté Madrid"), ("Liberté Madrid", "Bruxelles"), ("Bruxelles", "Schuman"), ("Schuman", "Signoret"),
                       ("Signoret", "La Douce")])

ligne2a = nx.Graph()
ligne2a.add_edges_from([("Hauts de Belfort", "Camus"), ("Camus", "Bichat"), ("Bichat", "CFA"), ("CFA", "Laurencie"), ("Laurencie", "Cimetière Militaire"),
                        ("Cimetière Militaire", "Parant"), ("Parant", "Sellier"), ("Sellier", "Altkirch"), ("Altkirch", "Les Perches"), ("Les Perches", "Multiplexe"),
                        ("Multiplexe", "Colbert"), ("Colbert", "Sernam"), ("Sernam", "Gare"), ("Gare", "Faubourg de Lyon"), ("Faubourg de Lyon", "Liberté Madrid"),
                        ("Liberté Madrid", "Blum"), ("Blum", "Le Nôtre"), ("Le Nôtre", "Bonneff"), ("Bonneff", "Mozart"), ("Mozart", "Pont Canal"), ("Pont Canal", "Bavilliers"),
                        ("Bavilliers", "La Belle"), ("La Belle", "La Dame")])

ligne2b = nx.Graph()
ligne2b.add_edges_from([("Hauts de Belfort", "Camus"), ("Camus", "Bichat"), ("Bichat", "CFA"), ("CFA", "Laurencie"), ("Laurencie", "Cimetière Militaire"),
                        ("Cimetière Militaire", "Parant"), ("Parant", "Sellier"), ("Sellier", "Altkirch"), ("Altkirch", "Les Perches"), ("Les Perches", "Multiplexe"),
                        ("Multiplexe", "Colbert"), ("Colbert", "Sernam"), ("Sernam", "Gare"), ("Gare", "Faubourg de Lyon"), ("Faubourg de Lyon", "Liberté Madrid"),
                        ("Liberté Madrid", "Blum"), ("Blum", "Le Nôtre"), ("Le Nôtre", "Bonneff"), ("Bonneff", "Mozart"), ("Mozart", "Pont Canal"), ("Pont Canal", "Bavilliers"),
                        ("Bavilliers", "Rue du Buc"), ("Rue du Buc", "Route d'Urcerey"), ("Route d'Urcerey", "ZI de Bavilliers"), ("ZI de Bavilliers", "Argésians"), ("Argésians", "Acacias")])

ligne2c = nx.Graph()
ligne2c.add_edges_from([("Hauts de Belfort", "Camus"), ("Camus", "Bichat"), ("Bichat", "CFA"), ("CFA", "Laurencie"), ("Laurencie", "Cimetière Militaire"),
                        ("Cimetière Militaire", "Parant"), ("Parant", "Sellier"), ("Sellier", "Altkirch"), ("Altkirch", "Les Perches"), ("Les Perches", "Multiplexe"),
                        ("Multiplexe", "Colbert"), ("Colbert", "Sernam"), ("Sernam", "Gare"), ("Gare", "Denfert Rochereau"), ("Denfert Rochereau", "Schwob"), ("Schwob", "Foch"),
                        ("Foch", "République"), ("République", "Clemenceau"), ("Clemenceau", "Rabin"), ("Rabin", "Mieg"), ("Mieg", "Saget"), ("Saget", "Sainte Thérèse"),
                        ("Sainte Thérèse", "Grand'Combe"), ("Grand'Combe", "Laurent Thierry"), ("Laurent Thierry", "Alstom Etang"), ("Alstom Etang", "Techn'Hom Cravanche")])

ligne3a = nx.Graph()
ligne3a.add_edges_from([("Valdoie Mairie", "Blumberg"), ("Blumberg", "Méchelle"), ("Méchelle", "Benoit Frachon"), ("Benoit Frachon", "Techn’Hom 3"),
                        ("Techn’Hom 3", "Techn’Hom 2"), ("Techn’Hom 2", "IUT"), ("IUT", "Techn’Hom 1/UTBM"), ("Techn’Hom 1/UTBM", "Liberté Follereau"),
                        ("Liberté Follereau", "Faubourg de Lyon"), ("Faubourg de Lyon", "Gare"), ("Gare", "Sernam"), ("Sernam", "Colbert"), ("Colbert", "Multiplexe"),
                        ("Multiplexe", "Varonne"), ("Varonne", "Bosmont"), ("Bosmont", "Jacquot"), ("Jacquot", "Eluard"), ("Eluard", "Grottes"), ("Grottes", "Andelans Prés"),
                        ("Andelans Prés", "Port de Botans"), ("Port de Botans", "Œufs Frais"), ("Œufs Frais", "Route de Bermont"), ("Route de Bermont", "Conforama"),
                        ("Conforama", "Bascule"), ("Bascule", "Trévenans"), ("Trévenans", "Route de Vourvenans"), ("Route de Vourvenans", "Châtenois Forges"),
                        ("Châtenois Forges", "Châtenois"), ("Châtenois", "Complexe Sportif"), ("Complexe Sportif", "Géhant")])

ligne3b = nx.Graph()
ligne3b.add_edges_from([("Valdoie Mairie", "Blumberg"), ("Blumberg", "Méchelle"), ("Méchelle", "Benoit Frachon"), ("Benoit Frachon", "Techn’Hom 3"),
                        ("Techn’Hom 3", "Techn’Hom 2"), ("Techn’Hom 2", "IUT"), ("IUT", "Techn’Hom 1/UTBM"), ("Techn’Hom 1/UTBM", "Liberté Follereau"),
                        ("Liberté Follereau", "Faubourg de Lyon"), ("Faubourg de Lyon", "Gare"), ("Gare", "Sernam"), ("Sernam", "Colbert"), ("Colbert", "Multiplexe"),
                        ("Multiplexe", "Varonne"), ("Varonne", "Bosmont"), ("Bosmont", "Jacquot"), ("Jacquot", "Eluard"), ("Eluard", "Grottes"), ("Grottes", "Andelans Prés"),
                        ("Andelans Prés", "Port de Botans"), ("Port de Botans", "Œufs Frais"), ("Œufs Frais", "Sévenans UTBM"), ("Sévenans UTBM", "Hôpital NFC"),
                        ("Hôpital NFC", "Rue des Soies"), ("Rue des Soies", "Rue des Alisiers"), ("Rue des Alisiers", "Gare TGV"), ("Gare TGV", "1er R.A.")])

ligne4a = nx.Graph()
ligne4a.add_edges_from([("Champs Cerisiers", "Moulin"), ("Moulin", "Ballon"), ("Ballon", "Romaine"), ("Romaine", "Centre Commercial"),
                        ("Centre Commercial", "Briand"), ("Briand", "Courbet"), ("Courbet", "Parmentier"), ("Parmentier", "Paul Bert"),
                        ("Paul Bert", "Ferrette"), ("Ferrette", "Madagascar"), ("Madagascar", "Bohn"), ("Bohn", "Mulhouse"),
                        ("Mulhouse", "Donation Maurice Jardot"), ("Donation Maurice Jardot", "Rabin"), ("Rabin", "Strolz"),
                        ("Strolz", "4 As"), ("4 As", "Hatry"), ("Hatry", "Dubail"), ("Dubail", "Liberté Madrid"), ("Liberté Madrid", "Blum"),
                        ("Blum", "Le Nôtre"), ("Le Nôtre", "Molière"), ("Molière", "Renan"), ("Renan", "Poincaré"), ("Poincaré", "Chênois"),
                        ("Chênois", "Marcel Braun"), ("Marcel Braun", "Pierre Engel")])

ligne4b = nx.Graph()
ligne4b.add_edges_from([("Champs Cerisiers", "Moulin"), ("Moulin", "Ballon"), ("Ballon", "Romaine"), ("Romaine", "Centre Commercial"),
                        ("Centre Commercial", "Briand"), ("Briand", "Courbet"), ("Courbet", "Parmentier"), ("Parmentier", "Paul Bert"),
                        ("Paul Bert", "Ferrette"), ("Ferrette", "Madagascar"), ("Madagascar", "Bohn"), ("Bohn", "Mulhouse"),
                        ("Mulhouse", "Donation Maurice Jardot"), ("Donation Maurice Jardot", "Rabin"), ("Rabin", "Strolz"),
                        ("Strolz", "4 As"), ("4 As", "Hatry"), ("Hatry", "Dubail"), ("Dubail", "Liberté Madrid"), ("Liberté Madrid", "Blum"),
                        ("Blum", "Le Nôtre"), ("Le Nôtre", "Molière"), ("Molière", "Renan"), ("Renan", "Poincaré"), ("Poincaré", "Chênois"),
                        ("Chênois", "Marcel Braun"), ("Marcel Braun", "Pierre Engel"), ("Pierre Engel", "Saint Antonin"), ("Saint Antonin", "L’Assise"), ("L’Assise", "Berger")])

ligne5a = nx.Graph()
ligne5a.add_edges_from([("Prés d’Aumont", "Beurrerie"), ("Beurrerie", "Nallet"), ("Nallet", "Turenne"), ("Turenne", "Savoureuse"),
                        ("Savoureuse", "Paquis"), ("Paquis", "Pont Blanc"), ("Pont Blanc", "Marchegay"), ("Marchegay", "Martinet"),
                        ("Martinet", "Briand"), ("Briand", "Champ de Mars"), ("Champ de Mars", "Les Forges"), ("Les Forges", "Marseille"),
                        ("Marseille", "Clemenceau"), ("Clemenceau", "Rabin"), ("Rabin", "Strolz"), ("Strolz", "4 As"), ("4 As", "Hatry"),
                        ("Hatry", "Dubail"), ("Dubail", "Liberté Follereau"), ("Liberté Follereau", "Guidon"), ("Guidon", "Gardey"), ("Gardey", "Carrières"),
                        ("Carrières", "La Poste"), ("La Poste", "Essert"), ("Essert", "De Gaulle"), ("De Gaulle", "Chemin de la Ferme"),
                        ("Chemin de la Ferme", "Ballinamuck"), ("Ballinamuck", "Bois Joli")])

ligne5b = nx.Graph()
ligne5b.add_edges_from([("Chaume", "Verdoyeux"), ("Verdoyeux", "Eloie"), ("Eloie", "Route de Sermamagny"), ("Route de Sermamagny", "Rosemontoise"),
                        ("Rosemontoise", "Aubépines"), ("Aubépines", "Mermoz"), ("Mermoz", "Prés d’Aumont"), ("Prés d’Aumont", "Beurrerie"), ("Beurrerie", "Nallet"), ("Nallet", "Turenne"), ("Turenne", "Savoureuse"),
                        ("Savoureuse", "Paquis"), ("Paquis", "Pont Blanc"), ("Pont Blanc", "Marchegay"), ("Marchegay", "Martinet"),
                        ("Martinet", "Briand"), ("Briand", "Champ de Mars"), ("Champ de Mars", "Les Forges"), ("Les Forges", "Marseille"),
                        ("Marseille", "Clemenceau"), ("Clemenceau", "Rabin"), ("Rabin", "Strolz"), ("Strolz", "4 As"), ("4 As", "Hatry"),
                        ("Hatry", "Dubail"), ("Dubail", "Liberté Follereau"), ("Liberté Follereau", "Guidon"), ("Guidon", "Gardey"), ("Gardey", "Carrières"),
                        ("Carrières", "La Poste"), ("La Poste", "Essert"), ("Essert", "De Gaulle"), ("De Gaulle", "Chemin de la Ferme"),
                        ("Chemin de la Ferme", "Ballinamuck"), ("Ballinamuck", "Bois Joli")])


ligne8 = nx.Graph()
ligne8.add_edges_from([("Liberté", "Maison de Santé"), ("Maison de Santé", "Terrasses"), ("Terrasses", "Pins"),
                       ("Pins", "Carrières"), ("Carrières", "La Poste"), ("La Poste", "Essert"), ("Essert", "De Gaulle"),
                       ("De Gaulle", "Chemin de la Ferme"), ("Chemin de la Ferme", "Ballinamuck"), ("Ballinamuck", "Frézard"),
                       ("Frézard", "Bas du Village"), ("Bas du Village", "La Forêt")])

ligne9 = nx.Graph()
ligne9.add_edges_from([("République", "Université"), ("Université", "Lieutenant Martin"), ("Lieutenant Martin", "Schmittlein"), ("Schmittlein", "Philippe Grille"),
                       ("Philippe Grille", "As de Trèfle"), ("As de Trèfle", "Picard"), ("Picard", "Deshaie"), ("Deshaie", "Haute Miotte"), ("Haute Miotte", "Clinique"),
                        ("Clinique", "Atria"), ("Atria", "République")])


bice_network = nx.Graph()

# Liste des lignes avec couleurs
line_data = [
    ('ligne1', ligne1, 'red'),
    ('ligne2a', ligne2a, 'orange'),
    ('ligne2b', ligne2b, 'orange'),
    ('ligne2c', ligne2c, 'orange'),
    ('ligne3a', ligne3a, 'blue'),
    ('ligne3b', ligne3b, 'blue'),
    ('ligne4a', ligne4a, 'purple'),
    ('ligne4b', ligne4b, 'purple'),
    ('ligne5a', ligne5a, 'yellow'),
    ('ligne5b', ligne5b, 'yellow'),
    ('ligne8', ligne8, 'brown'),
    ('ligne9', ligne9, 'pink')
]

# Ajouter les arêtes avec attributs de ligne et couleur
for line_name, graph, color in line_data:
    for u, v in graph.edges():
        bice_network.add_edge(u, v, line=line_name, color=color)

# Get all unique bus stops
all_stops = sorted(list(bice_network.nodes()))

def find_best_trajectory(start_stop, end_stop):
    """
    Find the best trajectory between two bus stops using Dijkstra's algorithm.
    Returns the list of stops in the shortest path.
    """
    try:
        path = nx.shortest_path(bice_network, source=start_stop, target=end_stop, method='dijkstra')
        return path
    except nx.NetworkXNoPath:
        return None
    except nx.NodeNotFound as e:
        return f"Stop not found: {e}"
    


def calculate_path():
    start = start_var.get()
    end = end_var.get()
    if start == end:
        messagebox.showerror("Error", "Start and end stops must be different.")
        return
    trajectory = find_best_trajectory(start, end)
    if trajectory:
        result_text.set(f"Best trajectory from {start} to {end}:\n{' -> '.join(trajectory)}")
    else:
        result_text.set("No path found between the selected stops.")

# Create GUI
root = tk.Tk()
root.title("Bus Trajectory Calculator of Optymo Bice Network")

tk.Label(root, text="Starting Bus Stop:").grid(row=0, column=0, padx=10, pady=10)
start_var = tk.StringVar()
start_combo = ttk.Combobox(root, textvariable=start_var, values=all_stops, state="readonly")
start_combo.grid(row=0, column=1, padx=10, pady=10)
start_combo.current(0)  # Set default to first stop

tk.Label(root, text="Ending Bus Stop:").grid(row=1, column=0, padx=10, pady=10)
end_var = tk.StringVar()
end_combo = ttk.Combobox(root, textvariable=end_var, values=all_stops, state="readonly")
end_combo.grid(row=1, column=1, padx=10, pady=10)
end_combo.current(1)  # Set default to second stop

calculate_button = tk.Button(root, text="Calculate Trajectory", command=calculate_path)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, justify="left", wraplength=400)
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

tk.mainloop()


