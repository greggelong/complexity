import matplotlib.pyplot as plt
import random
import math

turns = [0]
totalTurn = [0]
total = [0]
coin = ["H","T"]
counter = 0 # global counter which will be appended into turns

def plotit(x, y, z):   # x is turns, y is running total, z is total per turn
    #plt.plot(x,y,color='green',linestyle='dashed',marker='o',markerfacecolor='blue')

    #plt.plot(x , y)
   # plt.axis(0,max(x),0,max(y))
   
   
    figure, axis = plt.subplots(2)
  
    # For Function
    axis[0].plot(x, y)
    axis[0].set_title("total over turns")
      
    # For Cosine Function
    axis[1].plot(x, z)
    axis[1].set_title("total each turn")
    plt.show()



def taketurn():
    global turns, total, totalTurn, coin, counter
    counter = counter + 1
    turns.append(counter)
    turnTotal =2
    show = ""
    
    # flip a coin if heads get 2 dollars if tails turn total mult by 2
    
    while not show == "H":
        
        show = random.choice(coin)
        #print(show, turnTotal)
        if show == "H":
            
            newTotal = total[-1] + turnTotal
            total.append(newTotal)
            totalTurn.append(turnTotal)
            #print("you win ", turnTotal, counter, " your total is", total[-1])
        else:
            turnTotal = turnTotal * 2
            

for i in range(1000):
    taketurn()
    
    
#print(turns,total)
plotit(turns,total, totalTurn)
print(max(totalTurn), math.log(max(totalTurn),2))
    