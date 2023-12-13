## NMI JOB Application
## Coding Test 
## Liam Healey
## 12/6/2023
## Question 2

import random
import statistics

#Build a coin flip function
def flip_coin():
    return random.choice(["Heads", "Tails"])

print(flip_coin())

#test coin flip using the function
for i in range(10):
    print("Flip" + str(i+1) + ": " + flip_coin())


#Run the chunk below as a cell, for it to work properly
#%%
num_trials = 0      #set the number of trials to 0 initally

total_flips_count = {}   #Initialize the count of total flips dictionary

while num_trials <= 10000:  #set number of trials here
    print(num_trials)
    num_trials += 1   #increase the trial number by 1 for each loop
    PersonA_heads = 0   #create a Person A heads variable and set it to 0 for each loop
    PersonB_tails = 0   #create a Person B tails variable and set it to 0 for each loop
    while abs(PersonA_heads - PersonB_tails) < 100:  #Use the absolute value to find the difference between when PersonA and B reaches 100
        if (flip_coin()=="Heads"):  #Coin Flip Heads
            PersonA_heads += 1      #Add 1 to Person A, when the flip is Heads
            PersonB_tails - 1       #Subtract 1 to Person B, when the flip is Tails
        else:                       #Coin Flip Tails
            PersonB_tails += 1      #Add 1 to Person B, when the flip is Tails
            PersonA_heads - 1       #Subtract 1 to Person A, when the flip is Tails
    print("Person A Heads: " + str(PersonA_heads)) 
    print("Person B Tails: " + str(PersonB_tails))
    total_flips = PersonA_heads + PersonB_tails  #Find the total number of flips
    total_flips_count[num_trials] = total_flips  #Add to the 'total_flips_count' dictionary, where 'num_trials' is the key and 'total_flips' is the value
    print("Total Flips: " + str(total_flips))

print(total_flips_count)
res=statistics.mean(list(total_flips_count.values())) #take the mean of the total flips from all trials
print(res)

res_uncertainty=statistics.stdev(list(total_flips_count.values())) #take the standard deviation of the total flips from all trials
print(res_uncertainty)






# %%
