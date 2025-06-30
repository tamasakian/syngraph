import networkx as nx
from collections import Counter

def build_graph_from_file(input_file: str) -> nx.Graph:
    """
    Construct a graph from non-typical synteny pair files.
    All genes contained in each row are interconnected.

    Args:
        input_file: Input file path containing synteny pairs.

    Returns:
        nx.Graph: Constructed graph where each node is a gene and edges represent synteny relationships.
    """
    G = nx.Graph()

    with open(input_file) as f:
        for line in f:
            tokens = line.strip().split()
            if len(tokens) < 3:
                continue

            genes = tokens[1:]

            for i, gene1 in enumerate(genes):
                for gene2 in genes[i + 1:]:
                    G.add_edge(gene1, gene2)

    return G

def build_graph_from_file_with_paralog_filter(input_file: str, max_paralog: int = 2) -> nx.Graph:
    """
    Construct a graph from non-typical synteny pair files with a filter for maximum paralogs.
    All genes contained in each row are interconnected.

    Args:
        input_file: Input file path containing synteny pairs.
        max_paralog: Maximum number of genes per species allowed in each row.

    Returns:
        nx.Graph: Constructed graph where each node is a gene and edges represent synteny relationships.
    """
    G = nx.Graph()

    with open(input_file) as f:
        for line in f:
            tokens = line.strip().split()
            if len(tokens) < 3:
                continue

            genes = tokens[1:]

            species_counts = Counter(extract_sp_name(g) for g in genes)
            if any(count > max_paralog for count in species_counts.values()):
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
        G: Input graph from which to extract connected components.

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
            out.write(f"MS{idx}\t" + "\t".join(sorted(group)) + "\n")


def extract_sp_name(gene: str) -> str:
    """
    Extract the species name from a gene identifier.
    Assumes the species name is the first part of the gene identifier.

    Args:
        gene: Gene identifier.

    Returns:
        str: Species name extracted from the gene identifier.
    """
    return "_".join(gene.split("_")[:2])