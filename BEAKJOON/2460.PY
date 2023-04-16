max_people = 0  
num_people = 0 

for i in range(10):
    get_off, get_on = map(int, input().split())
    num_people = num_people - get_off + get_on 
    max_people = max(max_people, num_people) 
    
print(max_people)
