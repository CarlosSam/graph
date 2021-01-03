from node import Node

def loadGraphRecursive(node, info):
    node_info = next(filter(lambda current_node_info: current_node_info['id'] == node.name, info['nodes']))
    for child_name in node_info['children']:
        child_node = node.addChild(child_name)
        loadGraphRecursive(child_node, info)
    return node

def loadGraph(info):
    root = Node(info['startNode'])
    loadGraphRecursive(root, info)
    return root

