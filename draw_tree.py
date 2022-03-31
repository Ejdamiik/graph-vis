from typing import Optional, List, Tuple, Callable
import tkinter as tk

# --- values to be determined
Node = str
Node_value = int
Tree = str

# --- Terminal-based binary tree print
def number_split(n: int) -> List[int]:
    
    res = [] if n % 2 == 0 else [0]
    for i in range(1, n // 2 + 1):

        res.append(i)
        res.append(-i)

    return sorted(res)



def print_tree(tree: Tree) -> None:
    """
    Text-representation
    """
    width = get_width(tree) * 5
    height = get_height(tree)
    levels = [" " * width for _ in range(height)]

    _print_levels(tree, width // 2, width // 2, levels, 0)
    return "\n".join(levels)


def _print_levels(tree: Tree,
         width: int,
         x: int,
         levels: List[str],
         i: int) -> None:
    
    if not tree:
        return

    levels[i] = place_in_string(levels[i], x, tree.data)
    _print_levels(tree.left, width // 2, x - width // 2, levels, i + 1)
    _print_levels(tree.right, width // 2, x + width // 2, levels, i + 1)


def place_in_string(string: str, pos: int, val: Node_value) -> str:

    return string[:pos] + str(val) + string[pos + 1:]

# ---



# --- Tkinter tree visualization
def draw_tree(tree: Tree,
              value_getter: Callable[[Node], Node_value],
              binary: bool = False,
              redblack: bool = False) -> None:
    """
    Function to draw binary tree graphicaly

    tree = tree structure to be visualized
    value_getter = function to get value to print
    binary = bool deciding whether tree is binary
    redblack = bool deciding whether tree is RBtree
    """

    CANVAS_WIDTH = 400
    CANVAS_HEIGHT = 400

    canvas = tk.Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    canvas.pack()
    _draw(tree.root, CANVAS_WIDTH // 2, CANVAS_WIDTH // 2, \
          40, canvas, None, value_getter, binary, redblack)

    canvas.mainloop()


def _draw(node: Node,
         width: int,
         x: int,
         y: int,
         canvas: tk.Canvas,
         parent_xy: Optional[Tuple[int, int]],
         value_getter: Callable[[Node], Node_value],
         binary: bool,
         redblack: bool) -> None:

    if not node:
        return

    if redblack:
        fill = node.color
    else:
        fill = "black"

    canvas.create_text(x, y, text = value_getter(node), fill = fill)

    if parent_xy:
        canvas.create_line((x, y - 10), (parent_xy[0], parent_xy[1] + 10))

    if binary:
        _draw(node.left, width // 2, x - width // 2, y + 40, canvas, (x, y), value_getter, binary, redblack)
        _draw(node.right, width // 2, x + width // 2, y + 40, canvas, (x, y), value_getter, binary, redblack)

    else:
        for i, child in zip(number_split(len(node.children)), node.children):
            _draw(child, width // len(node.children), x + i * (width // len(node.children)),
                  y + 40, canvas, (x, y), value_getter, binary, redblack)

