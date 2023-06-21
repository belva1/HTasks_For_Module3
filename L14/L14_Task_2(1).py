# king - король, queen - ферзь, rook - ладья, bishop - слон, knight - конь, pawn - пешка

class Figure:
    def __init__(self, color: bool, place: tuple) -> None:  # initialization
        self.color = color
        self.place = place  # place[0] - column, place[1] - row

    def change_color(self) -> None:
        if self.color:  # self.color == True
            self.color = False
        else:
            self.color = True

    def change_place(self, new_place: tuple) -> None:
        self.place = new_place


# KING
class King(Figure):
    def __str__(self) -> str:
        return f'Type: King, place: {self.place}, color: {"white" if self.color else "black"}.'

    def check_king(self, check_place: tuple) -> bool:
        if abs(self.place[0] - check_place[0]) <= 1 and abs(self.place[1] - check_place[1]) <= 1:
            return True
        return False


# QUEEN
class Queen(Figure):
    def __str__(self) -> str:
        return f'Type: Queen, place: {self.place}, color: {"white" if self.color else "black"}.'

    def check_queen(self, check_place: tuple) -> bool:
        if self.place[0] == check_place[0] or self.place[1] == check_place[1] or abs(self.place[0] - check_place[0]) == abs(self.place[1] - check_place[1]) or self.place[0] + self.place[1] == check_place[0] + check_place[1]:
            return True
        return False


# ROOK
class Rook(Figure):
    def __str__(self) -> str:
        return f'Type: Rook, place: {self.place}, color: {"white" if self.color else "black"}.'

    def check_rook(self, check_place: tuple) -> bool:
        if self.place[0] == check_place[0] or self.place[1] == check_place[1]:
            return True
        return False


# BISHOP
class Bishop(Figure):
    def __str__(self) -> str:
        return f'Type: Bishop, place: {self.place}, color: {"white" if self.color else "black"}.'

    def check_bishop(self, check_place: tuple) -> bool:
        if abs(self.place[0] - check_place[0]) == abs(self.place[1] - check_place[1]) or self.place[0] + self.place[1] == check_place[0] + check_place[1]:
            return True
        return False


# KNIGHT
class Knight(Figure):
    def __str__(self) -> str:
        return f'Type: Knight, place: {self.place}, color: {"white" if self.color else "black"}.'

    def check_knight(self, check_place: tuple) -> bool:
        if abs(self.place[0] - check_place[0]) * abs(self.place[1] - check_place[1]) == 2:
            return True
        return False


# PAWN
class Pawn(Figure):
    def __str__(self) -> str:
        return f'Type: Pawn, place: {self.place}, color: {"white" if self.color else "black"}.'

    def check_pawn(self, check_place: tuple) -> bool:
        if self.color:
            if self.place[0] == check_place[0]:
                if self.place[1] == 1 and check_place[1] == 3:
                    return True
                elif check_place[1] - self.place[1] == 1:
                    return True
            return False
        else:
            if self.place[0] == check_place[0]:
                if self.place[1] == 6 and check_place[1] == 4:
                    return True
                elif check_place[1] - self.place[1] == -1:
                    return True
            return False


color: bool = bool(int(input('0 - Black, any other number - White: ')))
while True:
    place: tuple = tuple(map(int, input('Please enter King place: ').split()))
    if place[0] in range(8) and place[1] in range(8):
        break
    else:
        print('You need to enter 2 numbers from 0 to 8 with space please.')
king: King = King(color, place)


color: bool = bool(int(input('0 - Black, any other number - White: ')))
while True:
    place: tuple = tuple(map(int, input('Please enter Queen place: ').split()))
    if place[0] in range(8) and place[1] in range(8):
        break
    else:
        print('You need to enter 2 numbers from 0 to 8 with space please.')
queen: Queen = Queen(color, place)


color: bool = bool(int(input('0 - Black, any other number - White: ')))
while True:
    place: tuple = tuple(map(int, input('Please enter Rook place: ').split()))
    if place[0] in range(8) and place[1] in range(8):
        break
    else:
        print('You need to enter 2 numbers from 0 to 8 with space please.')
rook: Rook= Rook(color, place)


color: bool = bool(int(input('0 - Black, any other number - White: ')))
while True:
    place: tuple = tuple(map(int, input('Please enter Bishop place: ').split()))
    if place[0] in range(8) and place[1] in range(8):
        break
    else:
        print('You need to enter 2 numbers from 0 to 8 with space please.')
bishop: Bishop = Bishop(color, place)


color: bool = bool(int(input('0 - Black, any other number - White: ')))
while True:
    place: tuple = tuple(map(int, input('Please enter Knight place: ').split()))
    if place[0] in range(8) and place[1] in range(8):
        break
    else:
        print('You need to enter 2 numbers from 0 to 8 with space please.')
knight: Knight = Knight(color, place)


color: bool = bool(int(input('0 - Black, any other number - White: ')))
while True:
    place: tuple = tuple(map(int, input('Please enter Pawn place: ').split()))
    if place[0] in range(8) and place[1] in range(8):
        break
    else:
        print('You need to enter 2 numbers from 0 to 8 with space please.')
pawn: Pawn = Pawn(color, place)


while True:
    check_place: tuple = tuple(map(int, input('Please enter place: ').split()))
    if check_place[0] in range(8) and check_place[1] in range(8):
        break
    else:
        print('You need to enter 2 numbers from 0 to 8 with space please.')


print('King:', king.check_king(check_place))
print('Queen:', queen.check_queen(check_place))
print('Rook:', rook.check_rook(check_place))
print('Bishop:', bishop.check_bishop(check_place))
print('Knight:', knight.check_knight(check_place))
print('Pawn:', pawn.check_pawn(check_place))