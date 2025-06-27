from syngraph import utils

def mso(input_file:str, output_file:str):
    """
    MSO (Multi Syntenic Orthologs) function

    Args:
        input_file (str): Input file path containing synteny pairs.
        output_file (str): Output file path for connected components.
    """
    G = utils.build_graph_from_file(input_file)
    components = utils.extract_connected_components(G)
    utils.output_connected_components(components, output_file)

