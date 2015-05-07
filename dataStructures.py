__author__ = 'nimish'

#!/usr/bin/env python

# import modules used here
import sys
import numpy as np
from numpy.linalg import inv


def findInv():
    a = np.array([[1, 2, 3],[4, 5, 6], [7, 8, 9]])
    
    # Raising power of array to 2
    aRaised2 = np.power(a,2)

    # Finding inverse of array
    aInv =  np.linalg.inv(aRaised2)
    
    # Filtering array based on value=25
    aRaised2flat = aRaised2.flatten()
    filteredList = [i for i in aRaised2flat if i > 25]    
    
    print aRaised2
    print aInv
    print filteredList
    return

def DS():
	'''
	for flattening list  

	list1 = reduce(lambda x,y: x+y,list_of_list)  
	list2 = sum(list_of_list, [])
	list3 = [item for sublist in list_of_list for item in sublist]  - fastest way
	
	'''
	list_of_list = [[1,2,3,4,5],[10,20,30,40],[6,12,18,24]]
	reversed_lists = [list(reversed(x)) for x in list_of_list]
	print reversed_lists

	flat_list = reduce(lambda x,y: x+y,list_of_list)
	squared_list = map(lambda x: x*x , flat_list)
	print squared_list

	filter_list = filter(lambda x: x > 25 , squared_list)
	print filter_list
	
	return
def main():
	#findInv()
	DS()
	print 'end of main function'


if __name__ == '__main__':
	main()