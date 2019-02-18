clauses = []
literals = {}
clause_counter = 0
indices = []

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
    global clause_counter, clauses, indices
    
    for line in dimacs.split('\n'):
        clause = []
        for lit in line.split():
            if lit == 'p': break
            if lit != '0':
                clause.append(lit)
                add_to_lit_dict(lit, clause_counter)
            else:
                clauses.append(clause)
                indices.append(clause_counter)
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
    
def satisfied(ind):
	global indices
   
	indices.remove(ind)
	for lit in literals:
		toremove = []
		for tup in literals[lit]:
			if tup[0] == ind:
				toremove.append(tup)
		for tup in toremove:
			literals[lit].remove(tup)

def find_tautologies():
    prev_ind = -1
    prev_signs = []
    for lit in literals:
        for (ind, sign) in literals[lit]:
            if ind != prev_ind:
                prev_signs = [sign]
                prev_ind = ind
            elif sign*-1 in prev_signs:
                print('sat', ind)
                print(clauses[ind])
                satisfied(ind)
            else:
            	prev_signs.append(sign)
            #joe = raw_input('...')

def get_formula():
	return [clauses[index] for index in indices]

def find_pure_literals():
	formula = get_formula()
	for lit in literals:
		if not (any('-'+lit in clause for clause in formula) and any(lit in clause for clause in formula)):
			if(any('-'+lit in clause for clause in formula)):
				# Set pure literal to false
				literals[lit].append(0);
			else:
				# Set pure literal to true
				literals[lit].append(1)

def find_unit_clauses(truth_value=1):
	formula = get_formula()
	for clause in formula: 
		if len(clause)==1:
			literals[clause[0]].append(truth_value)
			if(truth_value==1):
				satisfied(literals[clause[0]][0][0])
			
def dpll():
	find_tautologies()
	find_pure_literals()
	find_unit_clauses()



with  open("sudoku-rules.txt") as file:
    data = file.read()

add_clauses(data)

with open("test sudokus/1000 sudokus.txt") as file:
    data = file.read()

sudokus = to_dimacs(data)

sudoku_nr = 0

add_clauses(sudokus[sudoku_nr])

'''
add_clauses("1811 -1811 0\n")

add_clauses("1812 -1813 0\n")

add_clauses("1345 0\n")

add_clauses("-1950 0\n")
'''

dpll()


