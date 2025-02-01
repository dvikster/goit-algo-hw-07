# --- Двійкове дерево пошуку (BST) ВАРІАНТ ---
# --- код для BST взятий з уроку  ---

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key  

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

# Завдання 1: Функція пошуку максимального ключа в BST
def bst_find_max(root):
    if root is None:
        return None  # якщо дерево порожнє
    while root.right is not None:
        root = root.right
    return root.val

# Завдання 2: Функція пошуку мінімального ключа в BST
def bst_find_min(root):
    if root is None:
        return None  # якщо дерево порожнє
    while root.left is not None:
        root = root.left
    return root.val

# Завдання 3: Функція обчислення суми всіх ключів у BST
def bst_tree_sum(root):
    if root is None:
        return 0  # базовий випадок – порожнє дерево
    return root.val + bst_tree_sum(root.left) + bst_tree_sum(root.right)
  
# Приклад використання для BST:
if __name__ == '__main__':
    # Створення BST і вставка ключів
    keys = [20, 10, 30, 5, 15, 25, 35]
    bst_root = None
    for key in keys:
        bst_root = insert(bst_root, key)
    
    print("BST - Максимальний ключ:", bst_find_max(bst_root))  # Очікуємо 35
    print("BST - Мінімальний ключ:", bst_find_min(bst_root))    # Очікуємо 5
    print("BST - Сума всіх ключів:", bst_tree_sum(bst_root))     # Очікуємо 20+10+30+5+15+25+35 = 140



# --- AVL ВАРІАНТ ---
# --- код для AVL-дерева взятий з уроку---

class AVLNode:
    def __init__(self, key):
        self.key = key        # використовуємо атрибут 'key'
        self.height = 1       # Початкова висота вузла
        self.left = None      # Ліве піддерево
        self.right = None     # Праве піддерево

def get_height(node):
    if not node:
        return 0
    return node.height

def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)

def left_rotate(z):
    y = z.right
    T2 = y.left

    y.left = z
    z.right = T2

    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y

def right_rotate(y):
    x = y.left
    T3 = x.right

    x.right = y
    y.left = T3

    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))

    return x

def avl_insert(root, key):
    if not root:
        return AVLNode(key)

    if key < root.key:
        root.left = avl_insert(root.left, key)
    elif key > root.key:
        root.right = avl_insert(root.right, key)
    else:
        return root  # дублікати не допускаються

    root.height = 1 + max(get_height(root.left), get_height(root.right))
    balance = get_balance(root)

    # Балансування
    # Лівий Лівий випадок
    if balance > 1 and key < root.left.key:
        return right_rotate(root)
    # Лівий Правий випадок
    if balance > 1 and key > root.left.key:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    # Правий Правий випадок
    if balance < -1 and key > root.right.key:
        return left_rotate(root)
    # Правий Лівий випадок
    if balance < -1 and key < root.right.key:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root

# Завдання 1: Функція пошуку максимального ключа в AVL-дереві
def avl_find_max(root):
    if root is None:
        return None  # якщо дерево порожнє
    while root.right is not None:
        root = root.right
    return root.key

# Завдання 2: Функція пошуку мінімального ключа в AVL-дереві
def avl_find_min(root):
    if root is None:
        return None  # якщо дерево порожнє
    while root.left is not None:
        root = root.left
    return root.key
    
# Завдання 3: Функція обчислення суми всіх ключів у AVL-дереві
def avl_tree_sum(root):
    if root is None:
        return 0  # базовий випадок – порожнє дерево
    return root.key + avl_tree_sum(root.left) + avl_tree_sum(root.right)

# Приклад використання для AVL-дерева:
if __name__ == '__main__':
    # Створення AVL-дерева і вставка ключів
    keys = [20, 10, 30, 5, 15, 25, 35]
    avl_root = None
    for key in keys:
        avl_root = avl_insert(avl_root, key)
    
    print("AVL-дерево - Максимальний ключ:", avl_find_max(avl_root))  # Очікуємо 35
    print("AVL-дерево - Мінімальний ключ:", avl_find_min(avl_root))   # Очікуємо 5
    print("AVL-дерево - Сума всіх ключів:", avl_tree_sum(avl_root))   # Очікуємо 20+10+30+5+15+25+35 = 140
