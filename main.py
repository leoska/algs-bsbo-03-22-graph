from graph import Graph
from dfs import dfs, dfs_transpose


VERTEXES_NAMES = {"A", "B", "C", "D", "E", "F", "G", "H"}
GRAPH_EDGES: list[dict[str, str]] = [
    {"src": "A", "dst": "B"},  # A -> B
    {"src": "B", "dst": "E"},  # B -> E
    {"src": "B", "dst": "F"},  # B -> F
    {"src": "B", "dst": "C"},  # B -> C
    {"src": "C", "dst": "G"},  # C -> G
    {"src": "C", "dst": "D"},  # C -> D
    {"src": "D", "dst": "C"},  # D -> C
    {"src": "D", "dst": "H"},  # D -> H
    {"src": "E", "dst": "A"},  # E -> A
    {"src": "E", "dst": "F"},  # E -> F
    {"src": "F", "dst": "G"},  # F -> G
    {"src": "G", "dst": "F"},  # G -> F
    {"src": "H", "dst": "G"},  # H -> G
    {"src": "H", "dst": "D"},  # H -> D
]


def _init_graph() -> Graph:
    result = Graph()

    for vertex in VERTEXES_NAMES:
        result.add_v(vertex)

    for params in GRAPH_EDGES:
        result.add_e(**params)

    return result


def _init_used() -> dict[str, bool]:
    result = {}
    for vertex in VERTEXES_NAMES:
        result[vertex] = False
    return result


if __name__ == '__main__':
    graph = _init_graph()

    order: list[str] = []
    used = _init_used()

    for vertex in VERTEXES_NAMES:
        dfs(v=vertex, order=order, used=used, g=graph)

    graph_t = graph.get_transpose()
    used = _init_used()
    component: list[str] = []

    order.reverse()
    for vertex in order:
        if not used[vertex]:
            dfs_transpose(v=vertex, component=component, used=used, g_t=graph_t)

            print(", ".join(component))
            component.clear()
