import random

class ComputerStrategy:
    def __init__(self):
        """
        Stores the last position where computer scored a hit. If None, AI is in searching
        """
        self._last_hit=None

    def choose_move(self,board):
        """
        Determine the next move for computer.
        The strategy has 3 phases:
        1. If the previous shot was a hit, shoot around that hit
        2. If there were earlier hits, shoot around them
        3. Otherwise choose a random unshot cell
        """
        size=board.size
        if self._last_hit is not None:
            r,c=self._last_hit
            neighbors=[
                (r-1,c),(r+1,c),
                (r, c-1),(r,c+1)
            ]
            random.shuffle(neighbors)

            for nr,nc in neighbors:
                if 0<=nr<size and 0<=nc<size:
                    if (nr,nc) not in board._shots:
                        return (nr,nc)


            self._last_hit=None

        for r,c in board._shots:
            was_hit=False
            for plane in board._planes:
                if (r,c) in plane.cells:
                    was_hit=True
                    break

            if was_hit:
                neighbors = [
                    (r - 1, c), (r + 1, c),
                    (r, c - 1), (r, c + 1)
                ]
                random.shuffle(neighbors)
                for nr, nc in neighbors:
                    if 0 <= nr < size and 0 <= nc < size:
                        if (nr, nc) not in board._shots:
                            return (nr, nc)



        while True:
            r=random.randint(0,size-1)
            c=random.randint(0,size-1)

            if (r,c) not in board._shots:
                return (r,c)


    def update_after_shot(self,pos,result):
        """
        Update after a shot is resolved
        """
        if result=="hit":
            self._last_hit=pos
        elif result=="destroyed":
            self._last_hit=None


