######################################
# submited by
# 1. Meseret Dereje GSR/4274/13
# 2. Sebah Tewodros GSR/8418/13
# 3. Tinbilina Gashaw GSR/5005/13
#####################################
import math
import csv
import scipy.stats as stats
      
def seedLCG(initVal): 
    global rand
    rand = initVal
def lcg(): #function to find random number U between 1 and 0 using Linear congruential generators
    a = 1764525
    c = 0 
    m = 2**31
    global rand
    rand = (a*rand + c) % m
    return rand / m
seedLCG(1)
global RA  
RA =[]
def expontial_random_variable(mean_value): #function to generate the random expontialy distribuuted variable 
        
        random_number = lcg() #calling the random number gnerating function
        ERV= (-1/mean_value)*math.log(random_number)
        RA.append(ERV)
    
def Chi_Square():
 
    stat, p, dof, expected = stats.chi2_contingency(RA) 
  
    # interpret p-value 
    alpha = 0.05
    print("p value is " + str(p)) 
    if p <= alpha: 
      print('Dependent (reject H0)') 
    else: 
       print('Independent (H0 holds true)') 

         


# with open('Rabdom_variables.csv', mode='w') as random_variable: #opening the CSV file       
#       w = csv.writer(random_variable)
#       w.writerow(['U', 'X']) # writing the header in the csv file

for i in range(1000):
    expontial_random_variable(3) #calling the random number gnerating function

Chi_Square()
# print( RA)

        #   w.writerow([RVV.random_number,RVV.ERV,]) # writing the genrated numbers and variables in  the csv file 
