import random as r

print("random float number",r.random(),"-",r.random(),"-",r.random())
print ("float random number through uniform is " ,r.uniform(10,99))
print("random integer number",r.randint(1,100))
print("random number",r.randrange(0,100,2))

colors = ['red', 'yellow', 'green','blue']
print(r.choice(colors))  # return only one value
print(r.choices(colors,k=4))
r.shuffle(colors)
print(colors)
r.shuffle(colors)
print(colors)

countries= ["India",'usa','UK','Canada','Australia'] 
print(r.choices(countries,k=7)) # return value that given in argument k=" "
print(r.sample(countries,k=3))