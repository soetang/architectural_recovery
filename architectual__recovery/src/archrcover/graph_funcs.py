import re 
import warnings
import pandas as pd
import networkx as nx
from archrcover.hierarchy import change_level


def aggregate_edges(G, level, exclude_relations_to_self = True):
    edges = [
        {
            'outgoing' : change_level(outgoing, level), 
            'ingoing' : change_level(ingoing, level)
        }
        for outgoing, ingoing
        in G.edges(data=False)
    ]

    # add matching edges together an create a weight
    df = pd.DataFrame(edges).groupby(['outgoing', 'ingoing']).size().to_frame('weight')
    df = df.reset_index()

    if exclude_relations_to_self:
        df = df[df['outgoing'] != df['ingoing']]

    return list(df.itertuples(index=False, name=None))

def remove_nodes(g, filter:list[str]):

    if isinstance(filter, str):
        warnings.warn('You entered filter as a string, please consider if this is what you wanted to do?')
        filter = list([filter])

    regex = "|".join(filter)
    nodes = g.nodes(data=False)

    matching_nodes = [x for x in nodes if re.search(regex, x) is not None]

    g.remove_nodes_from(matching_nodes)

    return g

def rename_nodes(G, pattern, replacement, regex = False):
    
    nodes = list(G.nodes())
    # pandas since the vectorized functions are generally faster
    nodes = pd.Series(nodes)
    new_names = nodes.str.replace(pattern, replacement, regex=regex)
    look_up = dict(zip(nodes, new_names))

    G = nx.relabel_nodes(G, look_up)

    return G
