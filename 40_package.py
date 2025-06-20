from world.asia import country as a
from world.europe import country as e
from world  import continent  as c 
#import module from package 
import world.asia.country as a 
#use module 
list = a.getCountries()
print("\n",list)

list2 = e.getCountries()
print("\n",list2)

list3 = c.getContinent()
print("\n",list3)
