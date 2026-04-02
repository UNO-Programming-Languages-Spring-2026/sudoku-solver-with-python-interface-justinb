import clingo

class ClingoApp(clingo.application.Application):

    def print_model(self, model, printer) -> None:
        symbols = model.symbols(shown=True)
        symbols = sorted(symbols)
        print(" ".join(str(s) for s in symbols))

    def main(self, ctl, files):
        for f in files:
            ctl.load(f)
        if not files:
            ctl.load("-")
        ctl.load("sudoku.lp")
        ctl.ground()
        ctl.solve()

clingo.application.clingo_main(ClingoApp())