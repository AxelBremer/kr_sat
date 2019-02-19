from recordtype import recordtype

DataTuple = recordtype("DataTuple", "clauses literals indices clause_counter")

data_tuple = DataTuple([], {}, [], 0)

def add_to_lit_dict(lit, data):
    literals = data.literals
    
    if(lit[0]=='-'):
        lit = lit[1:]
        sign = -1
    else:
        sign = 1
    if lit not in literals:
        literals[lit] = {'occ':[], 'value':0}
    literals[lit]['occ'].append((data.clause_counter, sign))

def add_clauses(dimacs, data):
    clauses = data.clauses
    indices = data.indices
    
    for line in dimacs.split('\n'):
        clause = []
        for lit in line.split():
            if lit == 'p': break
            if lit != '0':
                clause.append(lit)
                add_to_lit_dict (lit, data)
            else:
                clauses.append(clause)
                indices.append(data.clause_counter)
                data.clause_counter += 1

def to_dimacs(data):
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
    
def satisfied(ind, data):
    indices = data.indices
    literals = data.literals
    
    indices.remove(ind)
    for lit in literals:
        toremove = []
        for tup in literals[lit]['occ']:
            if tup[0] == ind:
                toremove.append(tup)
        for tup in toremove:
            literals[lit]['occ'].remove(tup)

def find_tautologies(data):
    literals = data.literals
    prev_ind = -1
    prev_signs = []
    for lit in literals:
        for (ind, sign) in literals[lit]['occ']:
            if ind != prev_ind:
                prev_signs = [sign]
                prev_ind = ind
            elif sign*-1 in prev_signs:
                print('sat', ind)
                print(data.clauses[ind])
                satisfied(ind, data)
            else:
            	prev_signs.append(sign)

def is_pure(lit, data):
    lit_list = data.literals[lit]['occ']
    sign_list = [x[1] for x in lit_list]
    isTrue = all(x == sign_list[0] for x in sign_list)
    return isTrue, sign_list[0]

def find_pure_literals(data):
    literals = data.literals
    for lit in literals:
        pure, sign = is_pure(lit, data)
        if pure:
            print("pure", lit, sign)
            literals[lit]['value'] = sign

def find_unit_clauses(data):
    formula = get_formula(data)
    for clause in formula: 
        if len(clause)==1:
            if(truth_value==1):
                satisfied(literals[clause[0]][0][0])

def get_formula(data):
    return [data.clauses[i] for i in data.indices]
    
def check_clauses(data):
    for ind in data.indices:
        clause = data.clauses[ind]
        for atom in clause:
            if atom[0] == '-':
                sign = -1
                lit = atom[1:]
            else:
                sign = 1
                lit = atom
            if sign == data.literals[lit]['value']:
                satisfied(ind, data)
                return True
        return False

def dpll(data):
    find_tautologies(data)
    find_pure_literals(data)
    #find_unit_clauses(data)
    
    while(check_clauses(data)):
        pass
    
    if data.indices == []:
        return True, data



with  open("sudoku-rules.txt") as file:
    dat = file.read()

#add_clauses(dat)

with open("test sudokus/1000 sudokus.txt") as file:
    dat = file.read()

sudokus = to_dimacs(dat)

sudoku_nr = 0

#add_clauses(sudokus[sudoku_nr], data_tuple)


add_clauses("9999 -1442 0\n", data_tuple)

add_clauses("9999 -1552 0\n", data_tuple)

'''
add_clauses("1812 -1813 0\n")

add_clauses("1345 0\n")

add_clauses("-1950 0\n")
'''

print(dpll(data_tuple))


