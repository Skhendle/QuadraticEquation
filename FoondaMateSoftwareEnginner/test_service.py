from service import plot_graphs


def test_invalid_graph_order():
    assert plot_graphs(graph_type="line", graph_order="First") == "Invalid GRAPH_ORDER Arguement"


def test_invalid_graph_type():
    assert plot_graphs(graph_type="pie", graph_order="start") == "Invalid GRAPH_TYPE Arguement"

if __name__ == "__main__":
    test_invalid_graph_order()
    test_invalid_graph_type()
    print("Everything passed")