# Author: Matthew Llanes
# Date: 3/12/2020
# Description: A playable game of Xiangqi

class XiangqiGame:
    """Represents a playable game of Xiangqi"""

    def __init__(self):
        """Initializes game's data members"""
        self._red = Red()
        self._black = Black()
        self._board = {
            'a' :   {
                1   :   self._red._chariot,
                2   :   ' + ',
                3   :   ' + ',
                4   :   self._red._soldier,
                5   :   ' + ',
                6   :   ' + ',
                7   :   self._black._soldier,
                8   :   ' + ',
                9   :   ' + ',
                10  :   self._black._chariot
            },
            'b' :   {
                1   :   self._red._horse,
                2   :   ' + ',
                3   :   self._red._cannon_1,
                4   :   ' + ',
                5   :   ' + ',
                6   :   ' + ',
                7   :   ' + ',
                8   :   self._black._cannon_1,
                9   :   ' + ',
                10  :   self._black._horse
            },
            'c'   :   {
                1   :   self._red._elephant,
                2   :   ' + ',
                3   :   ' + ',
                4   :   self._red._soldier,
                5   :   ' + ',
                6   :   ' + ',
                7   :   self._black._soldier,
                8   :   ' + ',
                9   :   ' + ',
                10  :   self._black._elephant
            },
            'd' :   {
                1   :   self._red._advisor,
                2   :   ' + ',
                3   :   ' + ',
                4   :   ' + ',
                5   :   ' + ',
                6   :   ' + ',
                7   :   ' + ',
                8   :   ' + ',
                9   :   ' + ',
                10  :   self._black._advisor
            },
            'e' :   {
                1   :   self._red._general,
                2   :   ' + ',
                3   :   ' + ',
                4   :   self._red._soldier,
                5   :   ' + ',
                6   :   ' + ',
                7   :   self._black._soldier,
                8   :   ' + ',
                9   :   ' + ',
                10  :   self._black._general
            },
            'f' :   {
                1   :   self._red._advisor,
                2   :   ' + ',
                3   :   ' + ',
                4   :   ' + ',
                5   :   ' + ',
                6   :   ' + ',
                7   :   ' + ',
                8   :   ' + ',
                9   :   ' + ',
                10  :   self._black._advisor
            },
            'g' :   {
                1   :   self._red._elephant,
                2   :   ' + ',
                3   :   ' + ',
                4   :   self._red._soldier,
                5   :   ' + ',
                6   :   ' + ',
                7   :   self._black._soldier,
                8   :   ' + ',
                9   :   ' + ',
                10  :   self._black._elephant
            },
            'h' :   {
                1   :   self._red._horse,
                2   :   ' + ',
                3   :   self._red._cannon_2,
                4   :   ' + ',
                5   :   ' + ',
                6   :   ' + ',
                7   :   ' + ',
                8   :   self._black._cannon_2,
                9   :   ' + ',
                10  :   self._black._horse
            },
            'i' :   {
                1   :   self._red._chariot,
                2   :   ' + ',
                3   :   ' + ',
                4   :   self._red._soldier,
                5   :   ' + ',
                6   :   ' + ',
                7   :   self._black._soldier,
                8   :   ' + ',
                9   :   ' + ',
                10  :   self._black._chariot
            }
        }
        self._game_state = "UNFINISHED"


    def print_board(self):
        """Prints game board"""
        for row in range(1,11):
            print(self._board['a'][row], self._board['b'][row], self._board['c'][row], self._board['d'][row],
                  self._board['e'][row], self._board['f'][row], self._board['g'][row], self._board['h'][row],
                    self._board['i'][row])


    def set_board(self, board):
        """Sets game board"""
        self._board = board


    def get_game_state(self):
        """Returns game state"""
        return self._game_state


    def set_game_state(self, game_state):
        """Updates game state"""
        self._game_state = game_state


    def is_in_check(self, player):
        """Returns true if player is in check"""
        # Determine variables
        if player == "red":
            opponent = self._black
            general = self._red._general
        elif player == "black":
            opponent = self._red
            general = self._black._general
        else:
            return

        # Get own general's position
        for column in range(ord('a'), ord('i') + 1):
            for row in range(1, 11):
                if self._board[chr(column)][row] == general:
                    gen_column = chr(column)
                    gen_row = row
                    break
                else:
                    continue

        # Identify each opponent's piece and determine if it can attack player's general
        for column in range(ord('a'), ord('i') + 1):
            for row in range(1, 11):
                if self._board[chr(column)][row] != ' + ':
                    piece = self._board[chr(column)][row]   # nonempty point on board
                    if opponent.whose_piece(piece) == opponent: # opponent's piece
                        if piece.legal_move(chr(column), row, gen_column, gen_row, repr(opponent), self._board) == True:
                            return True     # is indeed in check
                        else:
                            continue
                    else:
                        continue
                else:
                    continue
        return False    # if none are true, return false


    def make_move(self, fro, to):
        """
        Allows player to move their piece, may capture an enemy piece, u
        pdates game board, game state, and is in check method
        :param fro: string designating row and column moving from
        :param to: string designating row and column moving to
        :return: True if move valid, false otherwise
        """
        # define variables column and row for both to and fro if they're within board range
        if ord('i') < ord(fro[0]) < ord('a') or type(fro) != str:
            return False    # out of range or incorrect type of input
        else:
            from_column = fro[0]    # sets from's column

        if ord('i') < ord(to[0]) < ord('a') or type(to) != str:
            return False    # out of range or incorrect type of input
        else:
            to_column = to[0]   # sets to's column

        if len(fro) == 3:
            if int(fro[1] + fro[2]) > 10:   # out of board range
                return False
            else:
                from_row = int(fro[1] + fro[2]) # sets from's row for row 10
        else:
            from_row = int(fro[1])   # sets from's row if less than 10

        if len(to) == 3:
            if int(to[1] + to[2]) > 10:     # out of board range
                return False
            else:
                to_row = int(to[1] + to[2]) # sets to's row for row 10
        else:
            to_row = int(to[1]) # sets to's row if less than 10

        # identify variables for moving piece type and player the piece belongs to
        moving_piece = self._board[from_column][from_row]
        if moving_piece == ' + ':
            return False

        if self._red.whose_piece(moving_piece) == self._red:
            player = self._red
        else:
            player = self._black
        if player.get_is_turn() == False:   # wrong player's turn
            return False

        # identify if there is a piece in the spot moving to and player it belongs to
        to_spot = self._board[to_column][to_row]
        if player.whose_piece(to_spot) == player:   # if player tries to move other player's piece
            return False

        # checks piece specific conditions for moving
        if moving_piece.legal_move(from_column, from_row, to_column, to_row, repr(player), self._board) == False:
            return False

        # check for flying generals
        if self.flying_general() == True:
            return False

        # move piece, remove piece if there's an opposing players piece in the spot
        else:
            self._board[to_column][to_row] = self._board[from_column][from_row]
            self._board[from_column][from_row] = " + "

        # update game state
        if self.checkmate("red") == True:
            self.set_game_state("BLACK_WON")
        elif self.checkmate("black") == True:
            self.set_game_state("RED_WON")

        # update player's turn
        if self._red.get_is_turn() == True:
            self._red.set_is_turn(False)
        else:
            self._red.set_is_turn(True)
        if self._black.get_is_turn() == True:
            self._black.set_is_turn(False)
        else:
            self._black.set_is_turn(True)
        return True


    def exchange_horse(self, position):
        """Changes cannon to horse if in starting position"""
        column = position[0]
        row = position[1]
        if position == 'b3' and self._red._cannon_1.get_has_gone() == False:
            self._board[column][row] = self._red._horse
        elif position == 'h3' and self._red._cannon_2.get_has_gone() == False:
            self._board[column][row] = self._red._horse
        elif position == 'b8' and self._black._cannon_1.get_has_gone() == False:
            self._board[column][row] = self._black._horse
        elif position == 'h8' and self._black._cannon_2.get_has_gone() == False:
            self._board[column][row] = self._black._horse
        else:
            return False


    def checkmate(self, player):
        """Returns true if player is in checkmate, false otherwise"""

        # Define variables
        if player == "red":
            general = self._red._general
            palace_rows = {1, 2, 3}
        elif player == "black":
            general = self._red._general
            palace_rows = {8, 9, 10}
        else:
            return False

        # Get own general's position
        for column in range(ord('d'), ord('g')):
            for row in range(1, 11):
                if self._board[chr(column)][row] == general:
                    gen_column = chr(column)
                    gen_row = row
                    break
                else:
                    continue

        # Check if moves the general can make would put it in check
        for column in range(ord('d'), ord('g')):
            for row in palace_rows:
                if general.legal_move(gen_column, gen_row, chr(column), row, player, self._board) == True \
                    and self._board[chr(column)][row] == ' + ':
                    self._board[chr(column)][row] = general         # set general to move to spot
                    if self.is_in_check(player) == False:           # if that move gets general out of check
                        self._board[chr(column)][row] = ' + '       # reset pieces
                        self._board[gen_column][gen_row] = general
                        return False
                    else:
                        self._board[chr(column)][row] = ' + '       # reset pieces
                        self._board[gen_column][gen_row] = general
                        continue
                else:
                    continue
        return True


    def flying_general(self):
        """Return true if generals can see eachother"""
        # Get columns and rows of both generals
        for column in range(ord('d'), ord('g')):
            for row in range(1, 11):
                if self._board[chr(column)][row] == self._red._general:
                    red_column = chr(column)
                    red_row = row
                elif self._board[chr(column)][row] == self._black._general:
                    black_column = chr(column)
                    black_row = row
                else:
                    continue

        if red_column != black_column:  # can't face each other from different columns
            return False
        else:
            column = red_column
            for row in range(red_row + 1, black_row):
                if self._board[column][row] != ' + ':
                    return False
                else:
                    continue
            return True


class Player:
    """Represents a player in a Xiangqi game."""

    def __init__(self):
        """Initializes player's data members"""
        self._general = General()
        self._advisor = Advisor()
        self._elephant = Elephant()
        self._horse = Horse()
        self._chariot = Chariot()
        self._cannon_1 = Cannon()
        self._cannon_2 = Cannon()
        self._soldier = Soldier()
        self._is_turn = None


    def get_is_turn(self):
        """Returns true if it's player's turn, false otherwise"""
        return self._is_turn


    def set_is_turn(self, turn):
        """Updates player's turn"""
        self._is_turn = turn


    def whose_piece(self, piece):
        pieces = {self._general, self._advisor, self._elephant, self._horse,
                  self._chariot, self._cannon_1, self._cannon_2, self._soldier}
        if piece in pieces:
            return self


class Red(Player):
    """Represents the red player."""

    def __init__(self):
        """Initializes red player's data members"""
        super().__init__()
        self._is_turn = True


    def __repr__(self):
        return "red"


class Black(Player):
    """Represents the black player."""

    def __init__(self):
        """Initializes black player's data members"""
        super().__init__()
        self._is_turn = False


    def __repr__(self):
        return "black"


class Piece:
    """Represents a generic piece in a Xiangqi game."""

    def __init__(self):
        """Initializes piece"""


class General(Piece):
    """Represents a general piece"""

    def __init__(self):
        """Initializes general's data members"""
        super().__init__()

    def __repr__(self):
        return "GEN"


    def legal_move(self, from_column, from_row, to_column, to_row, player, board):
        """Returns true if legal, false otherwise"""
        # Define variables
        palace_columns = {'d', 'e', 'f'}
        if player == "red":
            palace_rows = {1, 2, 3}
        elif player == "black":
            palace_rows = {8, 9, 10}
        else:
            return False


        # General must stay in palace
        if to_column not in palace_columns:
            return False
        elif to_row not in palace_rows:
            return False

        # General can move one point orthogonally
        elif ord(to_column) == ord(from_column) + 1 or ord(to_column) == ord(from_column) - 1:
            if to_row == from_row + 1 or to_row == from_row - 1:
                return False
            else:
                return True
        elif to_row == from_row +1 or to_row == from_row - 1:
            if ord(to_column) == ord(from_column) + 1 or ord(to_column) == ord(from_column) - 1:
                return False
            else:
                return True
        else:
            return False

class Advisor(Piece):
    """Represents a advisor piece"""

    def __init__(self):
        """Initializes advisor's data members"""
        super().__init__()

    def __repr__(self):
        return "ADV"


    def legal_move(self, from_column, from_row, to_column, to_row, player, board):
        """Returns true if legal, false otherwise"""
        # Define variables
        palace_columns = {'d', 'e', 'f'}
        if player == 'red':
            palace_rows = {1, 2, 3}
        else:
            palace_rows = {8, 9, 10}

        # Advisor must stay in palace
        if to_column not in palace_columns:
            return False
        elif to_row not in palace_rows:
            return False

        # Can move one point diagonally
        if ord(to_column) == ord(from_column) + 1 or ord(to_column) == ord(from_column) - 1:
            if to_row == from_row + 1 or to_row == from_row - 1:
                return True
            else:
                return False
        elif to_row == from_row + 1 or to_row == from_row - 1:
            if ord(to_column) == ord(from_column) + 1 or ord(to_column) == ord(from_column) - 1:
                return True
            else:
                return False
        else:
            return False


class Elephant(Piece):
    """Represents an elephant piece"""

    def __init__(self):
        """Initializes elephant's data members"""
        super().__init__()

    def __repr__(self):
        return "ELE"


    def legal_move(self, from_column, from_row, to_column, to_row, player, board):
        """Returns true if legal, false otherwise"""
        # Cannot cross river
        if player == 'red':
            if to_row > 5:
                return False
        else:
            if to_row < 6:
                return False

        # Can move two points diagonally without jumping over other pieces
        if ord(to_column) == ord(from_column) + 2 and to_row == from_row + 2:   # right and up
            if board[chr(ord(from_column) + 1)][from_row + 1] == ' + ': # must be empty
                return True
            else:
                return False
        elif ord(to_column) == ord(from_column) + 2 and to_row == from_row - 2: # right and down
            if board[chr(ord(from_column) + 1)][from_row - 1] == ' + ': # must be empty
                return True
            else: return False
        elif ord(to_column) == ord(from_column) - 2 and to_row == from_row - 2: # left and down
            if board[chr(ord(from_column) - 1)][from_row - 1] == ' + ': # must be empty
                return True
            else:
                return False
        elif ord(to_column) == ord(from_column) - 2 and to_row == from_row + 2: # left and up
            if board[chr(ord(from_column) - 1)][from_row + 1] == ' + ': # must be empty
                return True
            else: return False
        else:
            return False


class Horse(Piece):
    """Represents a horse piece"""

    def __init__(self):
        """Initializes horse's data members"""
        super().__init__()


    def __repr__(self):
        return "HRS"


    def legal_move(self, from_column, from_row, to_column, to_row, player, board):
        """Returns true if legal, false otherwise"""
        # One space orthogonally and one diagonally (away from original spot)
        # Movement to a spot to the left
        if ord(to_column) == ord(from_column) - 2:
            if board[chr(ord(to_column) - 1)][from_row] != ' + ':    # cannot jump pieces
                return False
            elif to_row == from_row + 1 or to_row == from_row - 1:  # potential diagonals
                return True
            else:
                return False

        # Movement to a spot to the right
        elif ord(to_column) == ord(from_column) + 2:
            if board[chr(ord(to_column) + 1)][from_row] != ' + ':    # cannot jump pieces
                return False
            elif to_row == from_row + 1 or to_row == from_row - 1:  # potential diagonals
                return True
            else:
                return False

        # Movement above
        elif to_row == from_row - 2:
            if board[from_column][from_row - 1] != ' + ':   # cannot jump pieces
                return False
            elif ord(to_column) == ord(from_column) + 1 or ord(to_column) == ord(from_column) - 1: # potential diagonals
                return True
            else:
                return False

        # Movement below
        elif to_row == from_row + 2:
            if board[from_column][from_row + 1] != ' + ':   # cannot jump pieces
                return False
            elif ord(to_column) == ord(from_column) + 1 or ord(to_column) == ord(from_column) - 1: # potential diagonals
                return True
            else:
                return False
        else:
            return False


class Chariot(Piece):
    """
    Represents a chariot piece
    """

    def __init__(self):
        """
        Initializes chariot's data members
        """
        super().__init__()

    def __repr__(self):
        return "CHR"


    def legal_move(self, from_column, from_row, to_column, to_row, player, board):
        """Returns true if legal, false otherwise"""
        # Any distance orthogonally
        # if moving up or down
        if from_column == to_column:
            if from_row < to_row:       # if moving down
                for row in range(from_row + 1, to_row): # path of movement
                    if board[to_column][row] != ' + ':  # cannot jump other pieces
                        return False
            elif from_row > to_row:   # if moving up
                for row in range(to_row + 1, from_row): # path of movement
                    if board[to_column][row] != ' + ':  # cannot jump other pieces
                        return False
            else:
                return True

        # if moving right or left
        elif from_row == to_row:
            if ord(from_column) < ord(to_column):   # if moving right
                for column in range(ord(from_column) + 1, ord(to_column)):  # path of movement
                    if board[chr(column)][to_row] != ' + ': # cannot jump other pieces
                        return False
            elif ord(from_column) > ord(to_column): # if moving left
                for column in range(ord(to_column) + 1, ord(from_column)):  # path of movement
                    if board[chr(column)][to_row] != ' + ': # cannot jump other pieces
                        return False
            else:
                return True
        else:   # neither the same row nor the same column (not orthogonally)
            return False


class Cannon(Piece):
    """Represents a cannon piece"""

    def __init__(self):
        """Initializes cannon's data members"""
        super().__init__()
        self._has_gone = False

    def __repr__(self):
        return "CAN"


    def legal_move(self, from_column, from_row, to_column, to_row, player, board):
        """Returns true if legal, false otherwise"""
        # If moving up or down
        if from_column == to_column:
            if from_row < to_row:       # if moving down
                if board[to_column][to_row] != ' + ':   # attacking
                    for row in range(from_row + 1, to_row):  # path of movement
                        if board[to_column][row] != ' + ':  # looking for cannon platform
                            self.set_has_gone()
                            return True
                        else:
                            continue
                    return False    # tried to attack without a platform
                else:   # NOT attacking
                    for row in range(from_row + 1, to_row):  # path of movement
                        if board[to_column][row] != ' + ':  # cannot jump other pieces
                            return False

            elif from_row > to_row:   # if moving up
                if board[to_column][to_row] != ' + ':   # attacking
                    for row in range(to_row + 1, from_row): # path of movement
                        if board[to_column][row] != ' + ':  # looking for cannon platform
                            self.set_has_gone()
                            return True
                        else:
                            continue
                    return False    # tried to attack without a platform
                else:   # NOT attacking
                    for row in range(to_row + 1, from_row): # path of movement
                        if board[to_column][row] != ' + ':  # cannot jump other pieces
                            return False

        # if moving right or left
        elif from_row == to_row:
            if ord(from_column) < ord(to_column):   # if moving right
                if board[to_column][to_row] != ' + ':  # attacking
                    for column in range(ord(from_column) + 1, ord(to_column)):  # path of movement
                        if board[chr(column)][to_row] != ' + ': # looking for cannon platform
                            self.set_has_gone()
                            return True
                        else:
                            continue
                    return False    # tried to attack without a platform
                else:   # NOT attacking
                    for column in range(ord(from_column) + 1, ord(to_column)):  # path of movement
                        if board[chr(column)][to_row] != ' + ': # cannot jump other pieces
                            return False

            elif ord(from_column) > ord(to_column): # if moving left
                if board[to_column][to_row] != ' + ':  # attacking
                    for column in range(ord(to_column) + 1, ord(from_column)):  # path of movement
                        if board[chr(column)][to_row] != ' + ': # looking for cannon platform
                            self.set_has_gone()
                            return True
                        else:
                            continue
                    return False    # tried to attack without a platform
                else:   # NOT attacking
                    for column in range(ord(to_column) + 1, ord(from_column)):  # path of movement
                        if board[chr(column)][to_row] != ' + ': # cannot jump other pieces
                            return False
            else:
                self.set_has_gone()
                return True
        else:   # neither the same row nor the same column (not orthogonally)
            return False


    def get_has_gone(self):
        """Returns true if piece has had a turn, false otherwise"""
        return self._has_gone


    def set_has_gone(self, has_gone = True):
        """CHanges value of get has gone to true"""
        self._has_gone = has_gone


class Soldier(Piece):
    """Represents a soldier piece"""

    def __init__(self):
        """Initializes soldier's data members"""
        super().__init__()

    def __repr__(self):
        return "SLD"


    def legal_move(self, from_column, from_row, to_column, to_row, player, board):
        """Returns true if legal, false otherwise"""
        if player == 'red':
            if to_column == from_column and to_row == from_row + 1: # can move forward one place
                return True
            elif from_row >= 6:     # after passing the river
                if to_row == from_row:
                    if ord(to_column) == ord(from_column) + 1 or ord(to_column) == ord(from_column) - 1:
                        return True     # can move one space horizontally as well
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:   # black player
            if to_column == from_column and to_row == from_row - 1: # can move forward one place
                return True
            elif from_row <= 5:     # after passing the river
                if to_row == from_row:
                    if ord(to_column) == ord(from_column) + 1 or ord(to_column) == ord(from_column) - 1:
                        return True     # can move one space horizontally as well
                    else:
                        return False
                else:
                    return False
            else:
                return False