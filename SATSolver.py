clauses = []
sudokus = []

with  open("sudoku-rules.txt") as file:
    data = file.read()

for line in data.split('\n')[1:]:
    clause = []
    for lit in line.split():
        if lit != '0':
            clause.append(lit)
        else:
            clauses.append(clause)

print(clauses[-10:])

with open("test sudokus/1000 sudokus.txt") as file:
    data = file.read()

for line in data.split('\n'):
    if line == "": break
    sud = []
    ct = 0
    for i in range(1,10):
        for j in range(1,10):
            if line[ct] != '.':
                sud.append("%i%i%i" %(i,j,int(line[ct])))
            ct += 1
    sudokus.append(sud)

sudoku_nr = 0

clauses += sudokus[sudoku_nr]

print(clauses[-10:])
