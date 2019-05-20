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
        self.is_piece_tested = []

    def get_status(self, x, y):
        """
        Get the status of a given position

        Args:
            x: the x coordinate
            y: the y coordinate

        Returns:
            a Status
        """
        if not self.goban or x < 0 or y < 0 or y >= len(self.goban) or x >= len(self.goban[0]):
            return Status.OUT
        elif self.goban[y][x] == '.':
            return Status.EMPTY
        elif self.goban[y][x] == 'o':
            return Status.WHITE
        elif self.goban[y][x] == '#':
            return Status.BLACK


    
    def is_taken(self, x, y):
        piece = self.get_status(x,y)#piece color
        if piece == Status.BLACK: opposite = Status.WHITE#|opposite color of
        if piece == Status.WHITE: opposite = Status.BLACK#|the piece

       
        self.is_piece_tested.append((x,y))#check if the piece have already been tested in a list.
        if piece == Status.BLACK or piece == Status.WHITE:

            #Check if the piece have no possibilities at all.
            if ( (self.get_status(x-1,y) ==  Status.OUT or self.get_status(x-1,y) ==  opposite)#left
            and  (self.get_status(x,y-1) ==  Status.OUT or self.get_status(x,y-1) ==  opposite)#bottom
            and  (self.get_status(x,y+1) ==  Status.OUT or self.get_status(x,y+1) ==  opposite)#top
            and  (self.get_status(x+1,y) ==  Status.OUT or self.get_status(x+1,y) ==  opposite) ):#right
                return True

            #Check if the piece got a empty case around it.
            if (self.get_status(x-1,y) ==  Status.EMPTY
            or  self.get_status(x,y-1) ==  Status.EMPTY
            or  self.get_status(x,y+1) ==  Status.EMPTY
            or  self.get_status(x+1,y) ==  Status.EMPTY):
                self.is_piece_tested[:] = []#reset the list
                return False

            #Check if the piece got a "sister" AND if that sister have others sisters, or got an empty case around.
            if self.get_status(x-1,y) ==  piece and (x-1,y) not in self.is_piece_tested and self.is_taken(x-1,y) == False:#left
                self.is_piece_tested[:] = []
                return False 
            if self.get_status(x,y-1) ==  piece and (x,y-1) not in self.is_piece_tested and self.is_taken(x,y-1) == False:#bottom
                self.is_piece_tested[:] = []
                return False 
            if self.get_status(x,y+1) ==  piece and (x,y+1) not in self.is_piece_tested and self.is_taken(x,y+1) == False:#top
                self.is_piece_tested[:] = []
                return False 
            if self.get_status(x+1,y) ==  piece and (x+1,y) not in self.is_piece_tested and self.is_taken(x+1,y) == False:#right
                self.is_piece_tested[:] = []
                return False 
            #Else at least if it got a locked sister.
            elif (self.get_status(x-1,y) ==  piece
            or self.get_status(x,y-1) ==  piece
            or self.get_status(x,y+1) ==  piece
            or self.get_status(x+1,y) ==  piece):  
                return True

