import pickle
import numpy as np
import glob, os
import seaborn as sns
import matplotlib.pyplot as plt
import statistics
from scipy.interpolate import spline



levels = ['very_easy', 'easy', 'med', 'hard', 'very_hard']
N = ['10', '15', '25', '50', '75']
switch_results = {}

overall = []
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
    overall.append(round(np.mean(flat)))



def line_plot(a, b, c, d, e, f):

	N = [10 , 15, 25, 50, 75]
	T = np.array(N)
	xnew = np.linspace(T.min(),T.max(),200) #300 represents number of points to make between T.min and T.max
	print(a)
	power_smooth1 = spline(T,a,xnew)

	power_smooth2 = spline(T,b,xnew)

	power_smooth3 = spline(T,c,xnew)

	power_smooth4 = spline(T,d,xnew)

	power_smooth5 = spline(T,e,xnew)

	
	fig = plt.figure()
	fig.set_size_inches(7, 5)

	ax = fig.add_subplot(111)
	ax.yaxis.grid(zorder=0)
	plt.title("Effect of N on performance")
	plt.ylabel('Average number of calls')
	plt.xlabel('Hyper parameter N ')
	plt.xticks(N)
	plt.yticks(np.arange(0, 100, 10))

	'''
	plt.plot(xnew, power_smooth1,'LightSeaGreen', label="Very easy") # plotting t, a separately 
	plt.plot(xnew, power_smooth2, 'LightSkyBlue', label="Easy") # plotting t, b separately  
	plt.plot(xnew, power_smooth3, 'LightSlateGrey', label="Medium")
	plt.plot(xnew, power_smooth4, 'g', label="Hard")
	plt.plot(xnew, power_smooth5, 'r', label="Very hard")
	'''
	print(a, b, c, d, e)
	plt.plot(N, a, 'firebrick',  marker='o', lw=3, label="Very easy") # plotting t, a separately 
	plt.plot(N, b, '#ff8c00',  marker='o',lw=3, label="Easy") # plotting t, b separately  
	plt.plot(N, c,  '#008b8b',  lw=3, marker='o',label="Medium")
	plt.plot(N, d, '#8b008b',  marker='o',lw=3,label="Hard")
	plt.plot(N, e, '#00008b', marker='o', lw=3,label="Very hard")
	plt.plot(N, f, 'LightSlateGrey',marker= 'o',ls='--', lw=2.8,label='All categories')

	lgd = plt.legend(loc='best', bbox_to_anchor=(0.64, 0.64))
	plt.show()

rs = []
for i in levels:
    avg = []
    for j in N:
        with open("scores/"+i+"_sudokus_SWITCH_"+j+".pckl", 'rb') as f: 
            dat = pickle.load(f)
        calls = dat[1]
        avg.append(round(np.mean(calls)))
    rs.append(avg)

a = rs[0]
b = rs[1]
c = rs[2]
d = rs[3]
e = rs[4]

line_plot(a, b, c, d, e, overall)

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
	c = ['darkred', 'darkorange', 'darkcyan',  'darkmagenta', 'darkblue' ]
	plt.title('Violin plots for the switching strategy with N=50')
	ax = sns.violinplot(data=results, palette=c, bw=0.3, cut= 0, scale='width', saturation=0.8)
	#ax = sns.boxplot(data=results, palette=c)

	ax.set_xticklabels(x_labels)
	ax.set_ylabel('Average number of calls')
	plt.tight_layout()
	plt.show()

def plot_histogram(c1, m, s):
	r1 = c1[0]

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
	    

	ax.set_ylabel('Average number of calls')
	ax.yaxis.set_ticks(np.arange(0, m, s))
	ax.set_xlabel('Difficulty category')

	ax.set_xticks(ind+width)
	ax.set_xticklabels( ('very easy', 'easy', 'medium', 'hard', 'very hard') )
	plt.legend( loc="upper right")
	plt.title("Switching strategy performances")

	def autolabel(rects):
	 
	    n = 0
	    for rect in rects:
	        height = rect.get_height()
	        ax.text(rect.get_x() + rect.get_width()/2., (height+0.4),
	                 "Avg. "+str( int(round(height+0.5))) ,
	                ha='center', va='bottom')
	        n+=1

	autolabel(rects1)


	box = ax.get_position()
	ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

	ax.legend((rects1[0], 
	            ('Switch') ))
	plt.tight_layout()
	plt.show()

switch_results = {}

for i in levels:
    	with open("scores/"+i+"_sudokus_SWITCH_50.pckl", 'rb') as f: 
    		dat = pickle.load(f)
    		switch_results[i] = dat
    


print("Switch")
scores, calls= get_dict(switch_results)


#plot_histogram(calls, 160, 10)

data = []
for i in levels:
	r = switch_results[i][1]
	r = [x for x in r if x!=0 and (x<150)]
	r = np.asarray(r)
	m = r.max()
	r = [x for x in r if x != m]
	print(len(r))
	data.append(r)

plot_violin(data)
