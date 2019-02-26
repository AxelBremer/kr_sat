import pickle
import numpy as np
import glob, os
import seaborn as sns
import matplotlib.pyplot as plt


levels = ['very_easy', 'easy', 'med', 'hard', 'very_hard']
heurs = ['RAND', 'JW']
rand_results = {}
jw_results = {}
conflict_results = {}
for i in levels:
    for j in heurs:
    	with open("scores/"+i+"_sudokus_"+j+".pckl", 'rb') as f: 
    		dat = pickle.load(f)
    	if(j == "RAND"):
    		rand_results[i] = dat
    	if(j == "JW"):
    		jw_results[i] = dat
    	elif(j=="Conflict"):
    		conflict_results[i] = dat


def get_dict(heur_dict):
	scores = []
	calls = []
	for key in heur_dict:
		value = heur_dict[key]
		s = np.mean(value[0])
		c = np.mean(value[1])
		print(key, "scores", s, "calls", c)
		scores.append(s)
		calls.append(c)
	return scores, calls



def plot_histogram(r1, r2, r3):
	N = 5
	ind = np.arange(N)  #
	width = 0.28       
	fig = plt.figure()
	fig.set_size_inches(10, 7)

	ax = fig.add_subplot(111)

	rects1 = ax.bar(ind, r1, width, alpha=1, color='#ff8c00')
	    
	rects2 = ax.bar(ind+width, r2, width, alpha=1, color='#008b8b')

	rects3 = ax.bar(ind+width*2, r3, width, alpha=1, color='#8b008b')
	    

	ax.set_ylabel('Calls')
	ax.yaxis.set_ticks(np.arange(0, 1000, 10000))

	ax.set_xticks(ind+width)
	ax.set_xticklabels( ('very easy', 'easy', 'medium', 'hard', 'very hard') )
	plt.legend( (rects1[0], rects2[0], rects3[0]), 
	          ('RAND', 'JW', 'Conflict') , loc="upper right")

	def autolabel(rects):
	    """
	    Attach a text label above each bar displaying its height
	    """
	    for rect in rects:
	        height = rect.get_height()
	        ax.text(rect.get_x() + rect.get_width()/2., 1.02*(height+0.45),
	                str(int(round(height+0.5))),
	                ha='center', va='bottom')
	        
	autolabel(rects1)
	autolabel(rects2)
	autolabel(rects3)

	box = ax.get_position()
	ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

	ax.legend((rects1[0], rects2[0], rects3[0]), 
	            ('RAND', 'JW', 'Conflict') )


	lgd = ax.legend((rects1[0], rects2[0], rects3[0]), 
	            ('RAND', 'JW', 'Conflict'))
	plt.tight_layout()
	plt.show()

print("Random")
scoresr, callsr = get_dict(rand_results)
print("JW")
scoresj, callsj = get_dict(jw_results)

plot_histogram(np.asarray(callsr), np.asarray(callsj), np.asarray(callsj))