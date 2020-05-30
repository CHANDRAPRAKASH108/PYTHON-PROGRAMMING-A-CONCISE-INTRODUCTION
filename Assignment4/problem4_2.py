import random
numList = []
random.seed(150)
for i in range(0,25):
    numList.append(round(100*random.random(),1))  
def problem4_2(ran_list):
    import statistics
    """ Compute the mean and standard deviation of a list of floats """
    print(statistics.mean(ran_list))
    print(statistics.stdev(ran_list))