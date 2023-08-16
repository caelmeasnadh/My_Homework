class Chess:
    color_white = 'white'
    color_black = 'black'

    def __init__(self, color, place_on_the_board):
        self.color = color
        self.place_on_the_board = place_on_the_board

    def __str__(self):
        print(f'Color : {self.color}, Place on board : {self.place_on_the_board}')

    def change_color(self):
        if self.color_white == self.color:
            self.color = self.color_black
        else:
            self.color = self.color_white

    def check_place_on_board(self):
        return 'Valid place' if 0 <= self.place_on_the_board[0] <= 7 and 0 <= self.place_on_the_board[1] <= 7 else 'Invalid place'

    def change_place_on_board(self, new_place):
        if 0 <= new_place[0] <= 7 and 0 <= new_place[1] <= 7:
            self.place_on_the_board = new_place
        else:
            print('Invalid place')

class Rook(Chess):
    def change_place_on_board(self, new_place):
        return self.place_on_the_board[0] == new_place[0] or self.place_on_the_board[1] == new_place[1]

class Knight(Chess):
    def change_place_on_board(self, new_place):
        x = self.place_on_the_board[0] - new_place[0]
        y = self.place_on_the_board[1] - new_place[1]

        return (x == 2 and y == 1) or (x == 1 or y == 2)

class Bishop(Chess):
    def change_place_on_board(self, new_place):
        x = self.place_on_the_board[0] - new_place[0]
        y = self.place_on_the_board[1] - new_place[1]

        return x == y

class Queen(Chess):
    def change_place_on_board(self, new_place):
        x = self.place_on_the_board[0] - new_place[0]
        y = self.place_on_the_board[1] - new_place[1]

        return x == y or self.place_on_the_board[0] == new_place[0] or self.place_on_the_board[1] == new_place[1]

class King(Chess):
    def change_place_on_board(self, new_place):
        x = self.place_on_the_board[0] - new_place[0]
        y = self.place_on_the_board[1] - new_place[1]

        return x <= 1 and y <= 1

class Pawn(Chess):
    def change_place_on_board(self, new_place):
        x = self.place_on_the_board[0] - new_place[0]
        y = self.place_on_the_board[1] - new_place[1]

        return True if y == 0 and x == 1 else False

def get_possible_moves(pieces, new_place):
    valid_pieces = []
    for piece in pieces:
        if piece.change_place_on_board(new_place):
            valid_pieces.append(piece)
    return valid_pieces

Rook = Rook('white', (2,1))
Knight = Knight('white', (5,2))
Bishop = Bishop('white', (3,3))
Queen = Queen('black', (3,3))
King = King('black', (5,3))
Pawn = Pawn('black', (6,1))

pieces = [Rook, Knight, Bishop, Queen, King, Pawn]
new_place = (4,4)

result = get_possible_moves(pieces,new_place)
for piece in result:
    print(f'{piece.color} {piece.__class__.__name__} can move to {new_place}')