import enum


class Status(enum.Enum):
    """
    Enum representing the Status of a position on a goban
    """

    WHITE = 1
    BLACK = 2
    EMPTY = 3
    OUT = 4


class Goban(object):
    def __init__(self, goban):
        self.goban = goban

    def get_status(self, x, y):
        """
        Get the status of a given position

        Args:
            x: the x coordinate
            y: the y coordinate

        Returns:
            a Status
        """
        if (
            not self.goban
            or x < 0
            or y < 0
            or y >= len(self.goban)
            or x >= len(self.goban[0])
        ):
            return Status.OUT
        elif self.goban[y][x] == ".":
            return Status.EMPTY
        elif self.goban[y][x] == "o":
            return Status.WHITE
        elif self.goban[y][x] == "#":
            return Status.BLACK

    def is_taken(self, x, y, ignore_list=None, base_status=None):
        """
        Tells if a given position is taken or not

        Args:
            x: the x coordinate
            y: the y coordinate
            ignore_list: the set of positions (as tuples) to ignore when
            looking at adjacent positions (default is None)
            base_status: the status of targetted shape (default is None)

        Returns:
            True if the given position is taken, False otherwise
        """
        if ignore_list is None:
            ignore_list = set()
        ignore_list.add((x, y))

        status = self.get_status(x, y)
        if status == Status.EMPTY:
            return False
        elif status == Status.OUT:
            return base_status is not None
        elif base_status is None:
            base_status = status
        elif status != base_status:
            return True

        taken_count = 0
        for side in [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]:
            if side in ignore_list:
                continue

            taken_count += 1
            if not self.is_taken(
                *side, ignore_list=ignore_list, base_status=base_status
            ):
                return False
            taken_count -= 1

        return taken_count == 0
