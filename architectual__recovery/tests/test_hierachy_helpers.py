from archrcover.hierarchy import change_level, get_node_level

def test_get_node_level():

    node = 'node.value'

    assert get_node_level(node) == 1

def test_change_level_regular():

    node = 'node.value'

    assert change_level(node, level = 1) == 'node'

def test_change_level_given_level_deeper_than_node():
    
    node = 'node.value'

    assert change_level(node, level = 3) == 'node.value'