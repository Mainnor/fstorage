import os.path
import uuid
from pandas import read_excel
from math import ceil
import functools


@functools.total_ordering
class Item(object):

    def __init__(self, name, height, width, depth, mass):
        self.name = name
        self.height = ceil(int(height) / 1000)
        self.width = ceil(int(width) / 1000)
        self.depth = ceil(int(depth) / 1000)
        self.mass = mass
        self.uuid = uuid.uuid4().hex

        self.original_height = height
        self.original_width = width
        self.original_depth = depth

    def __eq__(self, other) -> bool:
        if isinstance(other, Item):
            return self.mass == other.mass

        return NotImplemented

    def __ne__(self, other) -> bool:
        if isinstance(other, Item):
            return self.mass != other.mass

        return NotImplemented

    def __lt__(self, other) -> bool:
        if isinstance(other, Item):
            return self.mass < other.mass

        return NotImplemented

    def __le__(self, other) -> bool:
        if isinstance(other, Item):
            return self.mass <= other.mass

        return NotImplemented

    def __gt__(self, other) -> bool:
        if isinstance(other, Item):
            return self.mass > other.mass

        return NotImplemented

    def __ge__(self, other) -> bool:
        if isinstance(other, Item):
            return self.mass >= other.mass

        return NotImplemented


class WayBill:
    def __init__(self, fileway: str):
        if os.path.exists(fileway):
            self.fileway = fileway
        else:
            raise FileNotFoundError

    def create_item_list(self):
        items = []
        data = read_excel(self.fileway).values.tolist()

        for raw in data:
            _size = raw[2].split("*")
            items.append(Item(
                name=raw[1],
                height=_size[0],
                width=_size[1],
                depth=_size[2],
                mass=raw[-1]
            ))
        return sorted(items)

    def set_fileway(self, new_fileway):
        self.__init__(fileway=new_fileway)