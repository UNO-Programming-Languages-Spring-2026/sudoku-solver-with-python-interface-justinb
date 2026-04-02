import clingo

class ClingoApp(clingo.application.Application):

    def print_model(self, model, printer) -> None:
        sudoku = {}
        symbols = model.symbols(shown=True)
        for s in symbols:
            sudoku[(s.arguments[0].number,s.arguments[1].number)] = s.arguments[2].number

        s = ""
        sudokuDict = sudoku
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
        print(s)

    def main(self, ctl, files):
        for f in files:
            ctl.load(f)
        if not files:
            ctl.load("-")
        ctl.load("sudoku.lp")
        ctl.ground()
        ctl.solve()

clingo.application.clingo_main(ClingoApp())