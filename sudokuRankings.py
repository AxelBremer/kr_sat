from recordtype import recordtype
import pdb
import copy
import random
import time
import progressbar
import pickle

def check_difficulty(data, n):
    easy = []
    very_easy = []
    med = []
    hard = []
    very_hard = []
    for file in data:
        for line in file.split('\n'):
            if line == "": break
            ct = 0
            clue = 0
            for i in range(1,10):
                for j in range(1,10):
                    if line[ct] != '.':
                        clue+=1
                    ct+=1
            if(clue <=17):
                very_hard.append(line)
            elif(clue >= 19 and clue <=21):
                hard.append(line)
            elif(clue >= 23 and clue <=25):
                med.append(line)
            elif(clue>=31):
                very_easy.append(line)
            elif(clue >=27 and clue <=29):
                easy.append(line)
    print(len(easy), len(med), len(hard))
    return hard[:n], med[:n], easy[:n], very_easy[:n], very_hard[:n]
    
def write_to_file(sudokus, cat):
    output = open(cat+'_sudokus.txt', 'w')
    for i in sudokus:
        output.write(i)
        output.write("\n")
    output.close()


with open("test sudokus/1000 sudokus.txt") as file:
    dat1 = file.read()
with open("test sudokus/damnhard.sdk.txt") as file:
    dat2 = file.read()
with open("test sudokus/subig20.sdk.txt") as file:
    dat3 = file.read()
with open("test sudokus/top91.sdk.txt") as file:
    dat4 = file.read()
with open("test sudokus/top95.sdk.txt") as file:
    dat5 = file.read()
with open("test sudokus/top100.sdk.txt") as file:
    dat6 = file.read()
with open("test sudokus/top870.sdk.txt") as file:
    dat7 = file.read()
with open("test sudokus/top2365.sdk.txt") as file:
    dat8 = file.read()

sudokus = [dat1, dat2, dat3, dat4, dat5, dat6, dat7, dat8]

hard, med, easy, very_easy, very_hard = check_difficulty(sudokus, 200)
write_to_file(hard, "hard")
write_to_file(med, "med")
write_to_file(easy, "easy")
write_to_file(very_easy, "very_easy")
write_to_file(very_hard, "very_hard")

