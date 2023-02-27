# python3

import sys
import threading
import numpy as np

def compute_height(n, parents):
    max_height = 0

    #rewrite from list to numpy array !!!, tests 21-25???

    par_split = parents.split()
    #par_split = map(int, par_split)
    #par_split = list(par_split)
    par_split = np.array(list(map(int, par_split)))
    #print(par_split)

    for x in par_split:
        current_h = 1
        curr = x
        while curr > -1:
            curr = par_split[curr]
            #print(curr)
            current_h += 1
        if current_h > max_height :
            max_height = current_h
    
    return max_height

def main():
    text = input()
    if 'F' in text and not 'a' in text:
        file_name = input()
        file = "./test/" + file_name
        #print(file)
        with open(file) as f:
            num = f.readline()
            text = f.readline()
    if 'I' in text:
        num = input()
        text = input()
    
    print(compute_height(num, text))
    #print(num)
    #print(text)



# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
