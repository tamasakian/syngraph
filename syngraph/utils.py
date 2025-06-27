import networkx as nx

def build_graph_from_file(input_file: str) -> nx.Graph:
    """
    Construct a graph from non-typical synteny pair files.
    All genes contained in each row are interconnected.

    Args:
        input_file (str): Input file path containing synteny pairs.

    Returns:
        nx.Graph: Constructed graph where each node is a gene and edges represent synteny relationships.
    """
    G = nx.Graph()

    with open(input_file) as f:
        for line in f:
            genes = line.strip().split()
            if len(genes) < 2:
                continue

            for i, gene1 in enumerate(genes):
                for gene2 in genes[i + 1:]:
                    G.add_edge(gene1, gene2)

    return G


def extract_connected_components(G: nx.Graph) -> list:
    """
    Extract connected components from the graph.
    Each connected component is returned as a set.

    Args:
        G (nx.Graph): Input graph from which to extract connected components.

    Returns:
        list: List of sets, where each set contains the genes in a connected component.
    """
    return list(nx.connected_components(G))

def output_connected_components(components: list, output_file: str):
    """Output connected components to a file.
    Args:
        components (list): List of sets containing connected components.
        output_file (str): Path to the output file.
    """
    with open(output_file, "w") as out:
        for idx, group in enumerate(components, 1):
            out.write(f"Group{idx}\t" + "\t".join(sorted(group)) + "\n")

