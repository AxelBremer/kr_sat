import pickle
import numpy as np
import glob, os
import seaborn as sns
import matplotlib.pyplot as plt
import statistics


levels = ['very_easy', 'easy', 'med', 'hard', 'very_hard']
N = ['10', '15', '25', '50', '75']
switch_results = {}

for j in N: 
    print("N = ", j)
    results = []
    for i in levels:
    	with open("scores/"+i+"_sudokus_SWITCH_"+j+".pckl", 'rb') as f: 
    		dat = pickle.load(f)
    	calls = dat[1]
    	results.append(calls)
    flat = [y for x in results for y in x]
    print(round(np.mean(flat)))
    print(np.std(flat))


results = []
for i in levels: 
    print(i)
    with open("scores/"+i+"_sudokus_SWITCH_50.pckl", 'rb') as f: 
        dat = pickle.load(f)
    print(round(np.mean(dat[1])))

def get_dict(heur_dict):
	scores = []
	calls = []
	calls_std = []
	for key in heur_dict:
		value = heur_dict[key]
		print(len(value[0]), len(value[1]))
		s = np.mean(value[0])
		sd = np.mean(value[0])
		c = np.mean(value[1])
		cd = statistics.stdev(value[1])
		print(key, "scores", s, "calls", c)
		scores.append(s)
		calls.append(c)
		calls_std.append(cd)
	return scores, (calls, calls_std)

def plot_violin(results):
	sns.set(style="whitegrid") 
	y_labels = ["Average number of calls"]
	x_labels = ['very easy', 'easy', 'medium', 'hard', 'very hard']
	ax = sns.violinplot(data=results, palette="muted", split=True)
	#ax = sns.boxplot(data=results, palette="muted")

	ax.set_xticklabels(x_labels)
	plt.show()

def plot_histogram(c1, c2, c3, m, s):
	r1 = c1[0]
	r2 = c2[0]
	r3 = c3[0]

	N = 5
	ind = np.arange(N)  
	width = 0.3     
	fig = plt.figure()
	fig.set_size_inches(11, 6)

	ax = fig.add_subplot(111)
	ax.yaxis.grid(zorder=0)

	pal = sns.color_palette('muted',10)
	colorp = pal.as_hex()


	rects1 = ax.bar(ind, r1, width, alpha=1, color= '#ff8c00', zorder=3)
	    
	rects2 = ax.bar(ind+width, r2, width, alpha=1, color= '#008b8b', zorder=3)

	rects3 = ax.bar(ind+width*2, r3, width, alpha=1, color='#8b008b', zorder=3)
	    

	ax.set_ylabel('Average number of calls')
	ax.yaxis.set_ticks(np.arange(0, m, s))
	ax.set_xlabel('Difficulty category')

	ax.set_xticks(ind+width)
	ax.set_xticklabels( ('very easy', 'easy', 'medium', 'hard', 'very hard') )
	plt.legend( (rects1[0], rects2[0], rects3[0]), 
	          ('RAND', 'JW', 'Conflict') , loc="upper right")
	plt.title("Branching heuristic performances")

	def autolabel(rects):
	 
	    n = 0
	    for rect in rects:
	        height = rect.get_height()
	        ax.text(rect.get_x() + rect.get_width()/2., (height+0.4),
	                 "Avg. "+str( int(round(height+0.5))) ,
	                ha='center', va='bottom')
	        n+=1

	autolabel(rects1)
	autolabel(rects2)
	autolabel(rects3)

	box = ax.get_position()
	ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

	ax.legend((rects1[0], rects2[0], rects3[0]), 
	            ('RAND', 'JW', 'Conflict') )
	plt.tight_layout()
	plt.show()
'''
print("Random")
scoresr, callsr= get_dict(rand_results)
print("JW")
scoresj, callsj = get_dict(jw_results)
print("Conflict")
scoresc, callsc = get_dict(conflict_results)


plot_histogram(callsr, callsj, callsc, 160, 10)
plot_histogram([scoresr], [scoresj], [scoresc], 8500, 200)

data = []
for i in levels:
	data.append(jw_results[i][1])

plot_violin(data)
'''