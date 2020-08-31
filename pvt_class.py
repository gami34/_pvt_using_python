import math
from pprint import pprint



class pvt :
    '''
this is a class that help handles all needed pvt functions 
    '''
    def  __init__(self, dictionary):
        # contructor of the poll instance 
        self.dictionary = dictionary;           #vote share of each candidates
        self.k = 10                             #number of polling points
        self.f = 0                                           #fraction of voters
        self.mi = ['x'] + [0] * 10                        #list of mi
        self.mi_indexer = 1
        self.__gen_mi_list()                            #generate mi for each point i
        self.mi2 = ['x'] + [i**2 for i in self.mi[1:]]  #list of mi2
        
        
    #this helps to sum all share point of a candidate 
    def sum_ai(self, candidate):
        return sum( self.dictionary[candidate][ 1: ] )

    #this helps to sum all mi points , base on the list of generated mi for each polling point
    def sum_mi(self):
        return sum(self.mi[1:])

    #this helps to generate the list of mi for each pollng point
    def __gen_mi_list(self):
        for key in self.dictionary: 
            for i in  range(1, len(self.dictionary[key])):
                self.mi[ i ]  += self.dictionary[key][ i]
        
    #this helps get the point estimate for each candidate
    def point_est_p(self, candidate):
        total_ai = self.sum_ai(candidate)
        total_mi = self.sum_mi()
        return total_ai/total_mi

    #This is to get m prime of all sum of share points
    def m_prime(self):
        return sum(self.mi[1:])/len(self.mi[1:])

    #this is used with a mapping function in order to the list of mi * ai
    def mi_mul(self, ai):
        miai = self.mi[self.mi_indexer] * ai
        self.mi_indexer +=1
        return miai

    #this helps gets th margin error of each candidates
    def margin_error(self, candidate):
        self.mi_indexer = 1
        p = self.point_est_p(candidate)
        p2= p**2
        m_p = self.m_prime()
        m_p2 = m_p**2
        k = self.k
        f = self.f
        
        p2Emi2 = p2 * sum(self.mi2[1:])
        miai = list( map(self.mi_mul, self.dictionary[candidate][1:]) )
        pEaimi = p * sum(miai)
        
        ai2 = [ai**2 for ai in self.dictionary[candidate][1:]]
        Eai2 = sum(ai2)

        comp1 = ((1-f)*(Eai2 - (2*pEaimi) + (p2Emi2))) / (k * m_p2 * (k -1))
        
        error = math.sqrt(comp1) * 1.96 * 100

        return error

    #this if to get the vote share of each candidates
    def vote_share(self, candidate):

        total_poll = sum(self.mi[1:])
        cand_poll  = sum(self.dictionary[candidate][1:])

        return cand_poll / total_poll * 100

    #this function is called by the instance of the class
    #to generate the candidates Name, Share point and the Margin error of the result
    #by using string formatting
    def pvt_solution(self):
        print()
        print('-'*74)
        print('|{:^20s}|{:^25s}|{:^25s}|'.format(' ',' ',' '))
        print('|{:^20s}|{:^25s}|{:^25s}|'.format('Candidates','Votes Shares (%)', 'Margin Error (%)'))
        print('|{:^20s}|{:^25s}|{:^25s}|'.format(' ',' ',' '))
        for key in self.dictionary:
            print('-'*74)
            print('|{:^20s}|{:^25s}|{:^25s}|'.format(' ',' ',' '))
            print('|{:^20s}|{:>12.2f}{:13s}|{:>7s}{:5.2f}{:13s}|'.format(key.upper(), self.vote_share(key),'%','+/-', self.margin_error(key),'%'))
            print('|{:^20s}|{:^25s}|{:^25s}|'.format(' ',' ',' '))
        print('-'*74)
        
