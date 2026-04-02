import clingo

class ClingoApp(clingo.application.Application):

    def main(self, ctl, files):
        for f in files:
            ctl.load(f)
        if not files:
            ctl.load("-")
        ctl.load("sudoku.lp")
        ctl.ground()
        ctl.solve()

clingo.application.clingo_main(ClingoApp())