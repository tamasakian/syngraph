from syngraph import utils

def mso(input_file:str, output_file:str) -> None:
    """
    MSO (Multi Syntenic Orthologs) function

    Args:
        input_file (str): Input file path containing synteny pairs.
        output_file (str): Output file path for connected components.
    """
    G = utils.build_graph_from_file(input_file)
    components = utils.extract_connected_components(G)
    utils.output_connected_components(components, output_file)

def mso_p(input_file:str, output_file:str, max_paralog: int = 2) -> None:
    """
    MSO (Multi Syntenic Orthologs) function with paralog filtering.

    Args:
        input_file: Input file path containing synteny pairs.
        output_file: Output file path for connected components.
        max_paralog: Maximum allowed number of paralogs per species in a synteny block.
    """
    G = utils.build_graph_from_file_with_paralog_filter(input_file, max_paralog=2)
    components = utils.extract_connected_components(G)
    utils.output_connected_components(components, output_file)

