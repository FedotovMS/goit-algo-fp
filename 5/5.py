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


def generate_color(step, max_steps):
    """Генерація кольору в форматі 16-системи RGB, що змінюється від темного до світлого"""
    ratio = step / max_steps
    r = int(255 * ratio)
    g = int(150 + 100 * ratio)
    b = int(240 * (1 - ratio))
    return f"#{r:02X}{g:02X}{b:02X}"


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def dfs_traversal(root):
    """Обхід дерева в глибину (DFS) з використанням стеку"""
    stack = [root]
    visited = []
    max_steps = 0
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            max_steps += 1
            # Генерація кольору для поточного кроку
            node.color = generate_color(max_steps, len(visited) + len(stack))
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    return visited


def bfs_traversal(root):
    """Обхід дерева в ширину (BFS) з використанням черги"""
    queue = [root]
    visited = []
    max_steps = 0
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            max_steps += 1
            # Генерація кольору для поточного кроку
            node.color = generate_color(max_steps, len(visited) + len(queue))
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return visited


# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Відображення дерева до обходу
draw_tree(root)

# Виконання DFS обходу та візуалізація
dfs_traversal(root)
draw_tree(root)

# Виконання BFS обходу та візуалізація
bfs_traversal(root)
draw_tree(root)