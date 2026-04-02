from typing import Tuple
import clingo


class Sudoku:
    def __init__(self, sudoku: dict[Tuple[int, int], int]):
        self.sudoku = sudoku

    def __str__(self) -> str:
        s = ""
        sudokuDict = self.sudoku
        arr = [[0 for i in range(9)] for j in range(9)]
        for coord in sudokuDict:
            a,b = coord
            arr[a-1][b-1] = sudokuDict[coord]

        for i in range(9):
            for j in range(9):
                s += str(arr[i][j])
                if(j == 2 or j == 5):
                    s += "  "
                elif(j == 8):
                    if(i == 2 or i == 5):
                        s += "\n"
                    s += "\n" 
                else:
                    s += " "
        return s




    @classmethod
    def from_str(cls, s: str) -> "Sudoku":
        sudoku = {}
        # YOUR CODE HERE
        return cls(sudoku)

    @classmethod
    def from_model(cls, model: clingo.solving.Model) -> "Sudoku":
        sudoku = {}
        symbols = model.symbols(shown=True)
        for s in symbols:
            sudoku[(s.arguments[0].number,s.arguments[1].number)] = s.arguments[2].number

        return cls(sudoku)
