clauses = []
literals = {}
clause_counter = 0

def add_to_lit_dict(lit, index):
    global literals
    
    if(lit[0]=='-'):
        lit = lit[1:]
        sign = -1
    else:
        sign = 1
    if lit not in literals:
        literals[lit] = []
    literals[lit].append((index, sign))

def add_clauses(dimacs):
    global clause_counter, clauses
    
    print(clause_counter)
    
    for line in dimacs.split('\n')[1:]:
        clause = []
        for lit in line.split():
            if lit != '0':
                clause.append(lit)
                add_to_lit_dict(lit, clause_counter)
            else:
                clauses.append(clause)
                clause_counter += 1

def to_dimacs(sudokus):
    sudokus = []
    for line in data.split('\n'):
        if line == "": break
        sud = ""
        ct = 0
        for i in range(1,10):
            for j in range(1,10):
                if line[ct] != '.':
                    sud += "%i%i%i 0\n" %(i,j,int(line[ct]))
                ct += 1
        sudokus.append(sud)
    return sudokus

with  open("sudoku-rules.txt") as file:
    data = file.read()
    
add_clauses(data)

with open("test sudokus/1000 sudokus.txt") as file:
    data = file.read()

sudokus = to_dimacs(data)

sudoku_nr = 0

add_clauses(sudokus[sudoku_nr])