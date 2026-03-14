from src.domain.exceptions import InvalidMoveError

class Board:
    def __init__(self,size=10):
        """Initialize an empty board"""
        self._size=size
        self._planes=[]
        self._shots=set()

    @property
    def size(self):
        """The size of the board"""
        return self._size

    def in_bounds(self,pos):
        """Check whether a coordinate is inside the board or not"""
        row,col=pos
        return 0<=row<self._size and 0<=col<self._size

    def add_plane(self,plane):
        """Add a plane to the board. Check if plane is valid and if it is it adds it to the board"""
        for cell in plane.cells:
            if not self.in_bounds(cell):
                raise InvalidMoveError("Plane it is outside the board")

            for existing in self._planes:
                if cell in existing.cells:
                    raise InvalidMoveError("Planes cannot overlap")

        self._planes.append(plane)

    def fire(self,pos):
        """
        Process a shot fired at the board
        """
        if not self.in_bounds(pos):
            raise InvalidMoveError("Shot outside the board")

        if pos in self._shots:
            raise InvalidMoveError("You already shot here")

        self._shots.add(pos)
        for plane in self._planes:
            if plane.hit(pos):
                if plane.is_destroyed():
                    return "destroyed"
                return "hit"
        return "miss"

    def all_planes_destroyed(self):
        """Check if all planes on this board are destroyed"""
        return all(p.is_destroyed() for p in self._planes)

    def get_visible_grid(self, show_planes=False):
        """Build a representation for printing
        Symbols:
        ' ' -> empty
        P -> player's plane cell
        H -> hit
        M -> miss
        X -> destroyed plane cell
        """

        grid = [[' ' for _ in range(self._size)] for _ in range(self._size)]

        if show_planes:
            for plane in self._planes:
                for (r,c) in plane.cells:
                    grid[r][c]='P'

        for (r, c) in self._shots:
            hit=False
            for p in self._planes:
                if (r,c) in p.cells:
                    hit=True
                    break
            grid[r][c] = 'H' if hit else 'M'

        for plane in self._planes:
            if plane.is_destroyed():
                for (r,c) in plane.cells:
                    grid[r][c]='X'

        return grid

