from pvt_class import pvt  #the class the holds all PVT functions and solutions
import presentation #the class the helps with presenting the result of the solution

#converting the data into a dictionary data structure
candidates = {
    'alice' : ['x', 10, 92, 23, 17, 2, 44, 33, 41, 19, 54],
    'bob'   : ['x', 21, 91, 10, 9, 12, 21, 52, 18, 34, 78],
    'carol' : ['x', 10, 81, 8, 28, 53, 53, 10, 11, 40, 36],
    'dave'  : ['x', 48, 12, 40, 30, 33, 37, 81, 29, 28, 32],
    'eli'   : ['x', 12, 9, 21, 44, 13, 17, 21, 34, 33, 62]
    }


poll = pvt(candidates)
poll.pvt_solution()
