# Tamsin Rogers
# October 9, 2019
# CS 152 
# Project 6: Optimizing the Simulation
# run this program from the Terminal by entering "python3 testoptimize.py [adultprob/calfprob/seniorprob/calv/maxage]"
# this program automates the process of evaluating the effects of the selected parameter on the dart percentage

import optimize					#import optimize.py
import elephant					#import elephant.py

"""This function returns the value (x - target)"""
def target(x, pars):
    return x - 0.73542618

"""This function tests the binary search using a simple target function."""
# Try changing the tolerance to see how that affects the search.
def testTarget():
    res = optimize.optimize( 0.0, 1.0, target, tolerance = 0.1, verbose=True)
    print(res)
    return

if __name__ == "__main__":
    testTarget()
    #evalParameterEffect( elephant.IDXadultprob, 0.98, 1.0, 0.001, verbose=True )	#CHANGE THIS TO main(sys.argv) EVENTUALLY