# Tamsin Rogers
# October 9, 2019
# CS 152 
# Project 6: Optimizing the Simulation
# run this program from the Terminal by entering "python3 optimize.py"
# this program executes a search to bring the result of the function optfunc to zero

import elephant                 #import elephant.py
import random                   #import the random package
import matplotlib.pyplot as plt #import the matplotlib package


"""This function executes a search to bring the result of the function optfunc to 0."""
# Executes a search to bring the result of the function optfunc to zero.
# min: minimum parameter value to search
# max: maximum parameter value to search
# optfunc: function to optimize
# parameters: optional parameter list to pass to optfunc
# tolerance: how close to zero to get before terminating the search
# maIterations: how many iterations to run before terminating the search
# verbose: whether to print lots of information or not
def optimize(minimum, maximum, optfunc, parameters = None, tolerance = 0.001, maxIterations = 20, verbose=True ):
    done = False                                        #assign done to the value False
    while done == False:                                #start a loop that continues while done is equal to False
        #print("types", type(minimum), type(maximum))                      
        testValue = (minimum+maximum)/2                 #assigns to testValue the average of max and min
        print(testValue)                                #print testValue
        result = optfunc(testValue, parameters)         #assign to result the return value of calling optfunc with testValue and parameters as the arguments
        if verbose == True:                             #if verbose is True
            print(result)                               #print the result value
        if result>0:                                    #if the result is positive
            maximum = testValue                         #assign to max the value of testValue
        elif result<0:                                  #else if the result is negative
            minimum = testValue                         #assign to min the value of testValue
        else:
            done = True                                 #assign to done the value True
        if (maximum-minimum)<tolerance:                 #if (max-min) is less than the tolerance value
            done = True                                 #assigns to done the value True
        maxIterations = maxIterations -1 
        if maxIterations <= 0:
            done = True
    return testValue                            

"""This function tests the optimize function with the elephantSim function.  It finds a value
close to 0.43 for the percent darted."""    
def testEsim():
    test = optimize(0.0, 0.5, target, tolerance = 0.1, verbose=True)
    print(test)
    return
    
"""This function automates the process of evaluating the effects of changing a simulation 
parameter across a range of values."""
# Evaluates the effects of the selected parameter on the dart percentage
# whichParameter: the index of the parameter to test
# testmin: the minimum value to test
# testmax: the maximum value to test
# teststep: the step between parameter values to test
# defaults: default parameters to use (default value of None)
def evalParameterEffect( whichParameter, testmin, testmax, teststep, defaults=None, verbose=False ):
    if defaults == None:                                        # if defaults is None, assign to simParameters the result of calling elephant.defaultParameters.
        simParameters = elephant.defaultParameters()
    else:                                                       # else, assign to simParameters a copy of defaults  (e.g. simParameters = defaults[:]
        simParameters = defaults[:]
    results= []                                                 # create an empty list (e.g. results) to hold the results
    if verbose:
        print("Evaluating parameter %d from %.3f to %.3f with step %.3f" % (whichParameter, testmin, testmax, teststep))
    t = testmin                                                 # assign to t the value testmin
    while (t<testmax):                                          # while t is less than testmax
        simParameters[whichParameter] = t                       # assign to the whichParameter element of simParameters (e.g. simParameters[whicParameter]) the value t
        percDart = optimize(testmin, testmax, elephant.elephantSim, simParameters, tolerance = 0.001, maxIterations = 20, verbose=False)    # assign to percDart the result of calling optimize with the appropriate arguments, including simParameters
        #print("percDart", percDart)
        addthis = (t, percDart)
        results.append(addthis)                                 # append to results the tuple (t, percDart)
        t = (t+teststep)                                        #increment t by teststep
        #print("t", t)
        #print("teststep", teststep)
        #print("testmax", testmax)
    if verbose:
        print("final test value:   optimal percentage darted:")
        print ("%8.3f \t%8.3f" % (t, percDart))
    if verbose:
        print("Terminating")
    symbols = ["ro", "bo", "r+", "b", "-g", "--", "^k", "co"]   #create a list of possible plot symbols
    symbol = random.choice(symbols)                             #randomly select a matplotlib symbol for the graph
    plt.plot(t, percDart, symbol)                               #set up a matplotlib graph with x=t, y=percDart
    plt.xlabel("t")
    plt.ylabel("percDart")
    plt.annotate(("point = ", percDart), (t,percDart), textcoords="offset points", xytext=(0,50), ha='center')  #display the value of the percDart data above the point
    fp = open("optimizeddata.csv", 'w' )                                                           #creates a new csv file
    fp.write("Test Value (t)" + "," + "Optimal Percentage Darted (percDart)" + "\n")    #writes headers
    
    for i in (results):
        data1 = addthis[0]#assigns the values in the first column of data to data1
        data2 = addthis[1]
        # print (or save to a file) the day of the month and thermo_depth separated by a comma
        fp.write((str(data1) + "," + str(data2)) + "\n")
    return(results)                                             # return the list of results

def main():
    answer = input("This program shows the effect on the dart percentage of the following parameter sweeps: adult survival probability, calf survival probability, senior survival probability, calving interval, and max age.  Which would you like to evaluate?  (Enter adultprob, calfprob, seniorprob, calv, or maxage).")
    thetitle = "title"
    if answer == "adultprob":                                                            #if the input is adultprob (adult survival probability)
        evalParameterEffect(elephant.IDXadultprob, 0.98, 1.0, 0.001, verbose=True )     #run evalParameterEffect with the appropriate arguments
        thetitle = "Adult Survival Probability Varied from 0.98 to 1.0 in Steps of 0.001"  #set the plot title
    if answer == "calfprob":                                                             #if the input is calfprob (calf survival probability)
        evalParameterEffect(elephant.IDXcalfprob, 0.80, 0.90, 0.01, verbose=True )      #run evalParameterEffect with the appropriate arguments
        thetitle = "Calf Survival Probability Varied from 0.80 to 0.90 in Steps of 0.01"   #set the plot title
    if answer == "seniorprob":                                                           #if the input is seniorprob (senior survival probability)
        evalParameterEffect(elephant.IDXseniorprob, 0.1, 0.5, 0.05, verbose=True )      #run evalParameterEffect with the appropriate arguments
        thetitle = "Senior Survival Probability Varied from 0.1 to 0.5 in Steps of 0.05"   #set the plot title
    if answer == "calv":                                                                 #if the input is calv (calving interval)
        evalParameterEffect(elephant.IDXcalv, 3.0, 3.4, 0.05, verbose=True )            #run evalParameterEffect with the appropriate arguments
        thetitle = "Calving Interval Varied from 3.0 to 3.4 in Steps of 0.05"              #set the plot title
    if answer == "maxage":                                                               #if the input is maxage (max age)
        evalParameterEffect(elephant.IDXmaxage, 56, 66, 2, verbose=True )               #run evalParameterEffect with the appropriate arguments
        thetitle = "Max Age Varied from 56 to 66 in Steps of 2"                            #set the plot title
    #elif answer is not "adultprob" or "calfprob" or "seniorprob" or "calv" or "maxage":
        #print("Enter one of the follow: adultprob, calfprob, seniorprob, calv, maxage.")

    plt.title(thetitle) #reset the title of the graph to its appropriate valule
    plt.show()          #display the graph

if __name__ == "__main__":
    main()