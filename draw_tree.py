from typing import Optional, List, Tuple
import tkinter as tk

Value = int

class BinaryTree:

    def __init__(self, data: Value) -> None:

        self.data = data

        self.left:["BinaryTree"] = None
        self.right:["BinaryTree"] = None

class Tree:

    def __init__(self, data: Value) -> None:

        self.data = data
        self.children = []





def number_split(n: int) -> List[int]:
    
    res = [] if n % 2 == 0 else [0]
    for i in range(1, n // 2 + 1):

        res.append(i)
        res.append(-i)

    return sorted(res)



def print_tree(tree: BinaryTree) -> None:
    """
    Text-representation
    """
    width = get_width(tree) * 5
    height = get_height(tree)
    levels = [" " * width for _ in range(height)]

    _print_levels(tree, width // 2, width // 2, levels, 0)
    return "\n".join(levels)


def _print_levels(tree: Optional[BinaryTree],
         width: int,
         x: int,
         levels,
         i) -> None:
    
    if not tree:
        return

    levels[i] = place_in_string(levels[i], x, tree.data)
    _print_levels(tree.left, width // 2, x - width // 2, levels, i + 1)
    _print_levels(tree.right, width // 2, x + width // 2, levels, i + 1)


def place_in_string(string: str, pos: int, val: Value) -> str:

    return string[:pos] + str(val) + string[pos + 1:]



def draw_tree(tree: BinaryTree, binary: bool = False) -> None:
    """
    Function to draw binary tree graphicaly
    """
    CANVAS_WIDTH = 400
    CANVAS_HEIGHT = 400

    canvas = tk.Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    canvas.pack()
    _draw(tree, CANVAS_WIDTH // 2, CANVAS_WIDTH // 2, 40, canvas, None, binary)
    canvas.mainloop()


def _draw(tree: Optional[BinaryTree],
         width: int,
         x: int,
         y: int,
         canvas: tk.Canvas,
         parent_xy: Optional[Tuple[int, int]],
         binary: bool) -> None:

    if not tree:
        return

    canvas.create_text(x, y, text = tree.data)

    if parent_xy:
        canvas.create_line((x, y - 10), (parent_xy[0], parent_xy[1] + 10))

    if binary:
        _draw(tree.left, width // 2, x - width // 2, y + 40, canvas, (x, y), binary)
        _draw(tree.right, width // 2, x + width // 2, y + 40, canvas, (x, y), binary)

    else:
        for i, child in zip(number_split(len(tree.children)), tree.children):
            _draw(child, width // len(tree.children), x + i * (width // len(tree.children)), y + 40, canvas, (x, y), binary)


t1 = Tree(5)

for i in range(5):
    t1.children.append(Tree(i))

draw_tree(t1)
