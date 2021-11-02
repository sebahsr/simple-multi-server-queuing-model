######################################
# submited by
# 1. Meseret Dereje GSR/4274/13
# 2. Sebah Tewodros GSR/8418/13
# 3. Tinbilina Gashaw GSR/5005/13
#####################################


import math
import numpy as np
import matplotlib.pyplot as plt

class simulation:
    def __init__(self):
        
        self.num_in_queue1=0
        self.num_in_queue2=0
        self.num_in_queue3=0
        self.clock=0.0
        self.t_arrival=self.generate_interarrival()
        self.t_depart1=float('inf')
        self.t_depart2=float('inf')
        self.t_depart3=float('inf')
        self.server1=0 #0:idal 1: buisy 2:sleeping
        self.server2=0
        self.server3=0
        self.num_arrival=0
        self.num_depart1=0
        self.num_depart2=0
        self.num_depart3=0
        self.total_wait1=0.0
        self.total_wait2=0.0
        self.total_wait3=0.0
        self.responseTime1=0
        self.responseTime2=0
        self.responseTime3=0
        self.w_t1=0
        self.w_t2=0
        self.w_t3=0
        self.response1=0
        self.response2=0
        self.response3=0
	
    def advance_time(self):
        t_event=min(self.t_arrival,self.t_depart1,self.t_depart2,self.t_depart3)
        it=self.clock
        self.clock = t_event
        if self.t_arrival<=min(self.t_depart1,self.t_depart2,self.t_depart3):
            self.arrival_event()
        elif self.t_depart1<=min(self.t_arrival,self.t_depart2,self.t_depart3):
            self.departure_event1()  
            self.w_t1=self.num_in_queue1*(self.t_depart1-it)
            self.total_wait1 += self.w_t1
        elif self.t_depart2<=min(self.t_arrival,self.t_depart1,self.t_depart3):
            self.departure_event2()  
            self.w_t2=self.num_in_queue2*(self.t_depart2-it)
            self.total_wait2 += self.w_t2
        elif self.t_depart3<=min(self.t_arrival,self.t_depart1,self.t_depart2):
            self.departure_event3() 
            self.w_t3=self.num_in_queue3*(self.t_depart2-it)
            self.total_wait3 += self.w_t3
        
        
       
        
        
    def arrival_event(self):
        self.num_arrival+=1
        print("num_of_customers_arrived ",self.num_arrival)
        self.t_arrival=self.clock+self.generate_interarrival()
        if(self.num_in_queue1==0) :
            self.run_server1()
        elif (self.num_in_queue1<self.num_in_queue2 and self.num_in_queue1<self.num_in_queue3):
            self.run_server1()
        elif (self.num_in_queue2<self.num_in_queue1 and self.num_in_queue2<self.num_in_queue3):
            self.run_server2()
        elif (self.num_in_queue3<self.num_in_queue1 and self.num_in_queue3<self.num_in_queue1):
            self.run_server3()
        print("total_queue_length= ",self.num_in_queue1) 
        print("total_queue_length= ",self.num_in_queue2)
        print("total_queue_length= ",self.num_in_queue3)
    def run_server1(self):
        self.num_in_queue1+=1
        if (self.server1==0):
            self.server1=1
            self.t_depart1=self.clock+self.generate_service()
            self.response1=self.t_depart1-self.clock
            self.responseTime1+= self.response1
            self.num_in_queue1-=1
		# schedule next arrival_event
        self.t_arrival=self.clock+self.generate_interarrival()
        print("total_queue_length1= ",self.num_in_queue1)
    def run_server2(self):
        self.num_in_queue2+=1
        if (self.server2==0):
            self.server2=1
            self.t_depart2=self.clock+self.generate_service()
            self.num_in_queue2-=1
            self.response2=self.t_depart2-self.clock
            self.responseTime2+= self.response2
		# schedule next arrival_event
        self.t_arrival=self.clock+self.generate_interarrival()
        print("total_queue_length2= ",self.num_in_queue2)  
    def run_server3(self):
        self.num_in_queue3+=1
        if (self.server3==0):
            self.server3=1
            self.t_depart3=self.clock+self.generate_service()
            self.num_in_queue3-=1
            self.response3=self.t_depart3-self.clock
            self.responseTime3+= self.response3
	    #schedule next arrival_event
        self.t_arrival=self.clock+self.generate_interarrival()
        print("total_queue_length3= ",self.num_in_queue3)
    def departure_event1(self):
        self.num_depart1+=1
        self.server1=0
        print("customer has departed at",self.t_depart1)
        if self.num_in_queue1>0:
            self.run_server1()
        else: 
          self.t_depart2=float('inf')    
        
    def departure_event2(self):
        self.num_depart2+=1
        self.server2=0
        print("customer has departed at",self.t_depart2)
        if self.num_in_queue2>0:
          self.run_server2()
        else: 
          self.t_depart2=float('inf')
        
    def departure_event3(self):
        self.num_depart3+=1
        self.server3=0
        print("customer has departed at",self.t_depart3)
        if self.num_in_queue3>0:
            self.run_server3()
        else:
          self.t_depart2=float('inf')    
            
        
    def generate_interarrival(self):
        return expontial_random_variable(3)
    def generate_service(self):
        return expontial_random_variable(2)

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
  
def expontial_random_variable(mean_value): #function to generate the random expontialy distribuuted variable 
        random_number = lcg() #calling the random number gnerating function
        ERV= (-1/mean_value)*math.log(random_number)
        return ERV  
s = simulation() 
w_t1=[]
w_t2=[]
w_t3=[]
r_s1=[]
r_s2=[]
r_s3=[]
q_l =[]
q_2 =[]
q_3 =[]
while(s.clock<20):
    s.advance_time()
    w_t1.append(s.w_t1)
    w_t2.append(s.w_t2)
    w_t3.append(s.w_t3)
    r_s1.append(s.response1)
    r_s2.append(s.response2)
    r_s3.append(s.response3)
    q_l.append(s.num_in_queue1)
    q_2.append(s.num_in_queue2)
    q_3.append(s.num_in_queue3)
	
print('avrage queue length 1 is ', s.total_wait1/20)
print('avrage queue length 2 is ', s.total_wait2/20)
print('avrage queue length 3 is ', s.total_wait3/20)
print('avrage responce time of server 1 is',s.responseTime1/s.num_depart1)
print('avrage responce time of server 2 is',s.responseTime2/s.num_depart2)
print('avrage responce time of server 3 is',s.responseTime1/s.num_depart3)

plt.hist(r_s1)
plt.xlabel('time in min')
plt.ylabel('server 1 response ')
plt.show()
plt.hist(r_s2)
plt.xlabel('time in min')
plt.ylabel('server 2 response ')
plt.show()
plt.hist(r_s3)
plt.xlabel('time in min')
plt.ylabel('server 3 response ')
plt.show()
plt.hist(q_l)
plt.xlabel('time in min')
plt.ylabel('number of customers waiting in queue1')
plt.show()
plt.hist(q_2)
plt.xlabel('time in min')
plt.ylabel('number of customers waiting in queue2')
plt.show()
plt.hist(q_3)
plt.xlabel('time in min')
plt.ylabel('number of customers waiting in queue3')
plt.show()

			
			
			
			