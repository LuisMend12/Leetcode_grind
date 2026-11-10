"""
example facts:
 m = 3.28 ft
 ft = 12 in
 hr = 60 min
example queries:
 2 m = ? in  --> answer = 78.72
 13 in = ? m  --> answer = 0.3302 (roughly)
 13 in = ? hr --> "not convertible"

"""

# dictionary that maps strings (units) to some class that representsa a node in a graph
# nodes store: edges (float, node)

class Edge:
    def __init__(self, multiplier, node):
        self.multiplier = multiplier
        self.node = node

class Node:
    def __init__(self, unit):
        self.unit = unit

    def add_edge(self, multiplier, other_unit):
        self.multiplier = multiplier
        self.other_unit = other_unit

def parse_facts(facts):
    name_to_node = {}
    for (left_unit, multiplier, right_unit) in facts:
        if left_unit not in name_to_node:
            left_node = Node(left_unit)
            name_to_node[left_unit] = left_node
        if right_unit not in name_to_node:
            right_node = Node(right_unit)
            name_to_node[right_unit] = right_node
        name_to_node[left_node].add_edge(multiplier, right_unit)
    return name_to_node

def answer_query(query, facts):
    starting_amount, from_unit, to_unit = query
    # Given node, we want to enqueue (current_amount, unit_to_check)
    