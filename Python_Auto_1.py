# -*- coding: utf-8 -*-

# -- Sheet --

# # Python Auto I.


# ##  I. Inputs - pyinputplus


while True:
    print("Provide your age: ")
    age = input()
    try: 
        age = int(age)
    except:
        print("Please provide numeric values")
        continue

    if age < 1:
        print("Provide number bigger than 0")
        continue
    break

print(f"Your age is: {age}")

while True:
    try:
        age = (int(input("Provide your age: ")))
    
    
    except:
        print("Please provide numeric values")
        continue

    if age < 1:
        print("Provide number bigger than 0")
        continue
    break

print(f"Your age is: {age}")

!pip install pyinputplus

import pyinputplus as pyin
answear = pyin.inputNum("Provide a number: ", limit = 5)
print(f"Answear is: {answear}")


import pyinputplus as pyin
answear = pyin.inputInt("Provide a number: ", min = 18, max = 99, blank = True, timeout = 10, default = "NA")
print(f"Answear is: {answear}")

import pyinputplus as pyin
answear = pyin.inputInt("Provide a number: ", allowRegexes= [r' I|X|V|L|C|D|M '])
        
print(f"Answear is: {answear}")

import pyinputplus as pyin
while True:
    answear = pyin.inputYesNo("Do you want to sign the contract: ", yesVal= "yes", noVal= "no")
    print(f"The answear is: {answear} ")
    print("Thank you")
    


    if answear == "no":
        print("Have a good carrer")
        break
        
        


# ## II. Schedule


import time
import schedule

def task():
    print("task done")

schedule.every().day.at("10:04").do(task)

start_time = time.time()
run_seconds = 10  # Run for 10 seconds
while time.time() - start_time < run_seconds:
    schedule.run_pending()
    time.sleep(1)



