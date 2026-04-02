import clingo
from sudoku_board import Sudoku

class Context:

    def __init__(self, board: Sudoku):
        self.sudoku = board
        
    def initial(self) -> list[clingo.symbol.Symbol]:
        sudokuDict = self.sudoku.sudoku

        symbols = []
        for item in self.sudoku.sudoku:
            a,b = item
            sym = clingo.Function("",[clingo.Number(a), clingo.Number(b), clingo.Number(sudokuDict[item])])
            symbols.append(sym)
        return symbols




class ClingoApp(clingo.application.Application):

    def print_model(self, model, printer) -> None:
        sudoku = Sudoku.from_model(model)
        print(sudoku)

    def main(self, ctl, files):
        ctl.load("sudoku.lp")
        ctl.load("sudoku_py.lp")
        f = open(files[0],"r")
        context = Context(Sudoku.from_str(f.read()))
        ctl.ground([("base", [])], context)
        ctl.solve()

clingo.application.clingo_main(ClingoApp())