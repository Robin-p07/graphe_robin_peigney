import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

# --- 1. DÉFINITION DES GÉNÉRATIONS ---
generations = {
    -1: ["George VI", "Elizabeth Bowes-Lyon", "Prince Andrew", "Alice of Battenberg"],
    0: ["Philip", "Elizabeth II"],
    1: ["Diana", "King Charles III", "Camilla"],
    2: ["Kate", "Prince William", "Prince Harry", "Meghan"],
    3: ["Prince George", "Princess Charlotte", "Prince Louis", "Archie", "Lilibet"]
}

for layer, names in generations.items():
    for name in names:
        G.add_node(name, subset=layer)

# --- 2. DÉFINITION DES RELATIONS ---
parent_relations = [
    # Parents d'Elizabeth II et Philip
    ("George VI", "Elizabeth II"),
    ("Prince Andrew", "Philip"),

    # Enfants d'Elizabeth et Philip
    ("Elizabeth II", "King Charles III"),
    
    # Enfants de Charles
    ("King Charles III", "Prince William"),
    ("King Charles III", "Prince Harry"),
    
    # Enfants de William
    ("Prince William", "Prince George"),
    ("Prince William", "Princess Charlotte"),
    ("Prince William", "Prince Louis"),
    
    # Enfants de Harry
    ("Prince Harry", "Archie"),
    ("Prince Harry", "Lilibet"),
]

mariage_relations = [
    ("George VI", "Elizabeth Bowes-Lyon"),
    ("Prince Andrew", "Alice of Battenberg"),
    ("Philip", "Elizabeth II"),
    ("Diana", "King Charles III"),
    ("Kate", "Prince William"),
    ("Prince Harry", "Meghan")
]

divorces_relations = [("King Charles III", "Camilla")]

G.add_edges_from(parent_relations)
G.add_edges_from(mariage_relations)
G.add_edges_from(divorces_relations)

# --- 3. CONFIGURATION DU DESSIN ---
plt.figure(figsize=(16, 12)) 

manual_pos = {

    # --- GÉNÉRATION -1 ---
    "George VI":            (0, 1), 
    "Elizabeth Bowes-Lyon": (-1.5, 1),
    
    "Prince Andrew":   (1.5, 1),
    "Alice of Battenberg":  (3.0, 1),

    # --- GÉNÉRATION 0 ---
    "Elizabeth II": (0, 0),
    "Philip":       (1.5, 0),

    # --- GÉNÉRATION 1 ---
    "Diana":            (-2, -1),
    "King Charles III": (0, -1),   
    "Camilla":          (2, -1),

    # --- GÉNÉRATION 2 ---
    "Kate":             (-4.5, -2),
    "Prince William":   (-3, -2),  
    "Prince Harry":     (3, -2),   
    "Meghan":           (4.5, -2),

    # --- GÉNÉRATION 3 ---
    "Prince George":      (-4, -3),
    "Princess Charlotte": (-3, -3), 
    "Prince Louis":       (-2, -3),
    "Archie":             (2, -3),
    "Lilibet":            (4, -3)
}

# --- 4. COULEURS ---
rois_et_heritiers = ["George VI", "Elizabeth II", "King Charles III", "Prince William"]

femmes = [
    "Elizabeth Bowes-Lyon", "Alice of Battenberg","Diana", "Camilla", "Kate", "Meghan", "Princess Charlotte", "Lilibet"
]

node_colors = []
for node in G.nodes():
    if node in rois_et_heritiers:
        node_colors.append("gold")    
    elif node in femmes:
        node_colors.append("#ffb6c1") 
    else:
        node_colors.append("lightblue") 

# --- 5. DESSIN FINAL ---

nx.draw_networkx_nodes(G, manual_pos, node_size=3000, node_color=node_colors, edgecolors="gray")
nx.draw_networkx_labels(G, manual_pos, font_size=7, font_weight="bold")

nx.draw_networkx_edges(
    G, manual_pos, 
    edgelist=parent_relations, 
    edge_color="gray", 
    arrows=True, 
    arrowstyle="-|>", 
    arrowsize=15, 
    width=1.5
)

nx.draw_networkx_edges(
    G, manual_pos, 
    edgelist=mariage_relations, 
    edge_color="red", 
    arrows=False, 
    width=2
)

nx.draw_networkx_edges(
    G, manual_pos, 
    edgelist=divorces_relations, 
    edge_color="red", 
    style="dashed", 
    arrows=False, 
    width=2
)

plt.title("Arbre Généalogique Royal", fontsize=16)
plt.margins(0.1)
plt.axis("off")

plt.savefig("famille_royale.png", dpi=300)
plt.show()