#this is a sample .py file that we can try branching with 
#to keep things less chaotic, I'm giving you each a little bit of code to write

#Beatrice, write a for loop under this comment
for i in range(0,6):
    print(i)

#Charlie, write a while loop under this comment

#Matthew (D'Angelo), write a list under this comment
pizza = ["cheese", "pepperoni", "mushroom", "deep dish", "white", "sausage"]

#Nicholas (DeMatteo), import a library under this comment


=======
import pandas as pd
>>>>>>> main
#Talia, create a simple function under this comment
list_one = [1, 1, 2, 4, 5, 13, 23]

def simple(list_one):
    sort = sorted(set(list_one))
    return sort
print(simple(list_one))

#Jonathan, create a dictionary under this comment
dict_1 = {"Jonathan": 18, "Ben": 14, "Jeff": 16, "Mark": 12}
#Corey, print of something silly under this comment
print(":3") 
#Nicholas (Guarino), create a short conditonal block under this comment
age = 18
if age >= 18:
    print("is an adult")
else:
    print("is a kid")
#Aidan, randomly choose a number using random under this comment
import random
num = random.randint(1,100)
print(num)

#Mina, import a .txt file of your choosing under this comment, make sure the file is in the repo too
f = open('branches-practice/words.txt', 'r')

#Christian, create a ranged for loop under this comment
for i in range(10):
    print(i)

#Fayaz, create a simple program under this comment that incorporates your name

#Ricky, throw in one of our API calls under this comment
import requests

lat = "42.098701"
lon = "-75.912537"

lat_lon_url = f'https://api.weather.gov/points/{lat},{lon}'
request = requests.get(lat_lon_url)

print(request.status_code)

#Sharon, create a list of dictionaries under this comment

#Toyice, use a string method under this comment
my_string = "Hey there"
my_string.replace("there", "what's up")

#Will, use a list method under this comment
letters = ['a', 'b', 'c']
letters.append('d')

#Jake, index a list under this comment

# Hi everyone. It's Ian. 


print('Ian forgot me ☺')
# This is ians test upload=
print('[Hello]')
