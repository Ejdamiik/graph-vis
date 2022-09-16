from typing import Optional, List, Tuple, Callable, Any
import tkinter as tk

# --- values to be determined
Node = Any
Node_value = Any
Tree = Any

def number_split(n: int) -> List[int]:
    
    res = [] if n % 2 == 0 else [0]
    for i in range(1, n // 2 + 1):

        res.append(i)
        res.append(-i)

    return sorted(res)



# --- Tkinter tree visualization
def draw_tree(tree: Tree,
              value_getter: Callable[[Node], Node_value],
              binary: bool = False,
              redblack: bool = False) -> None:
    """
    Function to draw tree graphicaly

    tree = tree structure to be visualized
    value_getter = function to get value to print
    binary = bool deciding whether tree is binary
    redblack = bool deciding whether tree is RBtree
    """

    CANVAS_WIDTH = 400
    CANVAS_HEIGHT = 400

    canvas = tk.Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    canvas.pack()
    _draw(tree.root_node, CANVAS_WIDTH // 2, CANVAS_WIDTH // 2, \
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
        canvas.create_line(x, y - 10, parent_xy[0], parent_xy[1] + 10)

    if binary:
        _draw(node.left, width // 2, x - width // 2, y + 40, canvas, (x, y), value_getter, binary, redblack)
        _draw(node.right, width // 2, x + width // 2, y + 40, canvas, (x, y), value_getter, binary, redblack)

    else:
        for i, child in zip(number_split(len(node.children)), node.children):
            _draw(child, width // len(node.children), x + i * (width // len(node.children)),
                  y + 40, canvas, (x, y), value_getter, binary, redblack)

