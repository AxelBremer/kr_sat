import pdb
import copy
import random
import time
import progressbar
import pickle
from collections import Counter

global performance_score, call_heuristic, failed_clauses, bar, total
def print_sudoku(true_vars):
    """
    Print sudoku.
    :param true_vars: List of variables that your system assigned as true. Each var should be in the form of integers.
    :return:
    """
    if len(true_vars) != 81:
        print("Wrong number of variables.")
        return
    s = []
    row = []
    for i in range(len(true_vars)):
        row.append(str(int(true_vars[i]) % 10))
        if (i+1) % 9 == 0:
            s.append(row)
            row = []

    print("   " + "0" + "   " + "1" + "   " + "2" + "   " + "3" + "   " + "4" + "   " + "5" + "   " + "6" + "   " + "7" + "   " + "8" + "  ")
    print(" ╔═" + "═" + "═╦═" + "═" + "═╦═" + "═" + "═╦═" + "═" + "═╦═" + "═" + "═╦═" + "═" + "═╦═" + "═" + "═╦═" + "═" + "═╦═" + "═" + "═╗")
    print("0║ "+s[0][0]+" | "+s[0][1]+" | "+s[0][2]+" ║ "+s[0][3]+" | "+s[0][4]+" | "+s[0][5]+" ║ "+s[0][6]+" | "+s[0][7]+" | "+s[0][8]+" ║")
    print(" ╠─" + "─" + "─┼─" + "─" + "─┼─" + "─" + "─╬─" + "─" + "─┼─" + "─" + "─┼─" + "─" + "─╬─" + "─" + "─┼─" + "─" + "─┼─" + "─" + "─╣")
    print("1║ "+s[1][0]+" | "+s[1][1]+" | "+s[1][2]+" ║ "+s[1][3]+" | "+s[1][4]+" | "+s[1][5]+" ║ "+s[1][6]+" | "+s[1][7]+" | "+s[1][8]+" ║")
    print(" ╠─" + "─" + "─┼─" + "─" + "─┼─" + "─" + "─╬─" + "─" + "─┼─" + "─" + "─┼─" + "─" + "─╬─" + "─" + "─┼─" + "─" + "─┼─" + "─" + "─╣")
    print("2║ "+s[2][0]+" | "+s[2][1]+" | "+s[2][2]+" ║ "+s[2][3]+" | "+s[2][4]+" | "+s[2][5]+" ║ "+s[2][6]+" | "+s[2][7]+" | "+s[2][8]+" ║")
    print(" ╠═" + "═" + "═╬═" + "═" + "═╬═" + "═" + "═╬═" + "═" + "═╬═" + "═" + "═╬═" + "═" + "═╬═" + "═" + "═╬═" + "═" + "═╬═" + "═" + "═╣")
    print("3║ "+s[3][0]+" | "+s[3][1]+" | "+s[3][2]+" ║ "+s[3][3]+" | "+s[3][4]+" | "+s[3][5]+" ║ "+s[3][6]+" | "+s[3][7]+" | "+s[3][8]+" ║")
    print(" ╠─" + "─" + "─┼─" + "─" + "─┼─" + "─" + "─╬─" + "─" + "─┼─" + "─" + "─┼─" + "─" + "─╬─" + "─" + "─┼─" + "─" + "─┼─" + "─" + "─╣")
    print("4║ "+s[4][0]+" | "+s[4][1]+" | "+s[4][2]+" ║ "+s[4][3]+" | "+s[4][4]+" | "+s[4][5]+" ║ "+s[4][6]+" | "+s[4][7]+" | "+s[4][8]+" ║")
    print(" ╠─" + "─" + "─┼─" + "─" + "─┼─" + "─" + "─╬─" + "─" + "─┼─" + "─" + "─┼─" + "─" + "─╬─" + "─" + "─┼─" + "─" + "─┼─" + "─" + "─╣")
    print("5║ "+s[5][0]+" | "+s[5][1]+" | "+s[5][2]+" ║ "+s[5][3]+" | "+s[5][4]+" | "+s[5][5]+" ║ "+s[5][6]+" | "+s[5][7]+" | "+s[5][8]+" ║")
    print(" ╠═" + "═" + "═╬═" + "═" + "═╬═" + "═" + "═╬═" + "═" + "═╬═" + "═" + "═╬═" + "═" + "═╬═" + "═" + "═╬═" + "═" + "═╬═" + "═" + "═╣")
    print("6║ "+s[6][0]+" | "+s[6][1]+" | "+s[6][2]+" ║ "+s[6][3]+" | "+s[6][4]+" | "+s[6][5]+" ║ "+s[6][6]+" | "+s[6][7]+" | "+s[6][8]+" ║")
    print(" ╠─" + "─" + "─┼─" + "─" + "─┼─" + "─" + "─╬─" + "─" + "─┼─" + "─" + "─┼─" + "─" + "─╬─" + "─" + "─┼─" + "─" + "─┼─" + "─" + "─╣")
    print("7║ "+s[7][0]+" | "+s[7][1]+" | "+s[7][2]+" ║ "+s[7][3]+" | "+s[7][4]+" | "+s[7][5]+" ║ "+s[7][6]+" | "+s[7][7]+" | "+s[7][8]+" ║")
    print(" ╠─" + "─" + "─┼─" + "─" + "─┼─" + "─" + "─╬─" + "─" + "─┼─" + "─" + "─┼─" + "─" + "─╬─" + "─" + "─┼─" + "─" + "─┼─" + "─" + "─╣")
    print("9║ "+s[8][0]+" | "+s[8][1]+" | "+s[8][2]+" ║ "+s[8][3]+" | "+s[8][4]+" | "+s[8][5]+" ║ "+s[8][6]+" | "+s[8][7]+" | "+s[8][8]+" ║")
    print(" ╚═" + "═" + "═╩═" + "═" + "═╩═" + "═" + "═╩═" + "═" + "═╩═" + "═" + "═╩═" + "═" + "═╩═" + "═" + "═╩═" + "═" + "═╩═" + "═" + "═╝")

def check_sudoku(true_vars):
    """
    Check sudoku.
    :param true_vars: List of variables that your system assigned as true. Each var should be in the form of integers.
    :return:
    """
    import math as m
    s = []
    row = []
    for i in range(len(true_vars)):
        row.append(str(int(true_vars[i]) % 10))
        if (i + 1) % 9 == 0:
            s.append(row)
            row = []

    correct = True
    for i in range(len(s)):
        for j in range(len(s[0])):
            for x in range(len(s)):
                if i != x and s[i][j] == s[x][j]:
                    correct = False
                    print("Repeated value in column:", j, ':' ,s[i][j])
            for y in range(len(s[0])):
                if j != y and s[i][j] == s[i][y]:
                    correct = False
                    print("Repeated value in row:", i, ':' ,s[i][j])
            top_left_x = int(i-i%m.sqrt(len(s)))
            top_left_y = int(j-j%m.sqrt(len(s)))
            for x in range(top_left_x, top_left_x + int(m.sqrt(len(s)))):
                for y in range(top_left_y, top_left_y + int(m.sqrt(len(s)))):
                    if i != x and j != y and s[i][j] == s[x][y]:
                        correct = False
                        print("Repeated value in cell:", (top_left_x, top_left_y))
    return correct

def add_to_lit_dict(lit, data):
    literals = data['literals']
    
    if(lit[0]=='-'):
        lit = lit[1:]
        sign = -1
    else:
        sign = 1
    if lit not in literals:
        literals[lit] = {'occ':[], 'value':0}
        data['lit_list'].append(lit)
    literals[lit]['occ'].append((data['clause_counter'], sign))

def add_clauses(dimacs, data):
    clauses = data['clauses']
    indices = data['indices']
    
    for line in dimacs.split('\n'):
        clause = []
        for lit in line.split():
            if lit == 'p': break
            if lit != '0':
                clause.append(lit)
                add_to_lit_dict (lit, data)
            else:
                clauses.append(clause)
                indices.append(data['clause_counter'])
                data['clause_counter'] += 1

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
    indices = data['indices']
    literals = data['literals']
    
    indices.remove(ind)
    for lit in literals:
        toremove = []
        for tup in literals[lit]['occ']:
            if tup[0] == ind:
                toremove.append(tup)
        for tup in toremove:
            literals[lit]['occ'].remove(tup)

def find_tautologies(data):
    literals = data['literals']
    prev_ind = -1
    prev_signs = []
    for lit in data['lit_list']:
        for (ind, sign) in literals[lit]['occ']:
            if ind != prev_ind:
                prev_signs = [sign]
                prev_ind = ind
            elif sign*-1 in prev_signs:
                satisfied(ind, data)
            else:
            	prev_signs.append(sign)

def is_pure(lit, data):
    lit_list = data['literals'][lit]['occ']
    sign_list = [x[1] for x in lit_list]
    if sign_list == []:
        return False, 'joe'
    isTrue = all(x == sign_list[0] for x in sign_list)
    return isTrue, sign_list[0]

def find_pure_literals(data):
    found = False
    literals = data['literals']
    for lit in data['lit_list']:
        pure, sign = is_pure(lit, data)
        if pure:
            set_lit(lit, sign, data)
            return True
    return found

def get_sign_and_lit(atom):
    if atom[0] == '-':
        sign = -1
        lit = atom[1:]
    else:
        sign = 1
        lit = atom
    return sign, lit

def is_unit(ind, data):
    clause = data['clauses'][ind]
    literals = data['literals']
    f_num = 0
    num = len(clause)
    for atom in clause:
        sign, lit = get_sign_and_lit(atom)
        val = literals[lit]['value']
        if sign != val and val != 0:
            f_num += 1
        elif val == 0:
            unsat = atom
        else:
            return False, 'joe'
    if f_num == (num-1):
        return True, unsat
    return False, 'joe'

def find_unit_clauses(data):
    clauses = data['clauses']
    for ind in data['indices']:
        clause = clauses[ind]
        if len(clause)==1:
            atom = clause[0]
            sign, lit = get_sign_and_lit(atom)
            set_lit(lit, data, sign)
            return True
        else:
            unit, atom = is_unit(ind, data)
            if unit:
                sign, lit = get_sign_and_lit(atom)
                set_lit(lit, data, sign)
                return True
    return False

def get_formula(data):
    return [data['clauses'][i] for i in data['indices']]
    
def check_clauses(lit, data):
    global failed_clauses, total, bar
    tup_list = data['literals'][lit]['occ']
    ind_list = [x[0] for x in tup_list]
    for ind in ind_list:
        clause = data['clauses'][ind]
        n = len(clause)
        b = 0
        for atom in clause:
            sign, lit = get_sign_and_lit(atom)
            if sign == data['literals'][lit]['value']:
                satisfied(ind, data)
                prog = total - len(data['indices'])
                bar.update(prog)
            elif data['literals'][lit]['value'] != 0:
                b += 1
        if b == n:
            failed_clauses.append(ind)

def empty_clause(data):
    for clause in data['clauses']:
        if clause == []: return True

def set_lit(lit, data, sign):
    global performance_score
    performance_score += 1
    data['literals'][lit]['value'] = sign
    if lit in data['lit_list']: 
        data['lit_list'].remove(lit)
    check_clauses(lit, data)
    
# clauses literals indices lit_list clause_counter
def copy_data(data):
    new_clauses = [x for x in data['clauses']]
    new_indices = [x for x in data['indices']]
    new_lit_list = [x for x in data['lit_list']]
    new_clause_counter = data['clause_counter']
    new_literals = {}
    literals = data['literals']
    for lit in literals:
        new_literals[lit] = {'occ':[], 'value':0}
        for tup in literals[lit]['occ']:
            new_literals[lit]['occ'].append(tup)
        new_literals[lit]['value'] = literals[lit]['value']
    return {'clauses': new_clauses, 'literals':new_literals, 'indices':new_indices, 'lit_list':new_lit_list, 'clause_counter':new_clause_counter}

def num_unsatisfied(clause, literals):
	num = 0
	for lit in clause:
		if literals[lit]['value']==0:
			num+=1
	return num

def Dynamic_switch_heuristic(data, threshold=10):
    global failed_clauses
    n = len(failed_clauses)
    if (n < threshold):
        lit = JW_heuristic(data)
    else:
        lit = Conflict_heuristic(data)
    return lit

def JW_heuristic(data):
	weights = {}
	clauses = data['clauses']
	for ind in data['indices']:
		clause = clauses[ind]
		
		for lit in clause:
			if lit in data['lit_list']:
				leng = num_unsatisfied(clause, data['literals'])
				if lit in weights:
					weights[lit] += (2 ** (-leng))
				else: 
					weights[lit] = (2**(-leng))

	lit = max(weights, key=weights.get)
	maxi= max(weights.values())
	if len([k for (k, v) in weights.items() if v == maxi]) >1:
		lit = random.choice([k for (k, v) in weights.items() if v == maxi])
	return lit

def Conflict_heuristic(data):
    weights = {}
    global failed_clauses
    if failed_clauses == []:
        return random.choice(data['lit_list'])
    for ind in failed_clauses:
        clause = data['clauses'][ind]
        for lit in clause:
            if lit in data['lit_list']:
                if lit in weights:
                    weights[lit]+=1
                else:
                    weights[lit] = 1
    if bool(weights) == False:
        return random.choice(data['lit_list'])                                                                                                                                                                                                 
    lit = max(weights, key=weights.get)
    maxi= max(weights.values())
    if len([k for (k, v) in weights.items() if v == maxi]) >1:
        lit = random.choice([k for (k, v) in weights.items() if v == maxi])
    return lit

def dpll(data, heuristic, threshold):
    if data['indices'] == []:
        return True, data

    if empty_clause(data): return False

    find_tautologies(data)
    while(find_pure_literals(data)):
        pass

    while(find_unit_clauses(data)):
        pass

    if data['indices'] == []:
        return True, data

    try:
        global call_heuristic
        call_heuristic+=1
        if heuristic == "RAND":
            lit = random.choice(data['lit_list'])
        if heuristic == "JW":
            lit = JW_heuristic(data)
        if heuristic=="Conflict":
        	lit = Conflict_heuristic(data)
        if heuristic == "SWITCH":
            lit = Dynamic_switch_heuristic(data, threshold)

    except:
        return False, "joe"

    data_true = copy_data(data)
    set_lit(lit, data_true, -1)

    succ, data_true = dpll(data_true, heuristic, threshold)
    if succ:
        return succ, data_true

    data_false = copy_data(data)
    set_lit(lit, data_false, 1)
    succ, data_false = dpll(data_false, heuristic, threshold)
    if succ: 
        return succ, data_false
    
    return False, "joe"
    
def solve(clauses, heur, threshold):
    global performance_score, call_heuristic, failed_clauses, bar, total

    data_dict = {'clauses':[], 'literals':{}, 'indices':[], 'lit_list':[], 'clause_counter':0}
    performance_score = 0
    call_heuristic=0

    failed_clauses = []

    add_clauses(clauses, data_dict)

    total = len(data_dict['clauses'])

    bar = progressbar.ProgressBar(max_value=total) 

    succ, data = dpll(data_dict, heur, threshold)

    return succ, data, performance_score, call_heuristic


 