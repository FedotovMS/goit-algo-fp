import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def heapify(nodes, index, heap_type='min'):
    """Функція для підтримки властивостей купи"""
    left = 2 * index + 1
    right = 2 * index + 2
    smallest_or_largest = index

    if left < len(nodes):
        if (heap_type == 'min' and nodes[left].val < nodes[smallest_or_largest].val) or \
                (heap_type == 'max' and nodes[left].val > nodes[smallest_or_largest].val):
            smallest_or_largest = left

    if right < len(nodes):
        if (heap_type == 'min' and nodes[right].val < nodes[smallest_or_largest].val) or \
                (heap_type == 'max' and nodes[right].val > nodes[smallest_or_largest].val):
            smallest_or_largest = right

    if smallest_or_largest != index:
        nodes[index], nodes[smallest_or_largest] = nodes[smallest_or_largest], nodes[index]
        heapify(nodes, smallest_or_largest, heap_type)


def build_heap(elements, heap_type='min'):
    """Створення бінарної купи з елементів"""
    nodes = [Node(val) for val in elements]
    for i in range(len(nodes) // 2 - 1, -1, -1):
        heapify(nodes, i, heap_type)

    # Повернення кореня купи
    return nodes[0], nodes


def create_heap_tree(heap_nodes):
    """Створення дерева для візуалізації з бінарної купи"""
    root = heap_nodes[0]
    queue = [root]
    for i in range(1, len(heap_nodes)):
        current = queue.pop(0)
        new_node = heap_nodes[i]
        if current.left is None:
            current.left = new_node
        else:
            current.right = new_node
        queue.append(new_node)
    
    return root


# Приклад створення бінарної купи:
elements = [10, 20, 30, 40, 50, 60, 70]
heap_type = 'min'

# Створення купи
root, heap_nodes = build_heap(elements, heap_type)

# Створення дерева з елементів купи для візуалізації
heap_tree_root = create_heap_tree(heap_nodes)

# Відображення дерева купи
draw_tree(heap_tree_root)