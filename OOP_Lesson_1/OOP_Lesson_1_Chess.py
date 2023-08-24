class Chess:
    color_white = 'white'
    color_black = 'black'

# В першому варіанті перевірка в мене повертала строку і не виконувалась в ініті, додаю її в ініт так, щоб повертала bool
    def __init__(self, color, place_on_the_board):
        self.color = color
        if 0 <= place_on_the_board[0] <= 7 and 0 <= place_on_the_board[1] <= 7:
            self.place_on_the_board = place_on_the_board
        else:
            print('Invalid position')

    def __str__(self):
        return (f'Color : {self.color}, Place on board : {self.place_on_the_board}')

    def change_color(self):
        if self.color_white == self.color:
            self.color = self.color_black
        else:
            self.color = self.color_white

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

# У наступному блоці для позначення кольорів не використовував константи, а просто строки. І також перебивав
# назвою змінних клас, тому не було можливості створити ще один об*єкт класу.
rook_1 = Rook(Chess.color_white, (2, 1))
knight_1 = Knight(Chess.color_white, (5, 2))
bishop_1 = Bishop(Chess.color_white, (3, 3))
queen_1 = Queen(Chess.color_black, (3, 3))
king_1 = King(Chess.color_black, (5, 3))
pawn_1 = Pawn(Chess.color_black, (6, 1))

pieces = [rook_1, knight_1, bishop_1, queen_1, king_1, pawn_1]
new_place = (4, 4)

result = get_possible_moves(pieces, new_place)
for piece in result:
    print(f'{piece.color} {piece.__class__.__name__} can move to {new_place}')
print(rook_1)
print(king_1)