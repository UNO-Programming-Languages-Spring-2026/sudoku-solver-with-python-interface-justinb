% Sudoku Solver
%
% Hints:
% For subgrid of size n, subgrids can be identified by labels 1..n*n
% A cell (x,y) can be mapped to the subgrid labeled 1+(((x-1)/n)*n+(y-1)/n)

% Your implementation please...

#const s = 9.
#const n = 3.

{sudoku(X,Y,N) : N = 1..s} = 1 :- X = 1..s, Y = 1..s.
% Generate board

:- initial(X1,Y1,N1), sudoku(X2,Y2,N2), X1 == X2, Y1 == Y2, N1 != N2.
% Follow initial requirements

:- sudoku(X,Y1,N1), sudoku(X,Y2,N2), Y1 != Y2, N1 == N2.
% Rows cannot have the same number

:- sudoku(X1,Y,N1), sudoku(X2,Y,N2), X1 != X2, N1 == N2.
% Columns cannot have the same number

subgrid(X,Y,G) :- X=1..s, Y = 1..s, G = 1+(((X-1)/n)*n+(Y-1)/n).
% Create facts with correct subgrids

:- sudoku(X1,Y1,N1), subgrid(X1,Y1,G1), sudoku(X2,Y2,N2), subgrid(X2,Y2,G2), X1 != X2, Y1 != Y2, G1 == G2, N1 == N2.
% Subgrids cannot contain the same number

#show sudoku/3.

