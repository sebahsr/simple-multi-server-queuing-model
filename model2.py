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
        self.num_in_queue =0
        self.clock =0.0
        self.t_arrival =self.generate_interarrival()
        self.t_depart1 = float('inf')
        self.t_depart2 = float('inf')
        self.t_depart3 = float('inf')
        self.server1=0 #0:idal 1: buisy 
        self.server2=0
        self.server3=0
        self.num_arrival=0
        self.num_depart1=0
        self.num_depart2=0
        self.num_depart3=0
        self.total_wait=0.0
        self.responseTime1=0
        self.responseTime2=0
        self.responseTime3=0
        self.w_t=0
        self.response1=0
        self.response2=0
        self.response3=0

    def advance_time(self):
        t_event=min(self.t_arrival,self.t_depart1,self.t_depart2,self.t_depart3)
        it= self.clock
        self.clock = t_event
        if self.t_arrival<=min(self.t_depart1,self.t_depart2,self.t_depart3):
            self.arrival_event()  
                 
        elif self.t_depart1<=min(self.t_arrival,self.t_depart2,self.t_depart3):
            
            self.w_t=self.num_in_queue*(self.t_depart1-it)
            self.total_wait += self.w_t
            self.departure_event1()
            

        elif self.t_depart2<=min(self.t_arrival,self.t_depart1,self.t_depart2):
            
            self.w_t=self.num_in_queue*(self.t_depart2-it)
            self.total_wait += self.w_t   
            self.departure_event2()
               
            
        elif self.t_depart3<=min(self.t_arrival,self.t_depart1,self.t_depart2):
            
            self.w_t=self.num_in_queue*(self.t_depart3-it)
            self.total_wait += self.w_t  
            self.departure_event3()
                
             
    def arrival_event(self):
        self.num_in_queue+=1
        self.num_arrival+=1
        print("num_of_customers_arrived ",self.num_arrival)
        self.t_arrival=self.clock+self.generate_interarrival()
        if(self.server1==0 or self.server2==0 or self.server3==0):
          self.accept_customer_to_server()
    def accept_customer_to_server(self):
        if  (self.server1==0 and(self.num_in_queue==1 or (self.server2==1 and self.server3==1))):
            self.server1=1
            self.t_depart1=self.clock+self.generate_service()
            self.response1=self.t_depart1-self.clock
            self.responseTime1+= self.response1 
            self.num_in_queue-=1
        elif (self.server2==0 and(self.num_in_queue==1 or (self.server1==1 and self.server3==1))):
            self.server2=1
            self.t_depart2=self.clock+self.generate_service()
            self.response2=self.t_depart2-self.clock
            self.responseTime2+= self.response2
            self.num_in_queue-=1
        elif (self.server3==0 and(self.num_in_queue==1 or (self.server2==1 and self.server1==1))):
            self.server3=1
            self.t_depart3=self.clock+self.generate_service()
            self.response3=self.t_depart3-self.clock
            self.responseTime3+= self.response3
            self.num_in_queue-=1
        elif ((self.server1==0 and self.server2==0) and (self.num_in_queue==2 or self.server3==1)) :
            self.server1=1
            self.server2=1
            self.t_depart1=self.clock+self.generate_service()
            self.t_depart2=self.clock+self.generate_service()
            self.response1=self.t_depart1-self.clock
            self.responseTime1+= self.response1
            self.response2=self.t_depart2-self.clock
            self.responseTime2+= self.response2
            self.num_in_queue-=2
        elif ((self.server1==0 and self.server3==0) and (self.num_in_queue==2 or self.server2==1)) :
            self.server1=1
            self.server3=1
            self.t_depart1=self.clock+self.generate_service()
            self.t_depart3=self.clock+self.generate_service()
            self.response1=self.t_depart1-self.clock
            self.responseTime1+= self.response1
            self.response3=self.t_depart3-self.clock
            self.responseTime3+= self.response3
            self.num_in_queue-=2
        elif ((self.server2==0 and self.server3==0) and (self.num_in_queue==2 or self.server1==1)) :
            self.server2=1
            self.server3=1
            self.t_depart2=self.clock+self.generate_service()
            self.t_depart3=self.clock+self.generate_service()
            self.response3=self.t_depart3-self.clock
            self.responseTime3+= self.response3
            self.response2=self.t_depart2-self.clock
            self.responseTime2+= self.response2
            self.num_in_queue-=2
        elif (self.num_in_queue>=3 and self.server1==0 and self.server2==0 and self.server3==0):

            self.server1=1
            self.server2=1
            self.server3=1
            self.t_depart1=self.clock+self.generate_service()
            self.t_depart2=self.clock+self.generate_service()
            self.t_depart3=self.clock+self.generate_service()
            self.response1=self.t_depart1-self.clock
            self.responseTime1+= self.response1
            self.response2=self.t_depart2-self.clock
            self.responseTime2+= self.response2
            self.response3=self.t_depart3-self.clock
            self.responseTime3+= self.response3
            self.num_in_queue-=3
    def departure_event1(self):
        self.num_depart1+=1
        self.server1=0
        print("customer has departed at",self.t_depart1) 
        if self.num_in_queue>0:
            self.accept_customer_to_server()
        else:
            self.t_depart1 = float('inf')
          
    def departure_event2(self):
        self.num_depart2+=1
        self.server2=0
        print("customer has departed at",self.t_depart2)  
        if self.num_in_queue>0:
           self.accept_customer_to_server()
        else:
           self.t_depart2 = float('inf')
         
    def departure_event3(self):
        self.num_depart3+=1
        self.server3=0
        print("customer has departed at",self.t_depart3) 
        if self.num_in_queue>0:
            self.accept_customer_to_server()
        else:
          self.t_depart3 = float('inf')
         
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
s=simulation()                 

r_s1=[]
r_s2=[]
r_s3=[]
q_l =[]
while(s.clock<20):
    s.advance_time()
    
    r_s1.append(s.response1)
    r_s2.append(s.response2)
    r_s3.append(s.response3)
    q_l.append(s.num_in_queue)

print('avrage queue length time is ', s.total_wait/2)
print('avrage responce time of server 1 is',s.responseTime1/s.num_depart1)
print('avrage responce time of server 2 is',s.responseTime2/s.num_depart2)
print('avrage responce time of server 3 is',s.responseTime2/s.num_depart3)

plt.hist(r_s1)
plt.xlabel('time in min')
plt.ylabel('server 1 responce ')
plt.show()
plt.hist(r_s2)
plt.xlabel('time in min')
plt.ylabel('server 2 responce ')
plt.show()
plt.hist(r_s3)
plt.xlabel('time in min')
plt.ylabel('server 3 responce ')
plt.show()
plt.hist(q_l)
plt.xlabel('time in min')
plt.ylabel('number of customers waiting in queue')
plt.show()





   