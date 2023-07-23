from typing import Final


class ClsB:
    attr_b: Final[int]

    def __init__(self, attr_b):
        self.attr_b = attr_b


obj_b = ClsB(0)
obj_b.attr_b = 1
print(obj_b.attr_b)
