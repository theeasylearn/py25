# if we write x=y=10 than both get same value
def nsquare(x, y = 2): #here x is required and y is optional
    return (x*x + 2*x*y + y*y)
result = nsquare(3)  # 3*3 +2*3*2 +2*2
print("result is = ",result)
print("result is =",nsquare(2,3))
print("result is =",nsquare(1))  #nsquare() missing 1 required positional argument: 'x'
print("result is =",nsquare(y=2,x=3))


def marks(english, math,science):  # with parameter without return
	print('Marks in : English is - ', english,', Math - ',math, ', Science - ',science)
marks(20,30,50)
marks(english=50,science=30,math=20)	
