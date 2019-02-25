from SATSolver import *
import sys

heurs = ['RAND', 'JW', "Conflict"]

if len(sys.argv) != 2:
    print('Usage: runtests.py RAND|JW')
    exit()
elif sys.argv[1] not in heurs:
    print('Usage: runtests.py RAND|JW')
    exit()
else:
    heur = sys.argv[1]


with  open("sudoku-rules.txt") as file:
    rules = file.read()

difficulties = {}
with open("very_easy_sudokus.txt") as file:
    dat = file.read()
difficulties['very_easy_sudokus'] = to_dimacs(dat)
with open("easy_sudokus.txt") as file:
    dat = file.read()
difficulties['easy_sudokus'] = to_dimacs(dat)
with open("med_sudokus.txt") as file:
    dat = file.read()
difficulties['med_sudokus'] = to_dimacs(dat)
with open("hard_sudokus.txt") as file:
    dat = file.read()
difficulties['hard_sudokus'] = to_dimacs(dat)
with open("very_hard_sudokus.txt") as file:
    dat = file.read()
difficulties['very_hard_sudokus'] = to_dimacs(dat)

for diff in difficulties:
    print(diff)
    sudokus = difficulties[diff]
    datas = []
    scores = []
    calls = []
    for i in range(len(sudokus)):
        print(i,'/',len(sudokus))

        sudoku_nr = i

        clauses = rules + sudokus[i]
    #     add_clauses("111 0\n 167 0 \n 189 0\n 223 0\n 252 0\n 298 0\n 339 0\n 346 0 \n 375 0\n 435 0\n 443 0\n 479 0\n 521 0\n 558 0\n 592 0\n 616 0\n 664 0\n 713 0\n 781 0\n 824 0\n 831 0\n 897 0\n 937 0\n 973 0\n", data_tuple)

        succ, data, performance_score, call_heuristic = solve(clauses, heur)

        if succ:
            true_lits = []
            for lit in data['literals']:
                if data['literals'][lit]['value'] == 1:
                    true_lits.append(int(lit))

            #print_sudoku(true_lits)
            check_sudoku(true_lits) 
            print("Performance score = ", performance_score)
            print("Calls to heuristic = ", call_heuristic)

            scores.append(performance_score)
            calls.append(call_heuristic)
        else:
            print("not solvable")

    results = [scores, calls]
    '''
    f = open('scores/'+diff+'_'+heur+'.pckl', 'wb')
    pickle.dump(results, f)
    f.close()
    '''