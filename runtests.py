from SATSolver import *
import sys

heurs = ['RAND', 'JW', "Conflict"]
N = [10, 15,25, 50, 75]

# if len(sys.argv) != 2:
#     print('Usage: runtests.py index of N list [10, 15,25, 50, 75]')
#     exit()
# elif int(sys.argv[1]) not in range(5):
#     print('Usage: runtests.py index of N list [10, 15, 25, 50, 75]')
#     exit()
# else:
#     t = N[int(sys.argv[1])]
heur = 'SWITCH'
# heur = 'Conflict'
# heur = 'JW'

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
    for t in N:
        sudokus = difficulties[diff]
        datas = []
        scores = []
        calls = []
        for i in range(len(sudokus)):
            print(diff, 'N:', t, i+1,'/',len(sudokus))

            sudoku_nr = i

            clauses = rules + sudokus[i]
            succ, data, performance_score, call_heuristic = solve(clauses, heur, t)

            if succ:
                true_lits = []
                for lit in data['literals']:
                    if data['literals'][lit]['value'] == 1:
                        true_lits.append(int(lit))

                #print_sudoku(true_lits)
                check_sudoku(true_lits) 
                print("\nPerformance score = ", performance_score)
                print("Calls to heuristic = ", call_heuristic)

                scores.append(performance_score)
                calls.append(call_heuristic)
            else:
                print("\n---------------------------------------not solvable---------------------------------------------")

        results = [scores, calls]

        f = open('scores/'+diff+'_'+heur+'_'+str(t)+'.pckl', 'wb')
        pickle.dump(results, f)
        f.close()
