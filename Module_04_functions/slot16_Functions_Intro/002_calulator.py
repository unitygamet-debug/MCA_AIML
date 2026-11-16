#wap to design a function Non-parmetrized that accepts two number and adds them
#wap to call a functioon named additon
import math


def additon(x,y):
    print(x+y)




#parametrized functions:-
#wap to design a paremertized function with two values outside the function and
#wap to call the paremeterized function-Subtract where the answer must be positive only
#wap to design function a=named circle that accepts radius as an arugments and calculate the circumference the returns the valuea and doesn't print any thing



def circle(x):
    result=2*(math.pi(x))
    return result

def subtract(x,y):
    print(math.fabs(x-y))


#additon(10,20)

print(subtract(10,20))