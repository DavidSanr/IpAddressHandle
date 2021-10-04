from faker import Faker
import time
ip_address_list:dict = dict()
top100IP:list = []
faker = Faker()
 

def request_handled(ip_address):
    if(ip_address_list.get(ip_address) is not None):
        ip_address_list[ip_address] += 1        
    else:
         ip_address_list[ip_address] = 1
    
    
    

def top100():
    
    for i in sorted(ip_address_list.items(),key=lambda ip_address : ip_address[1],reverse=True):
        top100IP.append(i) 
    if (len(top100IP) > 100):
        return top100IP[:99]
    else:
        return top100IP
        
    
    
def clear():
    ip_address_list.clear()
    top100 = ()
    
    
for _ in range(0,1000000):
    request_handled(faker.ipv4())
start_time = time.time()
print(top100())
print(f"Execution time {time.time() - start_time}")
    
