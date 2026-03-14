
class Plane:
    def __init__(self,cells):
        """Initialize a plain"""
        self._cells=set(cells)
        self._hits=set()

    @property
    def cells(self):
        """a set of all cells occupied by this plane"""
        return self._cells

    def hit(self,pos):
        """
        Register a shot at a given position
        """
        if pos in self._cells:
            self._hits.add(pos)
            return True
        return False

    def is_destroyed(self):
        """ Check if the plane has been completely destroyed"""
        return self._hits==self._cells
